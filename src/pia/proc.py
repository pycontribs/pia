"""Module to work with processes."""
from __future__ import annotations

import json
import subprocess

# noqa: FA100
from typing import Mapping, Sequence, Union

JsonValueType = Union[
    None,
    str,
    int,
    float,
    bool,
    Sequence["JsonValueType"],
    Mapping[str, "JsonValueType"],
]
JsonObjectType = Mapping[str, JsonValueType]


def json_from_cmd(cmd: list[str]) -> JsonObjectType:
    """Return loaded JSON output from external command."""
    result = subprocess.run(cmd, check=True, capture_output=True)
    data = json.loads(result.stdout)
    if not isinstance(data, dict):
        raise RuntimeError("Unexpected data.")
    return data


def get_local_collections() -> dict[str, dict[str, str]]:
    """Return locally installed collections with their version and path."""
    result = json_from_cmd(["ansible-galaxy", "collection", "list", "--format=json"])
    colmap = {}
    if not isinstance(result, dict):
        raise RuntimeError(f"Unexpected data {result}")
    for path, collections in result.items():
        for k, value in collections.items():
            colmap[k] = {"version": value.get("version", None), "path": path}
    colmap = dict(sorted(colmap.items()))
    return colmap
