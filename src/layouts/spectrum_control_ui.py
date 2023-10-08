# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrum_control.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_spectrum_control(object):
    def setupUi(self, spectrum_control):
        if not spectrum_control.objectName():
            spectrum_control.setObjectName(u"spectrum_control")
        spectrum_control.resize(1210, 128)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(spectrum_control.sizePolicy().hasHeightForWidth())
        spectrum_control.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(spectrum_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_3 = QFrame(spectrum_control)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sweep_label = QLabel(spectrum_control)
        self.sweep_label.setObjectName(u"sweep_label")

        self.horizontalLayout.addWidget(self.sweep_label)

        self.line_11 = QFrame(spectrum_control)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_11)

        self.min_label = QLabel(spectrum_control)
        self.min_label.setObjectName(u"min_label")
        self.min_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.min_label)

        self.min_spinbox = QDoubleSpinBox(spectrum_control)
        self.min_spinbox.setObjectName(u"min_spinbox")

        self.horizontalLayout.addWidget(self.min_spinbox)

        self.min_unit_label = QLabel(spectrum_control)
        self.min_unit_label.setObjectName(u"min_unit_label")

        self.horizontalLayout.addWidget(self.min_unit_label)

        self.line_4 = QFrame(spectrum_control)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.max_label = QLabel(spectrum_control)
        self.max_label.setObjectName(u"max_label")
        self.max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.max_label)

        self.max_spinbox = QDoubleSpinBox(spectrum_control)
        self.max_spinbox.setObjectName(u"max_spinbox")

        self.horizontalLayout.addWidget(self.max_spinbox)

        self.max_unit_lable = QLabel(spectrum_control)
        self.max_unit_lable.setObjectName(u"max_unit_lable")

        self.horizontalLayout.addWidget(self.max_unit_lable)

        self.line_5 = QFrame(spectrum_control)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.step_count_label = QLabel(spectrum_control)
        self.step_count_label.setObjectName(u"step_count_label")
        self.step_count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.step_count_label)

        self.spinBox = QSpinBox(spectrum_control)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.line_6 = QFrame(spectrum_control)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.step_size_label = QLabel(spectrum_control)
        self.step_size_label.setObjectName(u"step_size_label")
        self.step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.step_size_label)

        self.step_size_spinbox = QDoubleSpinBox(spectrum_control)
        self.step_size_spinbox.setObjectName(u"step_size_spinbox")

        self.horizontalLayout.addWidget(self.step_size_spinbox)

        self.step_size_unit_label = QLabel(spectrum_control)
        self.step_size_unit_label.setObjectName(u"step_size_unit_label")

        self.horizontalLayout.addWidget(self.step_size_unit_label)

        self.line_7 = QFrame(spectrum_control)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(spectrum_control)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.parameters_label = QLabel(spectrum_control)
        self.parameters_label.setObjectName(u"parameters_label")

        self.horizontalLayout_3.addWidget(self.parameters_label)

        self.line_12 = QFrame(spectrum_control)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_12)

        self.a_label = QLabel(spectrum_control)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.a_label)

        self.a_spinbox = QDoubleSpinBox(spectrum_control)
        self.a_spinbox.setObjectName(u"a_spinbox")

        self.horizontalLayout_3.addWidget(self.a_spinbox)

        self.a_unit_label = QLabel(spectrum_control)
        self.a_unit_label.setObjectName(u"a_unit_label")

        self.horizontalLayout_3.addWidget(self.a_unit_label)

        self.line_8 = QFrame(spectrum_control)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_8)

        self.b_label = QLabel(spectrum_control)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.b_label)

        self.b_spinbox = QDoubleSpinBox(spectrum_control)
        self.b_spinbox.setObjectName(u"b_spinbox")

        self.horizontalLayout_3.addWidget(self.b_spinbox)

        self.b_unit_label = QLabel(spectrum_control)
        self.b_unit_label.setObjectName(u"b_unit_label")

        self.horizontalLayout_3.addWidget(self.b_unit_label)

        self.line_9 = QFrame(spectrum_control)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_9)

        self.rf_u_scale_label = QLabel(spectrum_control)
        self.rf_u_scale_label.setObjectName(u"rf_u_scale_label")
        self.rf_u_scale_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.rf_u_scale_label)

        self.rf_u_scale_spinbox = QDoubleSpinBox(spectrum_control)
        self.rf_u_scale_spinbox.setObjectName(u"rf_u_scale_spinbox")

        self.horizontalLayout_3.addWidget(self.rf_u_scale_spinbox)

        self.rf_u_scale_unit_label = QLabel(spectrum_control)
        self.rf_u_scale_unit_label.setObjectName(u"rf_u_scale_unit_label")

        self.horizontalLayout_3.addWidget(self.rf_u_scale_unit_label)

        self.line_10 = QFrame(spectrum_control)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(14, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(spectrum_control)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.repeating_checkbox = QCheckBox(spectrum_control)
        self.repeating_checkbox.setObjectName(u"repeating_checkbox")

        self.horizontalLayout_2.addWidget(self.repeating_checkbox)

        self.progressbar = QProgressBar(spectrum_control)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressbar)

        self.start_button = QPushButton(spectrum_control)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout_2.addWidget(self.start_button)

        self.stop_button = QPushButton(spectrum_control)
        self.stop_button.setObjectName(u"stop_button")

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
        self.parameters_label.setText(QCoreApplication.translate("spectrum_control", u"<html><head/><body><p><span style=\" font-weight:600;\">Parameters:</span></p></body></html>", None))
        self.a_label.setText(QCoreApplication.translate("spectrum_control", u"a:", None))
        self.a_unit_label.setText(QCoreApplication.translate("spectrum_control", u"[Vdc/Vrf]    ", None))
        self.b_label.setText(QCoreApplication.translate("spectrum_control", u"b:", None))
        self.b_unit_label.setText(QCoreApplication.translate("spectrum_control", u"[V]    ", None))
        self.rf_u_scale_label.setText(QCoreApplication.translate("spectrum_control", u"RF-to-Unit Scale:", None))
        self.rf_u_scale_unit_label.setText(QCoreApplication.translate("spectrum_control", u"[u/V]", None))
        self.repeating_checkbox.setText(QCoreApplication.translate("spectrum_control", u"Repeating", None))
        self.start_button.setText(QCoreApplication.translate("spectrum_control", u"Start  \u25b6", None))
        self.stop_button.setText(QCoreApplication.translate("spectrum_control", u"Stop", None))
    # retranslateUi

