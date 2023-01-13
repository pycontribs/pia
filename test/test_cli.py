"""Tests for PIA."""
import pytest

from pia.__main__ import main


def test_version() -> None:
    """Sample test."""
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])
    assert excinfo.value.code == 0
