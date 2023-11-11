# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map_control.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_map_control(object):
    def setupUi(self, map_control):
        if not map_control.objectName():
            map_control.setObjectName(u"map_control")
        map_control.resize(1304, 195)
        self.verticalLayout = QVBoxLayout(map_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_3 = QFrame(map_control)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(map_control)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_14 = QFrame(map_control)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_14)

        self.label_3 = QLabel(map_control)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.rf_min_spinbox = QDoubleSpinBox(map_control)
        self.rf_min_spinbox.setObjectName(u"rf_min_spinbox")

        self.horizontalLayout.addWidget(self.rf_min_spinbox)

        self.label_5 = QLabel(map_control)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.line_4 = QFrame(map_control)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.label_7 = QLabel(map_control)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.rf_max_spinbox = QDoubleSpinBox(map_control)
        self.rf_max_spinbox.setObjectName(u"rf_max_spinbox")

        self.horizontalLayout.addWidget(self.rf_max_spinbox)

        self.label_9 = QLabel(map_control)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.line_6 = QFrame(map_control)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.label_11 = QLabel(map_control)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_11)

        self.rf_step_count_spinbox = QSpinBox(map_control)
        self.rf_step_count_spinbox.setObjectName(u"rf_step_count_spinbox")

        self.horizontalLayout.addWidget(self.rf_step_count_spinbox)

        self.line_8 = QFrame(map_control)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_8)

        self.label_13 = QLabel(map_control)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_13)

        self.rf_step_size_spinbox = QDoubleSpinBox(map_control)
        self.rf_step_size_spinbox.setObjectName(u"rf_step_size_spinbox")

        self.horizontalLayout.addWidget(self.rf_step_size_spinbox)

        self.label_15 = QLabel(map_control)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout.addWidget(self.label_15)

        self.line_16 = QFrame(map_control)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_16)

        self.line_10 = QFrame(map_control)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_10)

        self.label_22 = QLabel(map_control)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout.addWidget(self.label_22)

        self.line_17 = QFrame(map_control)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_17)

        self.rf_u_scale_label = QLabel(map_control)
        self.rf_u_scale_label.setObjectName(u"rf_u_scale_label")
        self.rf_u_scale_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.rf_u_scale_label)

        self.rf_u_scale_spinbox = QDoubleSpinBox(map_control)
        self.rf_u_scale_spinbox.setObjectName(u"rf_u_scale_spinbox")

        self.horizontalLayout.addWidget(self.rf_u_scale_spinbox)

        self.rf_u_scale_unit_label = QLabel(map_control)
        self.rf_u_scale_unit_label.setObjectName(u"rf_u_scale_unit_label")

        self.horizontalLayout.addWidget(self.rf_u_scale_unit_label)

        self.line_15 = QFrame(map_control)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_15)

        self.label_20 = QLabel(map_control)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout.addWidget(self.label_20)

        self.mass_spinbox = QDoubleSpinBox(map_control)
        self.mass_spinbox.setObjectName(u"mass_spinbox")

        self.horizontalLayout.addWidget(self.mass_spinbox)

        self.label_25 = QLabel(map_control)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout.addWidget(self.label_25)

        self.label_24 = QLabel(map_control)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout.addWidget(self.label_24)

        self.rf_spinbox = QDoubleSpinBox(map_control)
        self.rf_spinbox.setObjectName(u"rf_spinbox")

        self.horizontalLayout.addWidget(self.rf_spinbox)

        self.label_26 = QLabel(map_control)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout.addWidget(self.label_26)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(map_control)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(map_control)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_13 = QFrame(map_control)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_13)

        self.label_4 = QLabel(map_control)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.dc_min_spinbox = QDoubleSpinBox(map_control)
        self.dc_min_spinbox.setObjectName(u"dc_min_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_min_spinbox)

        self.label_6 = QLabel(map_control)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.line_5 = QFrame(map_control)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.label_8 = QLabel(map_control)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.dc_max_spinbox = QDoubleSpinBox(map_control)
        self.dc_max_spinbox.setObjectName(u"dc_max_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_max_spinbox)

        self.label_10 = QLabel(map_control)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.line_7 = QFrame(map_control)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_7)

        self.label_12 = QLabel(map_control)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_12)

        self.dc_step_count_spinbox = QSpinBox(map_control)
        self.dc_step_count_spinbox.setObjectName(u"dc_step_count_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_step_count_spinbox)

        self.line_9 = QFrame(map_control)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_9)

        self.label_14 = QLabel(map_control)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.dc_step_size_spinbox = QDoubleSpinBox(map_control)
        self.dc_step_size_spinbox.setObjectName(u"dc_step_size_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_step_size_spinbox)

        self.label_16 = QLabel(map_control)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_2.addWidget(self.label_16)

        self.line_11 = QFrame(map_control)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_11)

        self.label_17 = QLabel(map_control)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.dc_offset_spinbox = QDoubleSpinBox(map_control)
        self.dc_offset_spinbox.setObjectName(u"dc_offset_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_offset_spinbox)

        self.label_18 = QLabel(map_control)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_2.addWidget(self.label_18)

        self.line_12 = QFrame(map_control)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_12)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(map_control)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_23 = QLabel(map_control)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_23)

        self.progessbar = QProgressBar(map_control)
        self.progessbar.setObjectName(u"progessbar")
        self.progessbar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progessbar)

        self.steps_label = QLabel(map_control)
        self.steps_label.setObjectName(u"steps_label")

        self.horizontalLayout_3.addWidget(self.steps_label)

        self.label_19 = QLabel(map_control)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_19)

        self.time_left_label = QLabel(map_control)
        self.time_left_label.setObjectName(u"time_left_label")

        self.horizontalLayout_3.addWidget(self.time_left_label)

        self.label_21 = QLabel(map_control)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.full_time_label = QLabel(map_control)
        self.full_time_label.setObjectName(u"full_time_label")

        self.horizontalLayout_3.addWidget(self.full_time_label)

        self.start_push_button = QPushButton(map_control)
        self.start_push_button.setObjectName(u"start_push_button")

        self.horizontalLayout_3.addWidget(self.start_push_button)

        self.stop_push_button = QPushButton(map_control)
        self.stop_push_button.setObjectName(u"stop_push_button")

        self.horizontalLayout_3.addWidget(self.stop_push_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_18 = QFrame(map_control)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_18)

        self.line_20 = QFrame(map_control)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_20)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.parameters_label = QLabel(map_control)
        self.parameters_label.setObjectName(u"parameters_label")

        self.horizontalLayout_31.addWidget(self.parameters_label)

        self.line_121 = QFrame(map_control)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setFrameShape(QFrame.VLine)
        self.line_121.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_31.addWidget(self.line_121)

        self.a_label = QLabel(map_control)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.a_label)

        self.a_spinbox = QDoubleSpinBox(map_control)
        self.a_spinbox.setObjectName(u"a_spinbox")

        self.horizontalLayout_31.addWidget(self.a_spinbox)

        self.a_unit_label = QLabel(map_control)
        self.a_unit_label.setObjectName(u"a_unit_label")

        self.horizontalLayout_31.addWidget(self.a_unit_label)

        self.b_label = QLabel(map_control)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.b_label)

        self.b_spinbox = QDoubleSpinBox(map_control)
        self.b_spinbox.setObjectName(u"b_spinbox")

        self.horizontalLayout_31.addWidget(self.b_spinbox)

        self.b_unit_label = QLabel(map_control)
        self.b_unit_label.setObjectName(u"b_unit_label")

        self.horizontalLayout_31.addWidget(self.b_unit_label)

        self.line_91 = QFrame(map_control)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setFrameShape(QFrame.VLine)
        self.line_91.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_31.addWidget(self.line_91)

        self.label1 = QLabel(map_control)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label1)

        self.x1_spinbox = QDoubleSpinBox(map_control)
        self.x1_spinbox.setObjectName(u"x1_spinbox")

        self.horizontalLayout_31.addWidget(self.x1_spinbox)

        self.label_51 = QLabel(map_control)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_31.addWidget(self.label_51)

        self.label_27 = QLabel(map_control)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_27)

        self.y1_spinbox = QDoubleSpinBox(map_control)
        self.y1_spinbox.setObjectName(u"y1_spinbox")

        self.horizontalLayout_31.addWidget(self.y1_spinbox)

        self.label_61 = QLabel(map_control)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_31.addWidget(self.label_61)

        self.label_31 = QLabel(map_control)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_31)

        self.x2_spinbox = QDoubleSpinBox(map_control)
        self.x2_spinbox.setObjectName(u"x2_spinbox")

        self.horizontalLayout_31.addWidget(self.x2_spinbox)

        self.label_71 = QLabel(map_control)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_31.addWidget(self.label_71)

        self.label_41 = QLabel(map_control)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_41)

        self.y2_spinbox = QDoubleSpinBox(map_control)
        self.y2_spinbox.setObjectName(u"y2_spinbox")

        self.horizontalLayout_31.addWidget(self.y2_spinbox)

        self.label_81 = QLabel(map_control)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_31.addWidget(self.label_81)

        self.line_81 = QFrame(map_control)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setFrameShape(QFrame.VLine)
        self.line_81.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_31.addWidget(self.line_81)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_21)

        self.horizontalLayout_31.setStretch(22, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_31)

        self.line_19 = QFrame(map_control)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_19)


        self.retranslateUi(map_control)

        QMetaObject.connectSlotsByName(map_control)
    # setupUi

    def retranslateUi(self, map_control):
        map_control.setWindowTitle(QCoreApplication.translate("map_control", u"Form", None))
        self.label.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">RF:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("map_control", u"Min:", None))
        self.label_5.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_7.setText(QCoreApplication.translate("map_control", u"Max:", None))
        self.label_9.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_11.setText(QCoreApplication.translate("map_control", u"Step count:", None))
        self.label_13.setText(QCoreApplication.translate("map_control", u"Step size:", None))
        self.label_15.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_22.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">Scale:</span></p></body></html>", None))
        self.rf_u_scale_label.setText(QCoreApplication.translate("map_control", u"RF-to-Unit Scale:", None))
        self.rf_u_scale_unit_label.setText(QCoreApplication.translate("map_control", u"[u/V]", None))
        self.label_20.setText(QCoreApplication.translate("map_control", u"Mass:", None))
        self.label_25.setText(QCoreApplication.translate("map_control", u"[u]", None))
        self.label_24.setText(QCoreApplication.translate("map_control", u"RF:", None))
        self.label_26.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_2.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">DC:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("map_control", u"Min:", None))
        self.label_6.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_8.setText(QCoreApplication.translate("map_control", u"Max:", None))
        self.label_10.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_12.setText(QCoreApplication.translate("map_control", u"Step count:", None))
        self.label_14.setText(QCoreApplication.translate("map_control", u"Step size:", None))
        self.label_16.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.label_17.setText(QCoreApplication.translate("map_control", u"Offset proportional to RF:", None))
        self.label_18.setText(QCoreApplication.translate("map_control", u"[Vdc/Vrf]", None))
        self.label_23.setText(QCoreApplication.translate("map_control", u"Steps:", None))
        self.steps_label.setText(QCoreApplication.translate("map_control", u"0/0", None))
        self.label_19.setText(QCoreApplication.translate("map_control", u"Time left:", None))
        self.time_left_label.setText(QCoreApplication.translate("map_control", u"00:00:00", None))
        self.label_21.setText(QCoreApplication.translate("map_control", u"Full time:", None))
        self.full_time_label.setText(QCoreApplication.translate("map_control", u"00:00:00", None))
        self.start_push_button.setText(QCoreApplication.translate("map_control", u"Start", None))
        self.stop_push_button.setText(QCoreApplication.translate("map_control", u"Stop", None))
        self.parameters_label.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">Scanline:</span></p></body></html>", None))
        self.a_label.setText(QCoreApplication.translate("map_control", u"a:", None))
        self.a_unit_label.setText(QCoreApplication.translate("map_control", u"[Vdc/Vrf]    ", None))
        self.b_label.setText(QCoreApplication.translate("map_control", u"b:", None))
        self.b_unit_label.setText(QCoreApplication.translate("map_control", u"[V]    ", None))
        self.label1.setText(QCoreApplication.translate("map_control", u"X1:", None))
        self.label_51.setText(QCoreApplication.translate("map_control", u"[Vrf]", None))
        self.label_27.setText(QCoreApplication.translate("map_control", u"Y1:", None))
        self.label_61.setText(QCoreApplication.translate("map_control", u"[Vdc]", None))
        self.label_31.setText(QCoreApplication.translate("map_control", u"X2:", None))
        self.label_71.setText(QCoreApplication.translate("map_control", u"[Vrf]", None))
        self.label_41.setText(QCoreApplication.translate("map_control", u"Y2:", None))
        self.label_81.setText(QCoreApplication.translate("map_control", u"[Vdc]", None))
    # retranslateUi

