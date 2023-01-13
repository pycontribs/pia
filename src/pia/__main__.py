"""PIA command line."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys

from pia import __version__
from pia.proc import get_local_collections


def main(args: list[str] | None = None) -> None:
    """Execute entrypoint for the pia package."""
    parser = argparse.ArgumentParser(
        prog="pia",
        description="Pia helps you list, install and uninstall Ansible content.",
        epilog="pia is not ready for consumption yet!",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "-f", "--force", action="store_true", default=False, help="Force command."
    )
    # parser.add_argument(
    #     "command",
    #     help="The command to run: install, uninstall or list.",
    # )
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")
    parser_install = subparsers.add_parser("install", help="Installs content")
    parser_install.add_argument(
        "collections", nargs="+", type=str, help="collection name such acme.goodies"
    )

    parser_uninstall = subparsers.add_parser("uninstall", help="Uninstalls content")
    parser_uninstall.add_argument(
        "collections", nargs="+", type=str, help="collection name such acme.goodies"
    )

    parser_list = subparsers.add_parser("list", help="Lists content already installed")
    parser_list.add_argument(
        "format",
        choices=["plain", "json"],
        default="plain",
        const="plain",
        nargs="?",
        help="Output format",
    )

    options = parser.parse_args(args)
    if options.command == "list":

        colmap = get_local_collections()
        if options.format == "plain":
            for collection, data in colmap.items():
                print(f"{collection:40s} {data['version']}")
        elif options.format == "json":
            print(colmap)
        else:
            raise RuntimeError(f"Unknown format {options.format}")
    elif options.command == "install":
        subprocess.run(
            ["ansible-galaxy", "collection", "install", *options.collections],
            check=True,
        )
    elif options.command == "uninstall":
        # https://github.com/ansible/ansible/issues/67759
        colmap = get_local_collections()
        for collection in options.collections:
            if collection in colmap:
                namespace, name = collection.split(".")
                path = colmap[collection]["path"] + f"/{namespace}/{name}"
                print(f"Going to remove {path}")
                shutil.rmtree(path)
            else:
                print(f"Collection {collection} was not found locally.")
    else:
        print(options)
        raise NotImplementedError()
    print(f"pia {__version__} is not ready for consumption yet! {options}")


if __name__ == "__main__":
    main(sys.argv[1:])
