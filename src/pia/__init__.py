"""PIA - Package Installer for Ansible."""
try:
    from pia._version import version as __version__
except ImportError:  # pragma: no branch
    __version__ = "0.1.dev1"

__all__ = ("__version__",)
