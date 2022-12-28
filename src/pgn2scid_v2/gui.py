# -*- coding: utf-8 -*-
# type: ignore

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QTextEdit, QWidget)


class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(715, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            QMainWindow.sizePolicy().hasHeightForWidth())
        QMainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        QMainWindow.setFont(font)
        QMainWindow.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.pgn2scid_2 = QWidget(QMainWindow)
        self.pgn2scid_2.setObjectName(u"pgn2scid_2")
        self.pgn2scid_2.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.pgn2scid_2.sizePolicy().hasHeightForWidth())
        self.pgn2scid_2.setSizePolicy(sizePolicy)
        self.pgn2scid_2.setMinimumSize(QSize(715, 725))
        self.pgn2scid_2.setMaximumSize(QSize(715, 725))
        self.console = QTextEdit(self.pgn2scid_2)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(10, 10, 691, 151))
        self.console.setFocusPolicy(Qt.WheelFocus)
        self.console.setAcceptDrops(False)
        self.w_path = QLineEdit(self.pgn2scid_2)
        self.w_path.setObjectName(u"w_path")
        self.w_path.setGeometry(QRect(150, 180, 501, 32))
        self.w_path.setFont(font)
        self.working_path = QLabel(self.pgn2scid_2)
        self.working_path.setObjectName(u"working_path")
        self.working_path.setGeometry(QRect(10, 187, 141, 18))
        font1 = QFont()
        font1.setPointSize(12)
        self.working_path.setFont(font1)
        self.wpath_button = QPushButton(self.pgn2scid_2)
        self.wpath_button.setObjectName(u"wpath_button")
        self.wpath_button.setGeometry(QRect(660, 180, 41, 34))
        self.twic_auto_dl = QCheckBox(self.pgn2scid_2)
        self.twic_auto_dl.setObjectName(u"twic_auto_dl")
        self.twic_auto_dl.setGeometry(QRect(10, 230, 281, 22))
        self.twic_auto_dl.setFont(font1)
        self.enable_proxy = QCheckBox(self.pgn2scid_2)
        self.enable_proxy.setObjectName(u"enable_proxy")
        self.enable_proxy.setEnabled(False)
        self.enable_proxy.setGeometry(QRect(30, 260, 291, 22))
        self.enable_proxy.setFont(font1)
        self.extract_pgn = QCheckBox(self.pgn2scid_2)
        self.extract_pgn.setObjectName(u"extract_pgn")
        self.extract_pgn.setGeometry(QRect(10, 300, 521, 22))
        self.extract_pgn.setFont(font1)
        self.proxy_button = QPushButton(self.pgn2scid_2)
        self.proxy_button.setObjectName(u"proxy_button")
        self.proxy_button.setEnabled(False)
        self.proxy_button.setGeometry(QRect(660, 250, 41, 34))
        self.delete_zip = QCheckBox(self.pgn2scid_2)
        self.delete_zip.setObjectName(u"delete_zip")
        self.delete_zip.setEnabled(False)
        self.delete_zip.setGeometry(QRect(30, 330, 501, 22))
        self.delete_zip.setFont(font1)
        self.merge_pgn = QCheckBox(self.pgn2scid_2)
        self.merge_pgn.setObjectName(u"merge_pgn")
        self.merge_pgn.setGeometry(QRect(10, 370, 481, 22))
        self.merge_pgn.setFont(font1)
        self.delete_pgn = QCheckBox(self.pgn2scid_2)
        self.delete_pgn.setObjectName(u"delete_pgn")
        self.delete_pgn.setEnabled(False)
        self.delete_pgn.setGeometry(QRect(30, 400, 311, 22))
        self.delete_pgn.setFont(font1)
        self.invoke_pgnscid = QCheckBox(self.pgn2scid_2)
        self.invoke_pgnscid.setObjectName(u"invoke_pgnscid")
        self.invoke_pgnscid.setGeometry(QRect(10, 440, 461, 22))
        self.invoke_pgnscid.setFont(font1)
        self.delete_remaining_pgn = QCheckBox(self.pgn2scid_2)
        self.delete_remaining_pgn.setObjectName(u"delete_remaining_pgn")
        self.delete_remaining_pgn.setEnabled(False)
        self.delete_remaining_pgn.setGeometry(QRect(30, 470, 401, 22))
        self.delete_remaining_pgn.setFont(font1)
        self.invoke_scmerge = QCheckBox(self.pgn2scid_2)
        self.invoke_scmerge.setObjectName(u"invoke_scmerge")
        self.invoke_scmerge.setGeometry(QRect(10, 510, 491, 22))
        self.invoke_scmerge.setFont(font1)
        self.create_zip = QCheckBox(self.pgn2scid_2)
        self.create_zip.setObjectName(u"create_zip")
        self.create_zip.setEnabled(False)
        self.create_zip.setGeometry(QRect(30, 540, 561, 22))
        self.create_zip.setFont(font1)
        self.delete_scid = QCheckBox(self.pgn2scid_2)
        self.delete_scid.setObjectName(u"delete_scid")
        self.delete_scid.setEnabled(False)
        self.delete_scid.setGeometry(QRect(30, 570, 341, 22))
        self.delete_scid.setFont(font1)
        self.select_db_labe = QLabel(self.pgn2scid_2)
        self.select_db_labe.setObjectName(u"select_db_labe")
        self.select_db_labe.setEnabled(False)
        self.select_db_labe.setGeometry(QRect(30, 607, 131, 18))
        self.select_db_labe.setFont(font1)
        self.delete_db = QPushButton(self.pgn2scid_2)
        self.delete_db.setObjectName(u"delete_db")
        self.delete_db.setEnabled(False)
        self.delete_db.setGeometry(QRect(660, 600, 41, 34))
        self.start = QPushButton(self.pgn2scid_2)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(10, 680, 88, 34))
        font2 = QFont()
        font2.setPointSize(14)
        self.start.setFont(font2)
        self.exit = QPushButton(self.pgn2scid_2)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(100, 680, 88, 34))
        self.exit.setFont(font2)
        self.select_db = QComboBox(self.pgn2scid_2)
        self.select_db.setObjectName(u"select_db")
        self.select_db.setGeometry(QRect(160, 600, 441, 32))
        self.select_db.setFont(font)
        self.add_db = QPushButton(self.pgn2scid_2)
        self.add_db.setObjectName(u"add_db")
        self.add_db.setEnabled(False)
        self.add_db.setGeometry(QRect(610, 600, 41, 34))
        self.default_db = QCheckBox(self.pgn2scid_2)
        self.default_db.setObjectName(u"default_db")
        self.default_db.setEnabled(False)
        self.default_db.setGeometry(QRect(30, 640, 351, 22))
        self.default_db.setFont(font1)
        self.line = QFrame(self.pgn2scid_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 660, 691, 16))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        self.line.setFont(font3)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        QMainWindow.setCentralWidget(self.pgn2scid_2)

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)
    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate(
            "QMainWindow", u"pgn2scid", None))
        self.working_path.setText(QCoreApplication.translate(
            "QMainWindow", u"Set working path:", None))
        self.wpath_button.setText(QCoreApplication.translate(
            "QMainWindow", u"PushButton", None))
        self.twic_auto_dl.setText(QCoreApplication.translate(
            "QMainWindow", u"Enable the TWIC auto downloader", None))
        self.enable_proxy.setText(QCoreApplication.translate(
            "QMainWindow", u"Enable manual proxy configuration", None))
        self.extract_pgn.setText(QCoreApplication.translate(
            "QMainWindow", u"Extract PGN files from ZIP archives", None))
        self.proxy_button.setText(QCoreApplication.translate(
            "QMainWindow", u"PushButton", None))
        self.delete_zip.setText(QCoreApplication.translate(
            "QMainWindow", u"Delete ZIP files after decompressing", None))
        self.merge_pgn.setText(QCoreApplication.translate(
            "QMainWindow", u"Merge all PGN files to one monolithic file", None))
        self.delete_pgn.setText(QCoreApplication.translate(
            "QMainWindow", u"Delete single PGN files after merging", None))
        self.invoke_pgnscid.setText(QCoreApplication.translate(
            "QMainWindow", u"Invoke 'pgnscid' to convert PGN files to native Scid format", None))
        self.delete_remaining_pgn.setText(QCoreApplication.translate(
            "QMainWindow", u"Delete remaining PGN files after data conversion", None))
        self.invoke_scmerge.setText(QCoreApplication.translate(
            "QMainWindow", u"Invoke 'scmerge' to merge Scid files with an existing database", None))
        self.create_zip.setText(QCoreApplication.translate(
            "QMainWindow", u"Create a ZIP compressed copy of the existing database before merging", None))
        self.delete_scid.setText(QCoreApplication.translate(
            "QMainWindow", u"Delete remaining Scid files after merging", None))
        self.select_db_labe.setText(QCoreApplication.translate(
            "QMainWindow", u"Select database:", None))
        self.delete_db.setText(QCoreApplication.translate(
            "QMainWindow", u"PushButton", None))
        self.start.setText(QCoreApplication.translate(
            "QMainWindow", u"START", None))
        self.exit.setText(QCoreApplication.translate(
            "QMainWindow", u"Exit", None))
# if QT_CONFIG(tooltip)
        self.add_db.setToolTip("")
# endif // QT_CONFIG(tooltip)
        self.add_db.setText(QCoreApplication.translate(
            "QMainWindow", u"PushButton", None))
        self.default_db.setText(QCoreApplication.translate(
            "QMainWindow", u"Use selected database as default database", None))
    # retranslateUi
