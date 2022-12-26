# tests/test_pgn2scid.py

from importlib.metadata import version

v = version('pgn2scid_v2')

def test_version():
    assert v == "2.1.0"
