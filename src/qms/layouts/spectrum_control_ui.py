# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrum_control.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_spectrum_control(object):
    def setupUi(self, spectrum_control):
        if not spectrum_control.objectName():
            spectrum_control.setObjectName(u"spectrum_control")
        spectrum_control.resize(1236, 155)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(spectrum_control.sizePolicy().hasHeightForWidth())
        spectrum_control.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(spectrum_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_3 = QFrame(spectrum_control)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sweep_label = QLabel(spectrum_control)
        self.sweep_label.setObjectName(u"sweep_label")

        self.horizontalLayout.addWidget(self.sweep_label)

        self.line_11 = QFrame(spectrum_control)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_11)

        self.min_label = QLabel(spectrum_control)
        self.min_label.setObjectName(u"min_label")
        self.min_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.min_label)

        self.min_spinbox = QDoubleSpinBox(spectrum_control)
        self.min_spinbox.setObjectName(u"min_spinbox")
        self.min_spinbox.setEnabled(True)
        self.min_spinbox.setMaximum(999.990000000000009)

        self.horizontalLayout.addWidget(self.min_spinbox)

        self.min_unit_label = QLabel(spectrum_control)
        self.min_unit_label.setObjectName(u"min_unit_label")

        self.horizontalLayout.addWidget(self.min_unit_label)

        self.line_4 = QFrame(spectrum_control)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.max_label = QLabel(spectrum_control)
        self.max_label.setObjectName(u"max_label")
        self.max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.max_label)

        self.max_spinbox = QDoubleSpinBox(spectrum_control)
        self.max_spinbox.setObjectName(u"max_spinbox")
        self.max_spinbox.setEnabled(True)
        self.max_spinbox.setMaximum(999.990000000000009)

        self.horizontalLayout.addWidget(self.max_spinbox)

        self.max_unit_lable = QLabel(spectrum_control)
        self.max_unit_lable.setObjectName(u"max_unit_lable")

        self.horizontalLayout.addWidget(self.max_unit_lable)

        self.line_5 = QFrame(spectrum_control)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.step_count_label = QLabel(spectrum_control)
        self.step_count_label.setObjectName(u"step_count_label")
        self.step_count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.step_count_label)

        self.step_count_spinbox = QSpinBox(spectrum_control)
        self.step_count_spinbox.setObjectName(u"step_count_spinbox")
        self.step_count_spinbox.setEnabled(True)
        self.step_count_spinbox.setMaximum(9999)

        self.horizontalLayout.addWidget(self.step_count_spinbox)

        self.line_6 = QFrame(spectrum_control)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.step_size_label = QLabel(spectrum_control)
        self.step_size_label.setObjectName(u"step_size_label")
        self.step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.step_size_label)

        self.step_size_spinbox = QDoubleSpinBox(spectrum_control)
        self.step_size_spinbox.setObjectName(u"step_size_spinbox")
        self.step_size_spinbox.setEnabled(True)
        self.step_size_spinbox.setDecimals(3)
        self.step_size_spinbox.setSingleStep(0.100000000000000)

        self.horizontalLayout.addWidget(self.step_size_spinbox)

        self.step_size_unit_label = QLabel(spectrum_control)
        self.step_size_unit_label.setObjectName(u"step_size_unit_label")

        self.horizontalLayout.addWidget(self.step_size_unit_label)

        self.line_7 = QFrame(spectrum_control)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(spectrum_control)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.repeating_checkbox = QCheckBox(spectrum_control)
        self.repeating_checkbox.setObjectName(u"repeating_checkbox")
        self.repeating_checkbox.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.repeating_checkbox)

        self.progressbar = QProgressBar(spectrum_control)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setEnabled(False)
        self.progressbar.setValue(0)

        self.horizontalLayout_2.addWidget(self.progressbar)

        self.start_button = QPushButton(spectrum_control)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.start_button)

        self.stop_button = QPushButton(spectrum_control)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(spectrum_control)

        QMetaObject.connectSlotsByName(spectrum_control)
    # setupUi

    def retranslateUi(self, spectrum_control):
        spectrum_control.setWindowTitle(QCoreApplication.translate("spectrum_control", u"Form", None))
        self.sweep_label.setText(QCoreApplication.translate("spectrum_control", u"<html><head/><body><p><span style=\" font-weight:600;\">Sweep:</span></p></body></html>", None))
        self.min_label.setText(QCoreApplication.translate("spectrum_control", u"Min:", None))
        self.min_unit_label.setText(QCoreApplication.translate("spectrum_control", u"[u]    ", None))
        self.max_label.setText(QCoreApplication.translate("spectrum_control", u"Max:", None))
        self.max_unit_lable.setText(QCoreApplication.translate("spectrum_control", u"[u]    ", None))
        self.step_count_label.setText(QCoreApplication.translate("spectrum_control", u"Step count:", None))
        self.step_size_label.setText(QCoreApplication.translate("spectrum_control", u"    Step size:", None))
        self.step_size_unit_label.setText(QCoreApplication.translate("spectrum_control", u"[u]", None))
        self.repeating_checkbox.setText(QCoreApplication.translate("spectrum_control", u"Repeating", None))
        self.start_button.setText(QCoreApplication.translate("spectrum_control", u"Start  \u25b6", None))
        self.stop_button.setText(QCoreApplication.translate("spectrum_control", u"Stop", None))
    # retranslateUi

