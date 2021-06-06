from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QLineEdit, QStyleFactory, QApplication
import sys


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        self.console_log = self.findChild(QtWidgets.QTextEdit, 'console')
        self.work_path = self.findChild(QtWidgets.QLineEdit, 'w_path')
        self.select_wpath_button = self.findChild(QtWidgets.QPushButton, 'wpath_button')
        self.enable_twic = self.findChild(QtWidgets.QCheckBox, 'twic_auto_dl')
        self.enable_proxy = self.findChild(QtWidgets.QCheckBox, 'enable_proxy')
        self.set_proxy = self.findChild(QtWidgets.QPushButton, 'proxy_button')
        self.extract_pgn = self.findChild(QtWidgets.QCheckBox, 'extract_pgn')
        self.delete_zip = self.findChild(QtWidgets.QCheckBox, 'delete_zip')
        self.merge_pgn = self.findChild(QtWidgets.QCheckBox, 'merge_pgn')
        self.delete_pgn = self.findChild(QtWidgets.QCheckBox, 'delete_pgn')
        self.invoke_scid = self.findChild(QtWidgets.QCheckBox, 'invoke_scid')
        self.delete_remaining_pgn = self.findChild(QtWidgets.QCheckBox, 'delete_remaining_pgn')
        self.invoke_scmerge = self.findChild(QtWidgets.QCheckBox, 'invoke_scmerge')
        self.create_zip = self.findChild(QtWidgets.QCheckBox, 'create_zip')
        self.delete_scid = self.findChild(QtWidgets.QCheckBox, 'delete_scid')
        self.select_db = self.findChild(QtWidgets.QComboBox, 'select_db')
        self.add_db_button = self.findChild(QtWidgets.QPushButton, 'add_db')
        self.delete_db_button = self.findChild(QtWidgets.QPushButton, 'delete_db')
        self.default_db = self.findChild(QtWidgets.QCheckBox, 'default_db')
        self.start = self.findChild(QtWidgets.QPushButton, 'start')
        self.exit = self.findChild(QtWidgets.QPushButton, 'exit')

        self.console_log.setAlignment(Qt.AlignCenter)
        self.console_log.insertPlainText("pgn2scid 2.0.beta0\n")
        self.console_log.insertPlainText("Copyright (c) 2017 - 2021 Andreas Kreisig\n")
        self.console_log.insertPlainText("Released under the terms of the GPL v3\n")
        self.console_log.insertPlainText("This program comes with absolutely NO WARRANTY\n")
        self.console_log.insertPlainText("pgnscid & scmerge copyright (c) by Shane Hudson\n")


