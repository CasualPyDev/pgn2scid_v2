import tomli

def read_config():
        with open ('pgn2scid.toml', mode='rb') as fp:
            config = tomli.load(fp)
        return config


app_config_read = read_config()
