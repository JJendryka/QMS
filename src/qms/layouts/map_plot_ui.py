# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map_plot.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_map_plot(object):
    def setupUi(self, map_plot):
        if not map_plot.objectName():
            map_plot.setObjectName(u"map_plot")
        map_plot.resize(1073, 542)
        self.verticalLayout = QVBoxLayout(map_plot)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.log_checkbox = QCheckBox(map_plot)
        self.log_checkbox.setObjectName(u"log_checkbox")

        self.horizontalLayout.addWidget(self.log_checkbox)

        self.line = QFrame(map_plot)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.current_min_label = QLabel(map_plot)
        self.current_min_label.setObjectName(u"current_min_label")

        self.horizontalLayout.addWidget(self.current_min_label)

        self.current_min_lineedit = QLineEdit(map_plot)
        self.current_min_lineedit.setObjectName(u"current_min_lineedit")
        self.current_min_lineedit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_min_lineedit.sizePolicy().hasHeightForWidth())
        self.current_min_lineedit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.current_min_lineedit)

        self.current_min_unit_label = QLabel(map_plot)
        self.current_min_unit_label.setObjectName(u"current_min_unit_label")

        self.horizontalLayout.addWidget(self.current_min_unit_label)

        self.line_2 = QFrame(map_plot)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.current_max_label = QLabel(map_plot)
        self.current_max_label.setObjectName(u"current_max_label")

        self.horizontalLayout.addWidget(self.current_max_label)

        self.current_max_lineedit = QLineEdit(map_plot)
        self.current_max_lineedit.setObjectName(u"current_max_lineedit")
        self.current_max_lineedit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.current_max_lineedit.sizePolicy().hasHeightForWidth())
        self.current_max_lineedit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.current_max_lineedit)

        self.current_max_unit_label = QLabel(map_plot)
        self.current_max_unit_label.setObjectName(u"current_max_unit_label")

        self.horizontalLayout.addWidget(self.current_max_unit_label)

        self.line_3 = QFrame(map_plot)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.scale_current_checkbox = QCheckBox(map_plot)
        self.scale_current_checkbox.setObjectName(u"scale_current_checkbox")
        self.scale_current_checkbox.setChecked(True)

        self.horizontalLayout.addWidget(self.scale_current_checkbox)

        self.scale_rf_button = QPushButton(map_plot)
        self.scale_rf_button.setObjectName(u"scale_rf_button")
        self.scale_rf_button.setEnabled(True)

        self.horizontalLayout.addWidget(self.scale_rf_button)

        self.scale_dc_button = QPushButton(map_plot)
        self.scale_dc_button.setObjectName(u"scale_dc_button")
        self.scale_dc_button.setEnabled(True)

        self.horizontalLayout.addWidget(self.scale_dc_button)

        self.scanline_checkbox = QCheckBox(map_plot)
        self.scanline_checkbox.setObjectName(u"scanline_checkbox")
        self.scanline_checkbox.setEnabled(True)
        self.scanline_checkbox.setChecked(True)

        self.horizontalLayout.addWidget(self.scanline_checkbox)

        self.save_button = QPushButton(map_plot)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.canvas_temp = QWidget(map_plot)
        self.canvas_temp.setObjectName(u"canvas_temp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.canvas_temp.sizePolicy().hasHeightForWidth())
        self.canvas_temp.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.canvas_temp)

        self.toolbar_temp = QWidget(map_plot)
        self.toolbar_temp.setObjectName(u"toolbar_temp")

        self.verticalLayout.addWidget(self.toolbar_temp)


        self.retranslateUi(map_plot)

        QMetaObject.connectSlotsByName(map_plot)
    # setupUi

    def retranslateUi(self, map_plot):
        map_plot.setWindowTitle(QCoreApplication.translate("map_plot", u"Form", None))
#if QT_CONFIG(tooltip)
        self.log_checkbox.setToolTip(QCoreApplication.translate("map_plot", u"Plot current data wih logarithmic scale", None))
#endif // QT_CONFIG(tooltip)
        self.log_checkbox.setText(QCoreApplication.translate("map_plot", u"Log current", None))
        self.current_min_label.setText(QCoreApplication.translate("map_plot", u"Current Min:", None))
        self.current_min_unit_label.setText(QCoreApplication.translate("map_plot", u"[A]", None))
        self.current_max_label.setText(QCoreApplication.translate("map_plot", u"Current Max:", None))
        self.current_max_unit_label.setText(QCoreApplication.translate("map_plot", u"[A]", None))
        self.scale_current_checkbox.setText(QCoreApplication.translate("map_plot", u"Scale Current", None))
        self.scale_rf_button.setText(QCoreApplication.translate("map_plot", u"Scale RF", None))
        self.scale_dc_button.setText(QCoreApplication.translate("map_plot", u"Scale DC", None))
        self.scanline_checkbox.setText(QCoreApplication.translate("map_plot", u"Show Scanline", None))
        self.save_button.setText(QCoreApplication.translate("map_plot", u"Save", None))
    # retranslateUi

