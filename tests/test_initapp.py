# # -*- coding: utf-8 -*-
# type: ignore

import pytest
import os
from importlib.metadata import version
import time

from pgn2scid_v2 import initapp

toml_config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..', 'src', 'pgn2scid_v2'))
toml_config_file = os.path.abspath(os.path.join(toml_config_path,
                                                'pgn2scid.toml'))


# Preparation
@pytest.fixture()
def delete_toml():
    if os.path.isfile(toml_config_file):
        os.remove('pgn2scid.toml')
        time.sleep(0.3)


def test_version():
    v = version('pgn2scid_v2')
    assert v == "2.0.1a0"


def test_init_toml(delete_toml):
    initapp.init_toml_file()
    toml_file = os.path.isfile(toml_config_file)
    assert toml_file is True


def test_get_config(delete_toml):
    config = initapp.get_app_config
    assert config['GENERAL']['enable_twic_auto_dl'] == 0
    assert config['GENERAL']['twic_max'] == 0
    assert config['GENERAL']['extract_pgn_files'] == 0
    assert config['GENERAL']['delete_zip_files'] == 0
    assert config['GENERAL']['merge_pgn_files'] == 0
    assert config['GENERAL']['delete_pgn_files'] == 0
    assert config['GENERAL']['convert_pgn_to_scid'] == 0
    assert config['GENERAL']['delete_remaining_pgn'] == 0
    assert config['GENERAL']['merge_scid_database'] == 0
    assert config['GENERAL']['write_zipped_scid_copy'] == 0
    assert config['GENERAL']['ask_before_merging'] == 0
    assert config['GENERAL']['delete_scid_files'] == 0
    assert config['PATHS']['working_path'] == ''
    assert config['PATHS']['database_dir'] == ''
