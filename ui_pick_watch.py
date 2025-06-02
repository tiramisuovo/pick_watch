# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movie.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 802)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionSave_my_list = QAction(MainWindow)
        self.actionSave_my_list.setObjectName(u"actionSave_my_list")
        self.actionLoad_my_list = QAction(MainWindow)
        self.actionLoad_my_list.setObjectName(u"actionLoad_my_list")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(370, 70, 113, 21))
        self.input.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    padding: 3px;\n"
"}")
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(280, 70, 81, 16))
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(70, 120, 47, 20))
        self.release_label = QLabel(self.centralwidget)
        self.release_label.setObjectName(u"release_label")
        self.release_label.setGeometry(QRect(70, 160, 91, 16))
        self.desc_label = QLabel(self.centralwidget)
        self.desc_label.setObjectName(u"desc_label")
        self.desc_label.setGeometry(QRect(70, 200, 81, 16))
        self.poster_label = QLabel(self.centralwidget)
        self.poster_label.setObjectName(u"poster_label")
        self.poster_label.setGeometry(QRect(70, 360, 47, 13))
        self.title_display = QLabel(self.centralwidget)
        self.title_display.setObjectName(u"title_display")
        self.title_display.setGeometry(QRect(160, 120, 361, 21))
        self.poster_display = QLabel(self.centralwidget)
        self.poster_display.setObjectName(u"poster_display")
        self.poster_display.setGeometry(QRect(160, 360, 200, 300))
        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(510, 70, 75, 23))
        self.search_button.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    border-radius: 4px;\n"
"}")
        self.fav_pushbutton = QPushButton(self.centralwidget)
        self.fav_pushbutton.setObjectName(u"fav_pushbutton")
        self.fav_pushbutton.setGeometry(QRect(160, 690, 101, 23))
        self.fav_pushbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    border-radius: 4px;\n"
"}")
        self.fav_label = QLabel(self.centralwidget)
        self.fav_label.setObjectName(u"fav_label")
        self.fav_label.setGeometry(QRect(600, 110, 171, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Text Semibold"])
        font.setBold(True)
        self.fav_label.setFont(font)
        self.fav_label.setTextFormat(Qt.AutoText)
        self.fav_label.setAlignment(Qt.AlignCenter)
        self.release_display = QLabel(self.centralwidget)
        self.release_display.setObjectName(u"release_display")
        self.release_display.setGeometry(QRect(160, 160, 361, 21))
        self.fav_list = QListWidget(self.centralwidget)
        self.fav_list.setObjectName(u"fav_list")
        self.fav_list.setGeometry(QRect(570, 160, 231, 491))
        self.moviescout_label = QLabel(self.centralwidget)
        self.moviescout_label.setObjectName(u"moviescout_label")
        self.moviescout_label.setGeometry(QRect(350, 20, 231, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Text Semibold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.moviescout_label.setFont(font1)
        self.toggle_button = QPushButton(self.centralwidget)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setGeometry(QRect(50, 50, 75, 23))
        self.toggle_button.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    padding: 5px;\n"
"    border-radius: 4px;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 111, 21))
        self.desc_display = QTextBrowser(self.centralwidget)
        self.desc_display.setObjectName(u"desc_display")
        self.desc_display.setGeometry(QRect(160, 200, 361, 131))
        self.desc_display.setStyleSheet(u"border:none;\n"
"background: transparent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 884, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionSave_my_list)
        self.menuMenu.addAction(self.actionLoad_my_list)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_my_list.setText(QCoreApplication.translate("MainWindow", u"Save my list", None))
        self.actionLoad_my_list.setText(QCoreApplication.translate("MainWindow", u"Load my list", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Enter a title:", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.release_label.setText(QCoreApplication.translate("MainWindow", u"Release date", None))
        self.desc_label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.poster_label.setText(QCoreApplication.translate("MainWindow", u"Poster", None))
        self.title_display.setText("")
        self.poster_display.setText("")
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.fav_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Add to Favorite", None))
        self.fav_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">~ My Favourite List ~</span></p></body></html>", None))
        self.release_display.setText("")
        self.moviescout_label.setText(QCoreApplication.translate("MainWindow", u"Pick & Watch!", None))
        self.toggle_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Click to toggle mode!", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

