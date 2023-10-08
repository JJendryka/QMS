# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map_view.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from map_control import MapControl
from map_plot import MapPlot

class Ui_map_view(object):
    def setupUi(self, map_view):
        if not map_view.objectName():
            map_view.setObjectName(u"map_view")
        map_view.resize(611, 489)
        self.verticalLayout = QVBoxLayout(map_view)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.map_plot = MapPlot(map_view)
        self.map_plot.setObjectName(u"map_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_plot.sizePolicy().hasHeightForWidth())
        self.map_plot.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.map_plot)

        self.map_control = MapControl(map_view)
        self.map_control.setObjectName(u"map_control")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.map_control.sizePolicy().hasHeightForWidth())
        self.map_control.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.map_control)


        self.retranslateUi(map_view)

        QMetaObject.connectSlotsByName(map_view)
    # setupUi

    def retranslateUi(self, map_view):
        map_view.setWindowTitle(QCoreApplication.translate("map_view", u"Form", None))
    # retranslateUi

