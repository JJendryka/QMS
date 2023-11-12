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
        map_control.resize(1304, 222)
        self.verticalLayout = QVBoxLayout(map_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_121 = QFrame(map_control)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setFrameShape(QFrame.HLine)
        self.line_121.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_121)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rf_label = QLabel(map_control)
        self.rf_label.setObjectName(u"rf_label")

        self.horizontalLayout.addWidget(self.rf_label)

        self.line_100 = QFrame(map_control)
        self.line_100.setObjectName(u"line_100")
        self.line_100.setFrameShape(QFrame.VLine)
        self.line_100.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_100)

        self.rf_min_label = QLabel(map_control)
        self.rf_min_label.setObjectName(u"rf_min_label")
        self.rf_min_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.rf_min_label)

        self.rf_min_spinbox = QDoubleSpinBox(map_control)
        self.rf_min_spinbox.setObjectName(u"rf_min_spinbox")

        self.horizontalLayout.addWidget(self.rf_min_spinbox)

        self.rf_min_unit_label = QLabel(map_control)
        self.rf_min_unit_label.setObjectName(u"rf_min_unit_label")

        self.horizontalLayout.addWidget(self.rf_min_unit_label)

        self.line_104 = QFrame(map_control)
        self.line_104.setObjectName(u"line_104")
        self.line_104.setFrameShape(QFrame.VLine)
        self.line_104.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_104)

        self.rf_max_label = QLabel(map_control)
        self.rf_max_label.setObjectName(u"rf_max_label")
        self.rf_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.rf_max_label)

        self.rf_max_spinbox = QDoubleSpinBox(map_control)
        self.rf_max_spinbox.setObjectName(u"rf_max_spinbox")

        self.horizontalLayout.addWidget(self.rf_max_spinbox)

        self.rf_max_unit_label = QLabel(map_control)
        self.rf_max_unit_label.setObjectName(u"rf_max_unit_label")

        self.horizontalLayout.addWidget(self.rf_max_unit_label)

        self.line_105 = QFrame(map_control)
        self.line_105.setObjectName(u"line_105")
        self.line_105.setFrameShape(QFrame.VLine)
        self.line_105.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_105)

        self.rf_step_count_label = QLabel(map_control)
        self.rf_step_count_label.setObjectName(u"rf_step_count_label")
        self.rf_step_count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.rf_step_count_label)

        self.rf_step_count_spinbox = QSpinBox(map_control)
        self.rf_step_count_spinbox.setObjectName(u"rf_step_count_spinbox")

        self.horizontalLayout.addWidget(self.rf_step_count_spinbox)

        self.line_106 = QFrame(map_control)
        self.line_106.setObjectName(u"line_106")
        self.line_106.setFrameShape(QFrame.VLine)
        self.line_106.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_106)

        self.rf_step_size_label = QLabel(map_control)
        self.rf_step_size_label.setObjectName(u"rf_step_size_label")
        self.rf_step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.rf_step_size_label)

        self.rf_step_size_spinbox = QDoubleSpinBox(map_control)
        self.rf_step_size_spinbox.setObjectName(u"rf_step_size_spinbox")

        self.horizontalLayout.addWidget(self.rf_step_size_spinbox)

        self.rf_step_size_unit_label = QLabel(map_control)
        self.rf_step_size_unit_label.setObjectName(u"rf_step_size_unit_label")

        self.horizontalLayout.addWidget(self.rf_step_size_unit_label)

        self.line_102 = QFrame(map_control)
        self.line_102.setObjectName(u"line_102")
        self.line_102.setFrameShape(QFrame.VLine)
        self.line_102.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_102)

        self.scale_label = QLabel(map_control)
        self.scale_label.setObjectName(u"scale_label")

        self.horizontalLayout.addWidget(self.scale_label)

        self.line_103 = QFrame(map_control)
        self.line_103.setObjectName(u"line_103")
        self.line_103.setFrameShape(QFrame.VLine)
        self.line_103.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_103)

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

        self.line_101 = QFrame(map_control)
        self.line_101.setObjectName(u"line_101")
        self.line_101.setFrameShape(QFrame.VLine)
        self.line_101.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_101)

        self.scale_mass_label = QLabel(map_control)
        self.scale_mass_label.setObjectName(u"scale_mass_label")

        self.horizontalLayout.addWidget(self.scale_mass_label)

        self.mass_spinbox = QDoubleSpinBox(map_control)
        self.mass_spinbox.setObjectName(u"mass_spinbox")

        self.horizontalLayout.addWidget(self.mass_spinbox)

        self.scale_mass_unit_label = QLabel(map_control)
        self.scale_mass_unit_label.setObjectName(u"scale_mass_unit_label")

        self.horizontalLayout.addWidget(self.scale_mass_unit_label)

        self.scale_rf_label = QLabel(map_control)
        self.scale_rf_label.setObjectName(u"scale_rf_label")

        self.horizontalLayout.addWidget(self.scale_rf_label)

        self.rf_spinbox = QDoubleSpinBox(map_control)
        self.rf_spinbox.setObjectName(u"rf_spinbox")

        self.horizontalLayout.addWidget(self.rf_spinbox)

        self.scale_rf_unit_label = QLabel(map_control)
        self.scale_rf_unit_label.setObjectName(u"scale_rf_unit_label")

        self.horizontalLayout.addWidget(self.scale_rf_unit_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_119 = QFrame(map_control)
        self.line_119.setObjectName(u"line_119")
        self.line_119.setFrameShape(QFrame.HLine)
        self.line_119.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_119)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dc_label = QLabel(map_control)
        self.dc_label.setObjectName(u"dc_label")

        self.horizontalLayout_2.addWidget(self.dc_label)

        self.line_109 = QFrame(map_control)
        self.line_109.setObjectName(u"line_109")
        self.line_109.setFrameShape(QFrame.VLine)
        self.line_109.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_109)

        self.dc_min_label = QLabel(map_control)
        self.dc_min_label.setObjectName(u"dc_min_label")
        self.dc_min_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dc_min_label)

        self.dc_min_spinbox = QDoubleSpinBox(map_control)
        self.dc_min_spinbox.setObjectName(u"dc_min_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_min_spinbox)

        self.dc_max_label = QLabel(map_control)
        self.dc_max_label.setObjectName(u"dc_max_label")

        self.horizontalLayout_2.addWidget(self.dc_max_label)

        self.line_110 = QFrame(map_control)
        self.line_110.setObjectName(u"line_110")
        self.line_110.setFrameShape(QFrame.VLine)
        self.line_110.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_110)

        self.dc_max_label_2 = QLabel(map_control)
        self.dc_max_label_2.setObjectName(u"dc_max_label_2")
        self.dc_max_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dc_max_label_2)

        self.dc_max_spinbox = QDoubleSpinBox(map_control)
        self.dc_max_spinbox.setObjectName(u"dc_max_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_max_spinbox)

        self.dc_max_unit_label = QLabel(map_control)
        self.dc_max_unit_label.setObjectName(u"dc_max_unit_label")

        self.horizontalLayout_2.addWidget(self.dc_max_unit_label)

        self.line_111 = QFrame(map_control)
        self.line_111.setObjectName(u"line_111")
        self.line_111.setFrameShape(QFrame.VLine)
        self.line_111.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_111)

        self.dc_step_count_label = QLabel(map_control)
        self.dc_step_count_label.setObjectName(u"dc_step_count_label")
        self.dc_step_count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dc_step_count_label)

        self.dc_step_count_spinbox = QSpinBox(map_control)
        self.dc_step_count_spinbox.setObjectName(u"dc_step_count_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_step_count_spinbox)

        self.line_112 = QFrame(map_control)
        self.line_112.setObjectName(u"line_112")
        self.line_112.setFrameShape(QFrame.VLine)
        self.line_112.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_112)

        self.dc_step_size_label = QLabel(map_control)
        self.dc_step_size_label.setObjectName(u"dc_step_size_label")
        self.dc_step_size_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dc_step_size_label)

        self.dc_step_size_spinbox = QDoubleSpinBox(map_control)
        self.dc_step_size_spinbox.setObjectName(u"dc_step_size_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_step_size_spinbox)

        self.dc_step_size_unit_label = QLabel(map_control)
        self.dc_step_size_unit_label.setObjectName(u"dc_step_size_unit_label")

        self.horizontalLayout_2.addWidget(self.dc_step_size_unit_label)

        self.line_107 = QFrame(map_control)
        self.line_107.setObjectName(u"line_107")
        self.line_107.setFrameShape(QFrame.VLine)
        self.line_107.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_107)

        self.dc_offset_map_label = QLabel(map_control)
        self.dc_offset_map_label.setObjectName(u"dc_offset_map_label")
        self.dc_offset_map_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dc_offset_map_label)

        self.dc_offset_spinbox = QDoubleSpinBox(map_control)
        self.dc_offset_spinbox.setObjectName(u"dc_offset_spinbox")

        self.horizontalLayout_2.addWidget(self.dc_offset_spinbox)

        self.dc_offset_map_unit_label = QLabel(map_control)
        self.dc_offset_map_unit_label.setObjectName(u"dc_offset_map_unit_label")

        self.horizontalLayout_2.addWidget(self.dc_offset_map_unit_label)

        self.line_108 = QFrame(map_control)
        self.line_108.setObjectName(u"line_108")
        self.line_108.setFrameShape(QFrame.VLine)
        self.line_108.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_108)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_116 = QFrame(map_control)
        self.line_116.setObjectName(u"line_116")
        self.line_116.setFrameShape(QFrame.HLine)
        self.line_116.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_116)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.steps_label = QLabel(map_control)
        self.steps_label.setObjectName(u"steps_label")
        self.steps_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.steps_label)

        self.steps_label_value_label = QLabel(map_control)
        self.steps_label_value_label.setObjectName(u"steps_label_value_label")

        self.horizontalLayout_3.addWidget(self.steps_label_value_label)

        self.progessbar = QProgressBar(map_control)
        self.progessbar.setObjectName(u"progessbar")
        self.progessbar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progessbar)

        self.time_left_label_2 = QLabel(map_control)
        self.time_left_label_2.setObjectName(u"time_left_label_2")
        self.time_left_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.time_left_label_2)

        self.time_left_label = QLabel(map_control)
        self.time_left_label.setObjectName(u"time_left_label")

        self.horizontalLayout_3.addWidget(self.time_left_label)

        self.full_time_label = QLabel(map_control)
        self.full_time_label.setObjectName(u"full_time_label")
        self.full_time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.full_time_label)

        self.full_time_value_label = QLabel(map_control)
        self.full_time_value_label.setObjectName(u"full_time_value_label")

        self.horizontalLayout_3.addWidget(self.full_time_value_label)

        self.start_push_button = QPushButton(map_control)
        self.start_push_button.setObjectName(u"start_push_button")

        self.horizontalLayout_3.addWidget(self.start_push_button)

        self.stop_push_button = QPushButton(map_control)
        self.stop_push_button.setObjectName(u"stop_push_button")

        self.horizontalLayout_3.addWidget(self.stop_push_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_117 = QFrame(map_control)
        self.line_117.setObjectName(u"line_117")
        self.line_117.setFrameShape(QFrame.HLine)
        self.line_117.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_117)

        self.line_120 = QFrame(map_control)
        self.line_120.setObjectName(u"line_120")
        self.line_120.setFrameShape(QFrame.HLine)
        self.line_120.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_120)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.parameters_label = QLabel(map_control)
        self.parameters_label.setObjectName(u"parameters_label")

        self.horizontalLayout_4.addWidget(self.parameters_label)

        self.line_113 = QFrame(map_control)
        self.line_113.setObjectName(u"line_113")
        self.line_113.setFrameShape(QFrame.VLine)
        self.line_113.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_113)

        self.a_label = QLabel(map_control)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.a_label)

        self.a_spinbox = QDoubleSpinBox(map_control)
        self.a_spinbox.setObjectName(u"a_spinbox")

        self.horizontalLayout_4.addWidget(self.a_spinbox)

        self.a_unit_label = QLabel(map_control)
        self.a_unit_label.setObjectName(u"a_unit_label")

        self.horizontalLayout_4.addWidget(self.a_unit_label)

        self.b_label = QLabel(map_control)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.b_label)

        self.b_spinbox = QDoubleSpinBox(map_control)
        self.b_spinbox.setObjectName(u"b_spinbox")

        self.horizontalLayout_4.addWidget(self.b_spinbox)

        self.b_unit_label = QLabel(map_control)
        self.b_unit_label.setObjectName(u"b_unit_label")

        self.horizontalLayout_4.addWidget(self.b_unit_label)

        self.line_115 = QFrame(map_control)
        self.line_115.setObjectName(u"line_115")
        self.line_115.setFrameShape(QFrame.VLine)
        self.line_115.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_115)

        self.x1_label = QLabel(map_control)
        self.x1_label.setObjectName(u"x1_label")
        self.x1_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.x1_label)

        self.x1_spinbox = QDoubleSpinBox(map_control)
        self.x1_spinbox.setObjectName(u"x1_spinbox")

        self.horizontalLayout_4.addWidget(self.x1_spinbox)

        self.x1_unit_label = QLabel(map_control)
        self.x1_unit_label.setObjectName(u"x1_unit_label")

        self.horizontalLayout_4.addWidget(self.x1_unit_label)

        self.y1_label = QLabel(map_control)
        self.y1_label.setObjectName(u"y1_label")
        self.y1_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.y1_label)

        self.y1_spinbox = QDoubleSpinBox(map_control)
        self.y1_spinbox.setObjectName(u"y1_spinbox")

        self.horizontalLayout_4.addWidget(self.y1_spinbox)

        self.y1_unit_label = QLabel(map_control)
        self.y1_unit_label.setObjectName(u"y1_unit_label")

        self.horizontalLayout_4.addWidget(self.y1_unit_label)

        self.x2_label = QLabel(map_control)
        self.x2_label.setObjectName(u"x2_label")
        self.x2_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.x2_label)

        self.x2_spinbox = QDoubleSpinBox(map_control)
        self.x2_spinbox.setObjectName(u"x2_spinbox")

        self.horizontalLayout_4.addWidget(self.x2_spinbox)

        self.x2_unit_label = QLabel(map_control)
        self.x2_unit_label.setObjectName(u"x2_unit_label")

        self.horizontalLayout_4.addWidget(self.x2_unit_label)

        self.y2_label = QLabel(map_control)
        self.y2_label.setObjectName(u"y2_label")
        self.y2_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.y2_label)

        self.y2_spinbox = QDoubleSpinBox(map_control)
        self.y2_spinbox.setObjectName(u"y2_spinbox")

        self.horizontalLayout_4.addWidget(self.y2_spinbox)

        self.y2_unit_label = QLabel(map_control)
        self.y2_unit_label.setObjectName(u"y2_unit_label")

        self.horizontalLayout_4.addWidget(self.y2_unit_label)

        self.line_114 = QFrame(map_control)
        self.line_114.setObjectName(u"line_114")
        self.line_114.setFrameShape(QFrame.VLine)
        self.line_114.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_114)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_4.setStretch(22, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_118 = QFrame(map_control)
        self.line_118.setObjectName(u"line_118")
        self.line_118.setFrameShape(QFrame.HLine)
        self.line_118.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_118)


        self.retranslateUi(map_control)

        QMetaObject.connectSlotsByName(map_control)
    # setupUi

    def retranslateUi(self, map_control):
        map_control.setWindowTitle(QCoreApplication.translate("map_control", u"Form", None))
        self.rf_label.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">RF:</span></p></body></html>", None))
        self.rf_min_label.setText(QCoreApplication.translate("map_control", u"Min:", None))
        self.rf_min_unit_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.rf_max_label.setText(QCoreApplication.translate("map_control", u"Max:", None))
        self.rf_max_unit_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.rf_step_count_label.setText(QCoreApplication.translate("map_control", u"Step count:", None))
        self.rf_step_size_label.setText(QCoreApplication.translate("map_control", u"Step size:", None))
        self.rf_step_size_unit_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.scale_label.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">Scale:</span></p></body></html>", None))
        self.rf_u_scale_label.setText(QCoreApplication.translate("map_control", u"RF-to-Unit Scale:", None))
        self.rf_u_scale_unit_label.setText(QCoreApplication.translate("map_control", u"[u/V]", None))
        self.scale_mass_label.setText(QCoreApplication.translate("map_control", u"Mass:", None))
        self.scale_mass_unit_label.setText(QCoreApplication.translate("map_control", u"[u]", None))
        self.scale_rf_label.setText(QCoreApplication.translate("map_control", u"RF:", None))
        self.scale_rf_unit_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.dc_label.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">DC:</span></p></body></html>", None))
        self.dc_min_label.setText(QCoreApplication.translate("map_control", u"Min:", None))
        self.dc_max_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.dc_max_label_2.setText(QCoreApplication.translate("map_control", u"Max:", None))
        self.dc_max_unit_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.dc_step_count_label.setText(QCoreApplication.translate("map_control", u"Step count:", None))
        self.dc_step_size_label.setText(QCoreApplication.translate("map_control", u"Step size:", None))
        self.dc_step_size_unit_label.setText(QCoreApplication.translate("map_control", u"[V]", None))
        self.dc_offset_map_label.setText(QCoreApplication.translate("map_control", u"Offset proportional to RF:", None))
        self.dc_offset_map_unit_label.setText(QCoreApplication.translate("map_control", u"[Vdc/Vrf]", None))
        self.steps_label.setText(QCoreApplication.translate("map_control", u"Steps:", None))
        self.steps_label_value_label.setText(QCoreApplication.translate("map_control", u"0/0", None))
        self.time_left_label_2.setText(QCoreApplication.translate("map_control", u"Time left:", None))
        self.time_left_label.setText(QCoreApplication.translate("map_control", u"00:00:00", None))
        self.full_time_label.setText(QCoreApplication.translate("map_control", u"Full time:", None))
        self.full_time_value_label.setText(QCoreApplication.translate("map_control", u"00:00:00", None))
        self.start_push_button.setText(QCoreApplication.translate("map_control", u"Start", None))
        self.stop_push_button.setText(QCoreApplication.translate("map_control", u"Stop", None))
        self.parameters_label.setText(QCoreApplication.translate("map_control", u"<html><head/><body><p><span style=\" font-weight:600;\">Scanline:</span></p></body></html>", None))
        self.a_label.setText(QCoreApplication.translate("map_control", u"a:", None))
        self.a_unit_label.setText(QCoreApplication.translate("map_control", u"[Vdc/Vrf]    ", None))
        self.b_label.setText(QCoreApplication.translate("map_control", u"b:", None))
        self.b_unit_label.setText(QCoreApplication.translate("map_control", u"[V]    ", None))
        self.x1_label.setText(QCoreApplication.translate("map_control", u"X1:", None))
        self.x1_unit_label.setText(QCoreApplication.translate("map_control", u"[Vrf]", None))
        self.y1_label.setText(QCoreApplication.translate("map_control", u"Y1:", None))
        self.y1_unit_label.setText(QCoreApplication.translate("map_control", u"[Vdc]", None))
        self.x2_label.setText(QCoreApplication.translate("map_control", u"X2:", None))
        self.x2_unit_label.setText(QCoreApplication.translate("map_control", u"[Vrf]", None))
        self.y2_label.setText(QCoreApplication.translate("map_control", u"Y2:", None))
        self.y2_unit_label.setText(QCoreApplication.translate("map_control", u"[Vdc]", None))
    # retranslateUi

