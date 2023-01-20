# -*- coding: utf-8 -*-
# type: ignore

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
import tomli_w
import time


def init_toml_file():
    config = {
        "GENERAL": {
            "enable_twic_auto_dl": 0,
            "twic_max": 0,
            "extract_pgn_files": 0,
            "delete_zip_files": 0,
            "merge_pgn_files": 0,
            "delete_pgn_files": 0,
            "convert_pgn_to_scid": 0,
            "delete_remaining_pgn": 0,
            "merge_scid_database": 0,
            "write_zipped_scid_copy": 0,
            "ask_before_merging": 0,
            "delete_scid_files": 0,
        },
        "PATHS": {
            "working_path": "",
            "database_dir": "",
        }
    }
    with open('pgn2scid.toml', mode='wb') as fw:
        tomli_w.dump(config, fw)


def get_config():
    try:
        with open('pgn2scid.toml', mode='rb') as fr:
            config = tomllib.load(fr)
        return config
    except FileNotFoundError:
        init_toml_file()
        time.sleep(0.5)
        with open('pgn2scid.toml', mode='rb') as fr:
            config = tomllib.load(fr)
        return config


def set_config():
    pass


get_app_config = get_config()
