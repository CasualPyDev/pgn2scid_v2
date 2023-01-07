# tests/test_pgn2scid.py

import pytest
import os
from importlib.metadata import version
import time

from pgn2scid_v2 import initapp

toml_config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'pgn2scid_v2'))
toml_config_file = os.path.abspath(os.path.join(toml_config_path, 'pgn2scid.toml'))


def test_version():
    v = version('pgn2scid_v2')
    assert v == "2.1.0"


# Preperation
@pytest.fixture(scope='session')
def delete_toml():
    os.chdir(toml_config_path)
    if os.path.isfile(toml_config_file):
        os.remove('pgn2scid.toml')
        time.sleep(0.3)


def test_init_toml(delete_toml):
    pass
    initapp.init_toml_file()
    toml_file = os.path.isfile(toml_config_file)
    assert toml_file is True
