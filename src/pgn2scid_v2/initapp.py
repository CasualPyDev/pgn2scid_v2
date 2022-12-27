# -*- coding: utf-8 -*-
# type: ignore

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
import tomli_w

def create_toml_file():
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
            "delete_scid_files": 0,
        },
        "PATHS": {
            "work_path": "",
            "database_dir": "",
            "default_database": "",
        }
    }
    with open('pgn2scid.toml', mode='wb') as fw:
        tomli_w.dump(config, fw)



def read_config():
    try:
        with open('pgn2scid.toml', mode='rb') as fr:
            config = tomllib.load(fr)
        return config
    except FileNotFoundError:
        create_toml_file()


app_config_read = read_config()
