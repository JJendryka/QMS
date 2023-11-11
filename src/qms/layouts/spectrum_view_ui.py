# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrum_view.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

from qms.gui.spectrum_control import SpectrumControl
from qms.gui.spectrum_plot import SpectrumPlot

class Ui_SpectrumView(object):
    def setupUi(self, SpectrumView):
        if not SpectrumView.objectName():
            SpectrumView.setObjectName(u"SpectrumView")
        SpectrumView.resize(400, 300)
        self.verticalLayout = QVBoxLayout(SpectrumView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(SpectrumView)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.spectrum_plot = SpectrumPlot(self.splitter)
        self.spectrum_plot.setObjectName(u"spectrum_plot")
        sizePolicy.setHeightForWidth(self.spectrum_plot.sizePolicy().hasHeightForWidth())
        self.spectrum_plot.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.spectrum_plot)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.widget_2)

        self.verticalLayout.addWidget(self.splitter)

        self.spectrum_control = SpectrumControl(SpectrumView)
        self.spectrum_control.setObjectName(u"spectrum_control")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spectrum_control.sizePolicy().hasHeightForWidth())
        self.spectrum_control.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.spectrum_control)


        self.retranslateUi(SpectrumView)

        QMetaObject.connectSlotsByName(SpectrumView)
    # setupUi

    def retranslateUi(self, SpectrumView):
        SpectrumView.setWindowTitle(QCoreApplication.translate("SpectrumView", u"Form", None))
    # retranslateUi

