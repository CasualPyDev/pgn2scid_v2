import configparser
import os
import sys
import ui_init


def write(OP_SYS):
    if OP_SYS == 'Windows':
        init_file = os.path.join(os.environ['APPDATA'], 'pgn2scid.ini')
    else:
        init_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'pgn2scid.ini')
    config = configparser.ConfigParser()
    chck_twic = ui_init.MainUi.enable_twic.checkState()
    chck_proxy = ui_init.MainUi.enable_proxy.checkState()
    chck_extract_pgn = ui_init.MainUi.extract_pgn.checkState()
    chck_delete_zip = ui_init.MainUi.delete_zip.checkState()
    chck_merge_pgn = ui_init.MainUi.merge_pgn.checkState()
    chck_delete_pgn = ui_init.MainUi.delete_pgn.checkState()
    chck_invoke_scid = ui_init.MainUi.invoke_scid.checkState()
    chck_delete_remaining_pgn = ui_init.MainUi.delete_remaining_pgn.checkState()
    chck_invoke_scmerge = ui_init.MainUi.invoke_scmerge.checkState()
    chck_create_zip = ui_init.MainUi.create_zip.checkState()
    chck_delete_scid = ui_init.MainUi.delete_scid.checkState()
    chck_default_db = ui_init.MainUi.default_db.checkState()