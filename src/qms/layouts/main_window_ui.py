# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QTabWidget, QWidget)

from qms.gui.diagnostic_view import DiagnosticView
from qms.gui.map_view import MapView
from qms.gui.spectrum_view import SpectrumView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.load_profile_action = QAction(MainWindow)
        self.load_profile_action.setObjectName(u"load_profile_action")
        self.save_profile_action = QAction(MainWindow)
        self.save_profile_action.setObjectName(u"save_profile_action")
        self.save_profile_action.setShortcutContext(Qt.WidgetShortcut)
        self.save_profile_as_action = QAction(MainWindow)
        self.save_profile_as_action.setObjectName(u"save_profile_as_action")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.spectrum_tab = SpectrumView()
        self.spectrum_tab.setObjectName(u"spectrum_tab")
        self.tabWidget.addTab(self.spectrum_tab, "")
        self.stability_map_tab = MapView()
        self.stability_map_tab.setObjectName(u"stability_map_tab")
        self.tabWidget.addTab(self.stability_map_tab, "")
        self.diagnostic_tab = DiagnosticView()
        self.diagnostic_tab.setObjectName(u"diagnostic_tab")
        self.tabWidget.addTab(self.diagnostic_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.profile_menu = QMenu(self.menubar)
        self.profile_menu.setObjectName(u"profile_menu")
        self.profile_menu.setToolTipsVisible(True)
        self.load_recent_profile_menu = QMenu(self.profile_menu)
        self.load_recent_profile_menu.setObjectName(u"load_recent_profile_menu")
        self.connection_menu = QMenu(self.menubar)
        self.connection_menu.setObjectName(u"connection_menu")
        self.connection_menu.setToolTipsVisible(True)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.profile_menu.menuAction())
        self.menubar.addAction(self.connection_menu.menuAction())
        self.profile_menu.addAction(self.load_profile_action)
        self.profile_menu.addAction(self.load_recent_profile_menu.menuAction())
        self.profile_menu.addSeparator()
        self.profile_menu.addAction(self.save_profile_action)
        self.profile_menu.addAction(self.save_profile_as_action)
        self.load_recent_profile_menu.addAction(self.actiontest)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_profile_action.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.save_profile_action.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.save_profile_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.save_profile_as_action.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
#if QT_CONFIG(shortcut)
        self.save_profile_as_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectrum_tab), QCoreApplication.translate("MainWindow", u"Spectrum", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stability_map_tab), QCoreApplication.translate("MainWindow", u"Stability Map", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagnostic_tab), QCoreApplication.translate("MainWindow", u"Diagnostics", None))
        self.profile_menu.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.load_recent_profile_menu.setTitle(QCoreApplication.translate("MainWindow", u"Load recent", None))
        self.connection_menu.setTitle(QCoreApplication.translate("MainWindow", u"Connect", None))
    # retranslateUi

