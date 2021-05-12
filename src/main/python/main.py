from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets, uic, QtGui
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    class Ui(QtWidgets.QMainWindow):
        def __init__(self):
            super(Ui, self).__init__()
            uic.loadUi('ui/pgn2scid.ui', self)
            self.show()

            self.console_log = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit')


    window = Ui()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

    cursor = QTextCursor(console_log.document())
    cursor.setPosition(0)
    textEdit.setTextCursor(cursor)
    window.console_log.insertPlainText("Hallo")

