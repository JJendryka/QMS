# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QMenu, QMenuBar, QSizePolicy, QTabWidget, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.load_profile_action = QAction(MainWindow)
        self.load_profile_action.setObjectName("load_profile_action")
        self.save_profile_action = QAction(MainWindow)
        self.save_profile_action.setObjectName("save_profile_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.spectrum_tab = QWidget()
        self.spectrum_tab.setObjectName("spectrum_tab")
        self.tabWidget.addTab(self.spectrum_tab, "")
        self.stability_map_tab = QWidget()
        self.stability_map_tab.setObjectName("stability_map_tab")
        self.tabWidget.addTab(self.stability_map_tab, "")
        self.diagnostics_tab = QWidget()
        self.diagnostics_tab.setObjectName("diagnostics_tab")
        self.tabWidget.addTab(self.diagnostics_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.profile_menu = QMenu(self.menubar)
        self.profile_menu.setObjectName("profile_menu")
        self.connection_menu = QMenu(self.menubar)
        self.connection_menu.setObjectName("connection_menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.profile_menu.menuAction())
        self.menubar.addAction(self.connection_menu.menuAction())
        self.profile_menu.addAction(self.load_profile_action)
        self.profile_menu.addAction(self.save_profile_action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.load_profile_action.setText(QCoreApplication.translate("MainWindow", "Load profile", None))
        self.save_profile_action.setText(QCoreApplication.translate("MainWindow", "Save profile", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.spectrum_tab), QCoreApplication.translate("MainWindow", "Spectrum", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.stability_map_tab),
            QCoreApplication.translate("MainWindow", "Stability Map", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.diagnostics_tab), QCoreApplication.translate("MainWindow", "Diagnostics", None)
        )
        self.profile_menu.setTitle(QCoreApplication.translate("MainWindow", "Profile", None))
        self.connection_menu.setTitle(QCoreApplication.translate("MainWindow", "Connection", None))

    # retranslateUi
