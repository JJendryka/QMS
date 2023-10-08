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
        map_control.resize(1182, 155)
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

        self.line_10 = QFrame(map_control)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_10)

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
        self.progessbar = QProgressBar(map_control)
        self.progessbar.setObjectName(u"progessbar")
        self.progessbar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progessbar)

        self.label_23 = QLabel(map_control)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_23)

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
    # retranslateUi

