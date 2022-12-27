import tomli

def create_toml_file():
    pass

def read_config():
    try:
        with open ('pgn2scid.toml', mode='rb') as fp:
            config = tomli.load(fp)
        return config
    except FileNotFoundError:
        create_toml_file()

app_config_read = read_config()
