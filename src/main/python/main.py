from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets, uic, QtGui
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QLineEdit

import sys


appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/pgn2scid.ui', self)
        self.show()

        self.console_log = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit')
        self.work_path = self.findChild(QtWidgets.QLineEdit, 'w_path')
        self.select_wpath_button = self.findChild(QtWidgets.QPushButton, 'wpath_button')
        self.enable_twic = self.findChild(QtWidgets.QCheckBox, 'twic_auto_dl')
        self.enable_proxy = self.findChild(QtWidgets.QCheckBox, 'enable_proxy')
        self.extract_pgn = self.findChild(QtWidgets.QCheckBox, 'extract_pgn')
        self.delete_zip = self.findChild(QtWidgets.QCheckBox, 'delete_zip')
        self.merge_pgn = self.findChild(QtWidgets.QCheckBox, 'merge_pgn')
        self.delete_pgn = self.findChild(QtWidgets.QCheckBox, 'delete_pgn')
        self.invoke_scid = self.findChild(QtWidgets.QCheckBox, 'invoke_scid')
        self.delete_remaining_pgn = self.findChild(QtWidgets.QCheckBox, 'delete_remaining_pgn')
        self.invoke_scmerge = self.findChild(QtWidgets.QCheckBox, 'invoke_scmerge')
        self.create_zip = self.findChild(QtWidgets.QCheckBox, 'create_zip')
        self.delete_scid = self.findChild(QtWidgets.QCheckBox, 'delete_scid')
        self.select_db = self.findChild(QtWidgets.QLineEdit, 'select_db_edit')
        self.select_db_button = self.findChild(QtWidgets.QPushButton, 'select_db_button')
        self.start = self.findChild(QtWidgets.QPushButton, 'start')
        self.exit = self.findChild(QtWidgets.QPushButton, 'exit')


if __name__ == '__main__':
    window = Ui()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
