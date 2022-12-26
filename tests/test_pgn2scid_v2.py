# tests/test_pgn2scid.py

from importlib.metadata import version
v = version('pgn2scid-v2')

def test_version():
    assert v == "0.1.0"
