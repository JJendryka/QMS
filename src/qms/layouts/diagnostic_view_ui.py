# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagnostic_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_diagnostic_view(object):
    def setupUi(self, diagnostic_view):
        if not diagnostic_view.objectName():
            diagnostic_view.setObjectName(u"diagnostic_view")
        diagnostic_view.resize(1660, 784)
        self.horizontalLayout = QHBoxLayout(diagnostic_view)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(diagnostic_view)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.resonance_chart = QWidget(diagnostic_view)
        self.resonance_chart.setObjectName(u"resonance_chart")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resonance_chart.sizePolicy().hasHeightForWidth())
        self.resonance_chart.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.resonance_chart)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_5 = QLabel(diagnostic_view)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.min_frequency_spinbox = QDoubleSpinBox(diagnostic_view)
        self.min_frequency_spinbox.setObjectName(u"min_frequency_spinbox")
        self.min_frequency_spinbox.setMinimum(1.000000000000000)
        self.min_frequency_spinbox.setMaximum(15.000000000000000)

        self.horizontalLayout_2.addWidget(self.min_frequency_spinbox)

        self.label_6 = QLabel(diagnostic_view)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.line = QFrame(diagnostic_view)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_4 = QLabel(diagnostic_view)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.max_frequency_spinbox = QDoubleSpinBox(diagnostic_view)
        self.max_frequency_spinbox.setObjectName(u"max_frequency_spinbox")
        self.max_frequency_spinbox.setMinimum(1.000000000000000)
        self.max_frequency_spinbox.setMaximum(15.000000000000000)
        self.max_frequency_spinbox.setValue(15.000000000000000)

        self.horizontalLayout_2.addWidget(self.max_frequency_spinbox)

        self.label_8 = QLabel(diagnostic_view)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.frequency_steps_spinbox = QSpinBox(diagnostic_view)
        self.frequency_steps_spinbox.setObjectName(u"frequency_steps_spinbox")
        self.frequency_steps_spinbox.setMinimum(1)
        self.frequency_steps_spinbox.setMaximum(1000)
        self.frequency_steps_spinbox.setValue(281)

        self.horizontalLayout_2.addWidget(self.frequency_steps_spinbox)

        self.label_7 = QLabel(diagnostic_view)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.line_11 = QFrame(diagnostic_view)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_11)

        self.label_14 = QLabel(diagnostic_view)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.frequency_step_size_label = QLabel(diagnostic_view)
        self.frequency_step_size_label.setObjectName(u"frequency_step_size_label")
        self.frequency_step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.frequency_step_size_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.resonance_scan_button = QPushButton(diagnostic_view)
        self.resonance_scan_button.setObjectName(u"resonance_scan_button")

        self.verticalLayout_2.addWidget(self.resonance_scan_button)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.line_8 = QFrame(diagnostic_view)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_8)

        self.label_12 = QLabel(diagnostic_view)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.working_frequency_spinbox = QDoubleSpinBox(diagnostic_view)
        self.working_frequency_spinbox.setObjectName(u"working_frequency_spinbox")

        self.horizontalLayout_5.addWidget(self.working_frequency_spinbox)

        self.label_13 = QLabel(diagnostic_view)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.line_7 = QFrame(diagnostic_view)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line_14 = QFrame(diagnostic_view)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_14)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(diagnostic_view)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(diagnostic_view)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.rf_chart = QWidget(diagnostic_view)
        self.rf_chart.setObjectName(u"rf_chart")

        self.verticalLayout.addWidget(self.rf_chart)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.line_21 = QFrame(diagnostic_view)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_21)

        self.label_9 = QLabel(diagnostic_view)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.rf_max_spinbox = QDoubleSpinBox(diagnostic_view)
        self.rf_max_spinbox.setObjectName(u"rf_max_spinbox")
        self.rf_max_spinbox.setMaximum(6.000000000000000)
        self.rf_max_spinbox.setValue(4.000000000000000)

        self.horizontalLayout_4.addWidget(self.rf_max_spinbox)

        self.label_11 = QLabel(diagnostic_view)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.line_22 = QFrame(diagnostic_view)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_22)

        self.label_10 = QLabel(diagnostic_view)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.rf_step_count_spinbox = QSpinBox(diagnostic_view)
        self.rf_step_count_spinbox.setObjectName(u"rf_step_count_spinbox")
        self.rf_step_count_spinbox.setMaximum(1000)
        self.rf_step_count_spinbox.setValue(81)

        self.horizontalLayout_4.addWidget(self.rf_step_count_spinbox)

        self.line_23 = QFrame(diagnostic_view)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.VLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_23)

        self.label_29 = QLabel(diagnostic_view)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_29)

        self.rf_step_size_label = QLabel(diagnostic_view)
        self.rf_step_size_label.setObjectName(u"rf_step_size_label")
        self.rf_step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.rf_step_size_label)

        self.line_24 = QFrame(diagnostic_view)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.VLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_24)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.rf_scan_button = QPushButton(diagnostic_view)
        self.rf_scan_button.setObjectName(u"rf_scan_button")

        self.verticalLayout.addWidget(self.rf_scan_button)

        self.line_5 = QFrame(diagnostic_view)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.label_24 = QLabel(diagnostic_view)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_24)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.line_16 = QFrame(diagnostic_view)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_16)

        self.use_pid_checkbox = QCheckBox(diagnostic_view)
        self.use_pid_checkbox.setObjectName(u"use_pid_checkbox")

        self.horizontalLayout_13.addWidget(self.use_pid_checkbox)

        self.line_12 = QFrame(diagnostic_view)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_12)

        self.label_25 = QLabel(diagnostic_view)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.pid_p_spinbox = QDoubleSpinBox(diagnostic_view)
        self.pid_p_spinbox.setObjectName(u"pid_p_spinbox")

        self.horizontalLayout_13.addWidget(self.pid_p_spinbox)

        self.line_9 = QFrame(diagnostic_view)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_9)

        self.pid_i_label = QLabel(diagnostic_view)
        self.pid_i_label.setObjectName(u"pid_i_label")
        self.pid_i_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.pid_i_label)

        self.pid_i_spinbox = QDoubleSpinBox(diagnostic_view)
        self.pid_i_spinbox.setObjectName(u"pid_i_spinbox")

        self.horizontalLayout_13.addWidget(self.pid_i_spinbox)

        self.line_10 = QFrame(diagnostic_view)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_10)

        self.pid_d_label = QLabel(diagnostic_view)
        self.pid_d_label.setObjectName(u"pid_d_label")
        self.pid_d_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.pid_d_label)

        self.pid_d_spinbox = QDoubleSpinBox(diagnostic_view)
        self.pid_d_spinbox.setObjectName(u"pid_d_spinbox")

        self.horizontalLayout_13.addWidget(self.pid_d_spinbox)

        self.line_17 = QFrame(diagnostic_view)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_17)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.line_6 = QFrame(diagnostic_view)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.label_32 = QLabel(diagnostic_view)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_32)

        self.rf_stability_chart = QWidget(diagnostic_view)
        self.rf_stability_chart.setObjectName(u"rf_stability_chart")

        self.verticalLayout.addWidget(self.rf_stability_chart)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.line_18 = QFrame(diagnostic_view)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_18)

        self.line_19 = QFrame(diagnostic_view)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_19)

        self.label_33 = QLabel(diagnostic_view)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_33)

        self.rf_setpoint_spinbox = QDoubleSpinBox(diagnostic_view)
        self.rf_setpoint_spinbox.setObjectName(u"rf_setpoint_spinbox")

        self.horizontalLayout_10.addWidget(self.rf_setpoint_spinbox)

        self.label_34 = QLabel(diagnostic_view)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_10.addWidget(self.label_34)

        self.line_20 = QFrame(diagnostic_view)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_20)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.rf_test_button = QPushButton(diagnostic_view)
        self.rf_test_button.setObjectName(u"rf_test_button")

        self.verticalLayout.addWidget(self.rf_test_button)

        self.line_15 = QFrame(diagnostic_view)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_15)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_3 = QFrame(diagnostic_view)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(diagnostic_view)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.source_chart = QWidget(diagnostic_view)
        self.source_chart.setObjectName(u"source_chart")

        self.verticalLayout_3.addWidget(self.source_chart)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_15)

        self.label_17 = QLabel(diagnostic_view)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.source_min_spinbox = QDoubleSpinBox(diagnostic_view)
        self.source_min_spinbox.setObjectName(u"source_min_spinbox")
        self.source_min_spinbox.setMinimum(0.000000000000000)
        self.source_min_spinbox.setMaximum(2.000000000000000)
        self.source_min_spinbox.setSingleStep(0.100000000000000)

        self.horizontalLayout_7.addWidget(self.source_min_spinbox)

        self.label_18 = QLabel(diagnostic_view)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_7.addWidget(self.label_18)

        self.line_13 = QFrame(diagnostic_view)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_13)

        self.label_16 = QLabel(diagnostic_view)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.source_max_spinbox = QDoubleSpinBox(diagnostic_view)
        self.source_max_spinbox.setObjectName(u"source_max_spinbox")
        self.source_max_spinbox.setMaximum(2.000000000000000)
        self.source_max_spinbox.setSingleStep(0.100000000000000)
        self.source_max_spinbox.setValue(2.000000000000000)

        self.horizontalLayout_7.addWidget(self.source_max_spinbox)

        self.label_19 = QLabel(diagnostic_view)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_7.addWidget(self.label_19)

        self.line_25 = QFrame(diagnostic_view)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.VLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_25)

        self.label_20 = QLabel(diagnostic_view)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_20)

        self.source_steps_spinbox = QSpinBox(diagnostic_view)
        self.source_steps_spinbox.setObjectName(u"source_steps_spinbox")
        self.source_steps_spinbox.setMaximum(1000)
        self.source_steps_spinbox.setValue(41)

        self.horizontalLayout_7.addWidget(self.source_steps_spinbox)

        self.label_15 = QLabel(diagnostic_view)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.source_step_size_label = QLabel(diagnostic_view)
        self.source_step_size_label.setObjectName(u"source_step_size_label")

        self.horizontalLayout_7.addWidget(self.source_step_size_label)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.source_scan_button = QPushButton(diagnostic_view)
        self.source_scan_button.setObjectName(u"source_scan_button")

        self.verticalLayout_3.addWidget(self.source_scan_button)

        self.line_4 = QFrame(diagnostic_view)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.label_23 = QLabel(diagnostic_view)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_23)

        self.source_stability_chart = QWidget(diagnostic_view)
        self.source_stability_chart.setObjectName(u"source_stability_chart")

        self.verticalLayout_3.addWidget(self.source_stability_chart)

        self.source_test_button = QPushButton(diagnostic_view)
        self.source_test_button.setObjectName(u"source_test_button")

        self.verticalLayout_3.addWidget(self.source_test_button)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cv_radiobutton = QRadioButton(diagnostic_view)
        self.source_buttongroup = QButtonGroup(diagnostic_view)
        self.source_buttongroup.setObjectName(u"source_buttongroup")
        self.source_buttongroup.addButton(self.cv_radiobutton)
        self.cv_radiobutton.setObjectName(u"cv_radiobutton")
        self.cv_radiobutton.setChecked(True)

        self.horizontalLayout_9.addWidget(self.cv_radiobutton)

        self.source_voltage_spinbox = QDoubleSpinBox(diagnostic_view)
        self.source_voltage_spinbox.setObjectName(u"source_voltage_spinbox")

        self.horizontalLayout_9.addWidget(self.source_voltage_spinbox)

        self.label_21 = QLabel(diagnostic_view)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_9.addWidget(self.label_21)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cc_radiobutton = QRadioButton(diagnostic_view)
        self.source_buttongroup.addButton(self.cc_radiobutton)
        self.cc_radiobutton.setObjectName(u"cc_radiobutton")
        self.cc_radiobutton.setEnabled(True)
        self.cc_radiobutton.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.cc_radiobutton)

        self.source_current_spinbox = QDoubleSpinBox(diagnostic_view)
        self.source_current_spinbox.setObjectName(u"source_current_spinbox")

        self.horizontalLayout_11.addWidget(self.source_current_spinbox)

        self.label_22 = QLabel(diagnostic_view)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_11.addWidget(self.label_22)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.line_26 = QFrame(diagnostic_view)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_26)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.retranslateUi(diagnostic_view)

        QMetaObject.connectSlotsByName(diagnostic_view)
    # setupUi

    def retranslateUi(self, diagnostic_view):
        diagnostic_view.setWindowTitle(QCoreApplication.translate("diagnostic_view", u"Form", None))
        self.label.setText(QCoreApplication.translate("diagnostic_view", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Resonance</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("diagnostic_view", u"Min:", None))
        self.label_6.setText(QCoreApplication.translate("diagnostic_view", u"[MHz]", None))
        self.label_4.setText(QCoreApplication.translate("diagnostic_view", u"Max:", None))
        self.label_8.setText(QCoreApplication.translate("diagnostic_view", u"Step count:", None))
        self.label_7.setText(QCoreApplication.translate("diagnostic_view", u"[MHz]", None))
        self.label_14.setText(QCoreApplication.translate("diagnostic_view", u"Step size:", None))
        self.frequency_step_size_label.setText(QCoreApplication.translate("diagnostic_view", u"0.05 MHz", None))
        self.resonance_scan_button.setText(QCoreApplication.translate("diagnostic_view", u"Scan", None))
        self.label_12.setText(QCoreApplication.translate("diagnostic_view", u"Working frequency:", None))
        self.label_13.setText(QCoreApplication.translate("diagnostic_view", u"[MHz]", None))
        self.label_2.setText(QCoreApplication.translate("diagnostic_view", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">RF Input-Output</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("diagnostic_view", u"Max:", None))
        self.label_11.setText(QCoreApplication.translate("diagnostic_view", u"[Vpp]", None))
        self.label_10.setText(QCoreApplication.translate("diagnostic_view", u"Step count:", None))
        self.label_29.setText(QCoreApplication.translate("diagnostic_view", u"Step size:", None))
        self.rf_step_size_label.setText(QCoreApplication.translate("diagnostic_view", u"0.050 V", None))
        self.rf_scan_button.setText(QCoreApplication.translate("diagnostic_view", u"Scan", None))
        self.label_24.setText(QCoreApplication.translate("diagnostic_view", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">PID Setup</span></p></body></html>", None))
        self.use_pid_checkbox.setText(QCoreApplication.translate("diagnostic_view", u"Use PID", None))
        self.label_25.setText(QCoreApplication.translate("diagnostic_view", u"P:", None))
        self.pid_i_label.setText(QCoreApplication.translate("diagnostic_view", u"I:", None))
        self.pid_d_label.setText(QCoreApplication.translate("diagnostic_view", u"D:", None))
        self.label_32.setText(QCoreApplication.translate("diagnostic_view", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">RF Stability</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("diagnostic_view", u"Setpoint:", None))
        self.label_34.setText(QCoreApplication.translate("diagnostic_view", u"[Vpp]", None))
        self.rf_test_button.setText(QCoreApplication.translate("diagnostic_view", u"Test", None))
        self.label_3.setText(QCoreApplication.translate("diagnostic_view", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source V-I</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("diagnostic_view", u"Min:", None))
        self.label_18.setText(QCoreApplication.translate("diagnostic_view", u"[kV]", None))
        self.label_16.setText(QCoreApplication.translate("diagnostic_view", u"Max:", None))
        self.label_19.setText(QCoreApplication.translate("diagnostic_view", u"[kV]", None))
        self.label_20.setText(QCoreApplication.translate("diagnostic_view", u"Step count:", None))
        self.label_15.setText(QCoreApplication.translate("diagnostic_view", u"Step size:", None))
        self.source_step_size_label.setText(QCoreApplication.translate("diagnostic_view", u"50 V", None))
        self.source_scan_button.setText(QCoreApplication.translate("diagnostic_view", u"Scan", None))
        self.label_23.setText(QCoreApplication.translate("diagnostic_view", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source Stability</span></p></body></html>", None))
        self.source_test_button.setText(QCoreApplication.translate("diagnostic_view", u"Test", None))
        self.cv_radiobutton.setText(QCoreApplication.translate("diagnostic_view", u"Constant Voltage", None))
        self.label_21.setText(QCoreApplication.translate("diagnostic_view", u"[kV]", None))
        self.cc_radiobutton.setText(QCoreApplication.translate("diagnostic_view", u"Constant Current", None))
        self.label_22.setText(QCoreApplication.translate("diagnostic_view", u"[mA]", None))
    # retranslateUi

