# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrum_plot.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_spectrum_plot(object):
    def setupUi(self, spectrum_plot):
        if not spectrum_plot.objectName():
            spectrum_plot.setObjectName(u"spectrum_plot")
        spectrum_plot.resize(1083, 760)
        self.verticalLayout = QVBoxLayout(spectrum_plot)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.y_axis_label = QLabel(spectrum_plot)
        self.y_axis_label.setObjectName(u"y_axis_label")

        self.horizontalLayout.addWidget(self.y_axis_label)

        self.log_checkbox = QCheckBox(spectrum_plot)
        self.log_checkbox.setObjectName(u"log_checkbox")

        self.horizontalLayout.addWidget(self.log_checkbox)

        self.y_axis_offset_label = QLabel(spectrum_plot)
        self.y_axis_offset_label.setObjectName(u"y_axis_offset_label")

        self.horizontalLayout.addWidget(self.y_axis_offset_label)

        self.offset_spinbox = QDoubleSpinBox(spectrum_plot)
        self.offset_spinbox.setObjectName(u"offset_spinbox")

        self.horizontalLayout.addWidget(self.offset_spinbox)

        self.y_axis_pA_label = QLabel(spectrum_plot)
        self.y_axis_pA_label.setObjectName(u"y_axis_pA_label")

        self.horizontalLayout.addWidget(self.y_axis_pA_label)

        self.autozero_button = QPushButton(spectrum_plot)
        self.autozero_button.setObjectName(u"autozero_button")

        self.horizontalLayout.addWidget(self.autozero_button)

        self.y_fullscale_button = QPushButton(spectrum_plot)
        self.y_fullscale_button.setObjectName(u"y_fullscale_button")

        self.horizontalLayout.addWidget(self.y_fullscale_button)

        self.line = QFrame(spectrum_plot)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.x_axis_label = QLabel(spectrum_plot)
        self.x_axis_label.setObjectName(u"x_axis_label")

        self.horizontalLayout.addWidget(self.x_axis_label)

        self.x_unit_combobox = QComboBox(spectrum_plot)
        self.x_unit_combobox.addItem("")
        self.x_unit_combobox.addItem("")
        self.x_unit_combobox.setObjectName(u"x_unit_combobox")

        self.horizontalLayout.addWidget(self.x_unit_combobox)

        self.x_fullscale_button = QPushButton(spectrum_plot)
        self.x_fullscale_button.setObjectName(u"x_fullscale_button")

        self.horizontalLayout.addWidget(self.x_fullscale_button)

        self.line_2 = QFrame(spectrum_plot)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.plot_label = QLabel(spectrum_plot)
        self.plot_label.setObjectName(u"plot_label")

        self.horizontalLayout.addWidget(self.plot_label)

        self.plot_type_combobox = QComboBox(spectrum_plot)
        self.plot_type_combobox.addItem("")
        self.plot_type_combobox.addItem("")
        self.plot_type_combobox.addItem("")
        self.plot_type_combobox.setObjectName(u"plot_type_combobox")

        self.horizontalLayout.addWidget(self.plot_type_combobox)

        self.line_3 = QFrame(spectrum_plot)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.peak_search_label = QLabel(spectrum_plot)
        self.peak_search_label.setObjectName(u"peak_search_label")

        self.horizontalLayout.addWidget(self.peak_search_label)

        self.peak_search_count_label = QLabel(spectrum_plot)
        self.peak_search_count_label.setObjectName(u"peak_search_count_label")

        self.horizontalLayout.addWidget(self.peak_search_count_label)

        self.peak_search_count_spinbox = QSpinBox(spectrum_plot)
        self.peak_search_count_spinbox.setObjectName(u"peak_search_count_spinbox")

        self.horizontalLayout.addWidget(self.peak_search_count_spinbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plot = QWidget(spectrum_plot)
        self.plot.setObjectName(u"plot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.plot)

        self.navigation_bar = QWidget(spectrum_plot)
        self.navigation_bar.setObjectName(u"navigation_bar")

        self.verticalLayout.addWidget(self.navigation_bar)


        self.retranslateUi(spectrum_plot)

        QMetaObject.connectSlotsByName(spectrum_plot)
    # setupUi

    def retranslateUi(self, spectrum_plot):
        spectrum_plot.setWindowTitle(QCoreApplication.translate("spectrum_plot", u"Form", None))
        self.y_axis_label.setText(QCoreApplication.translate("spectrum_plot", u"<html><head/><body><p><span style=\" font-weight:600;\">Y Axis:</span></p></body></html>", None))
        self.log_checkbox.setText(QCoreApplication.translate("spectrum_plot", u"Logarithmic", None))
        self.y_axis_offset_label.setText(QCoreApplication.translate("spectrum_plot", u"Offset:", None))
        self.y_axis_pA_label.setText(QCoreApplication.translate("spectrum_plot", u"pA", None))
        self.autozero_button.setText(QCoreApplication.translate("spectrum_plot", u"Auto zero", None))
        self.y_fullscale_button.setText(QCoreApplication.translate("spectrum_plot", u"Full scale", None))
        self.x_axis_label.setText(QCoreApplication.translate("spectrum_plot", u"<html><head/><body><p><span style=\" font-weight:600;\">X Axis:</span></p></body></html>", None))
        self.x_unit_combobox.setItemText(0, QCoreApplication.translate("spectrum_plot", u"unit", None))
        self.x_unit_combobox.setItemText(1, QCoreApplication.translate("spectrum_plot", u"volt", None))

        self.x_fullscale_button.setText(QCoreApplication.translate("spectrum_plot", u"Full scale", None))
        self.plot_label.setText(QCoreApplication.translate("spectrum_plot", u"<html><head/><body><p><span style=\" font-weight:600;\">Plot:</span></p></body></html>", None))
        self.plot_type_combobox.setItemText(0, QCoreApplication.translate("spectrum_plot", u"Line", None))
        self.plot_type_combobox.setItemText(1, QCoreApplication.translate("spectrum_plot", u"Scatter", None))
        self.plot_type_combobox.setItemText(2, QCoreApplication.translate("spectrum_plot", u"Histogram", None))

        self.peak_search_label.setText(QCoreApplication.translate("spectrum_plot", u"<html><head/><body><p><span style=\" font-weight:600;\">Peak search:</span></p></body></html>", None))
        self.peak_search_count_label.setText(QCoreApplication.translate("spectrum_plot", u"Count:", None))
    # retranslateUi

