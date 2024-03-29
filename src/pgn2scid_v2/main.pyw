# -*- coding: utf-8 -*-
# type: ignore

# import sys
# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from gui import Ui_QMainWindow

import initapp


class MainWindow(QMainWindow, Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


initapp.get_app_config

app = QApplication()
app.setStyle('Fusion')
main_window = MainWindow()
main_window.show()
app.exec()
