import configparser
import os
import sys


def write(app_setup, OP_SYS):
    if OP_SYS == 'Windows':
        init_file = os.path.join(os.environ['APPDATA'], 'pgn2scid.ini')
    else:
        init_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'pgn2scid.ini')
    config = configparser.ConfigParser()