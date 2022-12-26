# -*- coding: utf-8 -*-
# type: ignore

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from gui import Ui_QMainWindow


class MainWindow(QMainWindow, Ui_QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.show

app = QApplication()
app.setStyle('Fusion')
main_window = MainWindow()
main_window.show()
app.exec()