# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagnostic_view.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_DiagnosticView(object):
    def setupUi(self, DiagnosticView):
        if not DiagnosticView.objectName():
            DiagnosticView.setObjectName(u"DiagnosticView")
        DiagnosticView.resize(1173, 784)
        self.horizontalLayout = QHBoxLayout(DiagnosticView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(DiagnosticView)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.resonance_chart = QWidget(DiagnosticView)
        self.resonance_chart.setObjectName(u"resonance_chart")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resonance_chart.sizePolicy().hasHeightForWidth())
        self.resonance_chart.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.resonance_chart)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(DiagnosticView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.min_frequency_lineedit = QLineEdit(DiagnosticView)
        self.min_frequency_lineedit.setObjectName(u"min_frequency_lineedit")

        self.horizontalLayout_2.addWidget(self.min_frequency_lineedit)

        self.label_6 = QLabel(DiagnosticView)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.line = QFrame(DiagnosticView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_4 = QLabel(DiagnosticView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.max_frequency_lineedit = QLineEdit(DiagnosticView)
        self.max_frequency_lineedit.setObjectName(u"max_frequency_lineedit")

        self.horizontalLayout_2.addWidget(self.max_frequency_lineedit)

        self.label_7 = QLabel(DiagnosticView)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(DiagnosticView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.frequency_steps_spinbox = QSpinBox(DiagnosticView)
        self.frequency_steps_spinbox.setObjectName(u"frequency_steps_spinbox")

        self.horizontalLayout_3.addWidget(self.frequency_steps_spinbox)

        self.label_14 = QLabel(DiagnosticView)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.frequency_step_size_label = QLabel(DiagnosticView)
        self.frequency_step_size_label.setObjectName(u"frequency_step_size_label")
        self.frequency_step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.frequency_step_size_label)

        self.label_28 = QLabel(DiagnosticView)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_3.addWidget(self.label_28)

        self.resonance_scan_button = QPushButton(DiagnosticView)
        self.resonance_scan_button.setObjectName(u"resonance_scan_button")

        self.horizontalLayout_3.addWidget(self.resonance_scan_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(DiagnosticView)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.working_frequency_lineedit = QLineEdit(DiagnosticView)
        self.working_frequency_lineedit.setObjectName(u"working_frequency_lineedit")

        self.horizontalLayout_5.addWidget(self.working_frequency_lineedit)

        self.label_13 = QLabel(DiagnosticView)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(DiagnosticView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DiagnosticView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.rf_chart = QWidget(DiagnosticView)
        self.rf_chart.setObjectName(u"rf_chart")

        self.verticalLayout.addWidget(self.rf_chart)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(DiagnosticView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.rf_max_spinbox = QDoubleSpinBox(DiagnosticView)
        self.rf_max_spinbox.setObjectName(u"rf_max_spinbox")

        self.horizontalLayout_4.addWidget(self.rf_max_spinbox)

        self.label_11 = QLabel(DiagnosticView)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(DiagnosticView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.rf_step_count_spinbox = QSpinBox(DiagnosticView)
        self.rf_step_count_spinbox.setObjectName(u"rf_step_count_spinbox")

        self.horizontalLayout_6.addWidget(self.rf_step_count_spinbox)

        self.label_29 = QLabel(DiagnosticView)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_29)

        self.rf_step_size_label = QLabel(DiagnosticView)
        self.rf_step_size_label.setObjectName(u"rf_step_size_label")
        self.rf_step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.rf_step_size_label)

        self.label_31 = QLabel(DiagnosticView)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_6.addWidget(self.label_31)

        self.rf_scan_button = QPushButton(DiagnosticView)
        self.rf_scan_button.setObjectName(u"rf_scan_button")

        self.horizontalLayout_6.addWidget(self.rf_scan_button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.line_5 = QFrame(DiagnosticView)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.label_24 = QLabel(DiagnosticView)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_24)

        self.use_pid_checkbox = QCheckBox(DiagnosticView)
        self.use_pid_checkbox.setObjectName(u"use_pid_checkbox")

        self.verticalLayout.addWidget(self.use_pid_checkbox)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_25 = QLabel(DiagnosticView)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.pid_p_spinbox = QDoubleSpinBox(DiagnosticView)
        self.pid_p_spinbox.setObjectName(u"pid_p_spinbox")

        self.horizontalLayout_13.addWidget(self.pid_p_spinbox)

        self.pid_i_spinbox = QLabel(DiagnosticView)
        self.pid_i_spinbox.setObjectName(u"pid_i_spinbox")
        self.pid_i_spinbox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.pid_i_spinbox)

        self.doubleSpinBox_2 = QDoubleSpinBox(DiagnosticView)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_2)

        self.pid_d_spinbox = QLabel(DiagnosticView)
        self.pid_d_spinbox.setObjectName(u"pid_d_spinbox")
        self.pid_d_spinbox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.pid_d_spinbox)

        self.doubleSpinBox_3 = QDoubleSpinBox(DiagnosticView)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.line_6 = QFrame(DiagnosticView)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.label_32 = QLabel(DiagnosticView)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_32)

        self.rf_stability_chart = QWidget(DiagnosticView)
        self.rf_stability_chart.setObjectName(u"rf_stability_chart")

        self.verticalLayout.addWidget(self.rf_stability_chart)

        self.rf_enable_checkbox = QCheckBox(DiagnosticView)
        self.rf_enable_checkbox.setObjectName(u"rf_enable_checkbox")

        self.verticalLayout.addWidget(self.rf_enable_checkbox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_33 = QLabel(DiagnosticView)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_33)

        self.rf_setpoint_spinbox = QDoubleSpinBox(DiagnosticView)
        self.rf_setpoint_spinbox.setObjectName(u"rf_setpoint_spinbox")

        self.horizontalLayout_10.addWidget(self.rf_setpoint_spinbox)

        self.label_34 = QLabel(DiagnosticView)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_10.addWidget(self.label_34)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_3 = QFrame(DiagnosticView)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(DiagnosticView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.source_chart = QWidget(DiagnosticView)
        self.source_chart.setObjectName(u"source_chart")

        self.verticalLayout_3.addWidget(self.source_chart)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(DiagnosticView)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.source_min_spinbox = QDoubleSpinBox(DiagnosticView)
        self.source_min_spinbox.setObjectName(u"source_min_spinbox")

        self.horizontalLayout_7.addWidget(self.source_min_spinbox)

        self.label_18 = QLabel(DiagnosticView)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_7.addWidget(self.label_18)

        self.label_16 = QLabel(DiagnosticView)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.source_max_spinbox = QDoubleSpinBox(DiagnosticView)
        self.source_max_spinbox.setObjectName(u"source_max_spinbox")

        self.horizontalLayout_7.addWidget(self.source_max_spinbox)

        self.label_19 = QLabel(DiagnosticView)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_7.addWidget(self.label_19)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(DiagnosticView)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_20)

        self.source_steps_spinbox = QSpinBox(DiagnosticView)
        self.source_steps_spinbox.setObjectName(u"source_steps_spinbox")

        self.horizontalLayout_8.addWidget(self.source_steps_spinbox)

        self.pushButton_3 = QPushButton(DiagnosticView)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton = QRadioButton(DiagnosticView)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_9.addWidget(self.radioButton)

        self.source_voltage_spinbox = QDoubleSpinBox(DiagnosticView)
        self.source_voltage_spinbox.setObjectName(u"source_voltage_spinbox")

        self.horizontalLayout_9.addWidget(self.source_voltage_spinbox)

        self.label_21 = QLabel(DiagnosticView)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_9.addWidget(self.label_21)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_2 = QRadioButton(DiagnosticView)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.radioButton_2)

        self.source_current_spinbox = QDoubleSpinBox(DiagnosticView)
        self.source_current_spinbox.setObjectName(u"source_current_spinbox")

        self.horizontalLayout_11.addWidget(self.source_current_spinbox)

        self.label_22 = QLabel(DiagnosticView)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_11.addWidget(self.label_22)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.line_4 = QFrame(DiagnosticView)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.label_23 = QLabel(DiagnosticView)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_23)

        self.source_stability_chart = QWidget(DiagnosticView)
        self.source_stability_chart.setObjectName(u"source_stability_chart")

        self.verticalLayout_3.addWidget(self.source_stability_chart)

        self.source_enable_checkbox = QCheckBox(DiagnosticView)
        self.source_enable_checkbox.setObjectName(u"source_enable_checkbox")

        self.verticalLayout_3.addWidget(self.source_enable_checkbox)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.retranslateUi(DiagnosticView)

        QMetaObject.connectSlotsByName(DiagnosticView)
    # setupUi

    def retranslateUi(self, DiagnosticView):
        DiagnosticView.setWindowTitle(QCoreApplication.translate("DiagnosticView", u"Form", None))
        self.label.setText(QCoreApplication.translate("DiagnosticView", u"Resonance", None))
        self.label_5.setText(QCoreApplication.translate("DiagnosticView", u"Min:", None))
        self.label_6.setText(QCoreApplication.translate("DiagnosticView", u"[MHz]", None))
        self.label_4.setText(QCoreApplication.translate("DiagnosticView", u"Max:", None))
        self.label_7.setText(QCoreApplication.translate("DiagnosticView", u"[MHz]", None))
        self.label_8.setText(QCoreApplication.translate("DiagnosticView", u"Step count:", None))
        self.label_14.setText(QCoreApplication.translate("DiagnosticView", u"Step size:", None))
        self.frequency_step_size_label.setText(QCoreApplication.translate("DiagnosticView", u"-", None))
        self.label_28.setText(QCoreApplication.translate("DiagnosticView", u"MHz", None))
        self.resonance_scan_button.setText(QCoreApplication.translate("DiagnosticView", u"Scan", None))
        self.label_12.setText(QCoreApplication.translate("DiagnosticView", u"Working frequency:", None))
        self.label_13.setText(QCoreApplication.translate("DiagnosticView", u"[MHz]", None))
        self.label_2.setText(QCoreApplication.translate("DiagnosticView", u"RF Input-Output", None))
        self.label_9.setText(QCoreApplication.translate("DiagnosticView", u"Max:", None))
        self.label_11.setText(QCoreApplication.translate("DiagnosticView", u"[Vpp]", None))
        self.label_10.setText(QCoreApplication.translate("DiagnosticView", u"Step count:", None))
        self.label_29.setText(QCoreApplication.translate("DiagnosticView", u"Step size:", None))
        self.rf_step_size_label.setText(QCoreApplication.translate("DiagnosticView", u"-", None))
        self.label_31.setText(QCoreApplication.translate("DiagnosticView", u"Vpp", None))
        self.rf_scan_button.setText(QCoreApplication.translate("DiagnosticView", u"Scan", None))
        self.label_24.setText(QCoreApplication.translate("DiagnosticView", u"PID Setup", None))
        self.use_pid_checkbox.setText(QCoreApplication.translate("DiagnosticView", u"Use PID", None))
        self.label_25.setText(QCoreApplication.translate("DiagnosticView", u"P:", None))
        self.pid_i_spinbox.setText(QCoreApplication.translate("DiagnosticView", u"I:", None))
        self.pid_d_spinbox.setText(QCoreApplication.translate("DiagnosticView", u"D:", None))
        self.label_32.setText(QCoreApplication.translate("DiagnosticView", u"RF Stability", None))
        self.rf_enable_checkbox.setText(QCoreApplication.translate("DiagnosticView", u"Test enable RF", None))
        self.label_33.setText(QCoreApplication.translate("DiagnosticView", u"Setpoint:", None))
        self.label_34.setText(QCoreApplication.translate("DiagnosticView", u"[Vpp]", None))
        self.label_3.setText(QCoreApplication.translate("DiagnosticView", u"Source V-I", None))
        self.label_17.setText(QCoreApplication.translate("DiagnosticView", u"Min:", None))
        self.label_18.setText(QCoreApplication.translate("DiagnosticView", u"[V]", None))
        self.label_16.setText(QCoreApplication.translate("DiagnosticView", u"Max:", None))
        self.label_19.setText(QCoreApplication.translate("DiagnosticView", u"[V]", None))
        self.label_20.setText(QCoreApplication.translate("DiagnosticView", u"Steps:", None))
        self.pushButton_3.setText(QCoreApplication.translate("DiagnosticView", u"Scan", None))
        self.radioButton.setText(QCoreApplication.translate("DiagnosticView", u"Constant Voltage", None))
        self.label_21.setText(QCoreApplication.translate("DiagnosticView", u"[V]", None))
        self.radioButton_2.setText(QCoreApplication.translate("DiagnosticView", u"Constant Current", None))
        self.label_22.setText(QCoreApplication.translate("DiagnosticView", u"[mA]", None))
        self.label_23.setText(QCoreApplication.translate("DiagnosticView", u"Source Stability", None))
        self.source_enable_checkbox.setText(QCoreApplication.translate("DiagnosticView", u"Test enable source", None))
    # retranslateUi

