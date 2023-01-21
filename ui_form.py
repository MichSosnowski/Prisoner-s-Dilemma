# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1007, 876)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plot = QWidget(self.centralwidget)
        self.plot.setObjectName(u"plot")
        self.plot.setAutoFillBackground(False)
        self.plot.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout.addWidget(self.plot, 0, 1, 1, 1)

        self.plot2 = QWidget(self.centralwidget)
        self.plot2.setObjectName(u"plot2")
        self.plot2.setAutoFillBackground(False)
        self.plot2.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout.addWidget(self.plot2, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.PDNp = QRadioButton(self.groupBox)
        self.PDNp.setObjectName(u"PDNp")

        self.gridLayout_2.addWidget(self.PDNp, 0, 1, 1, 1)

        self.seedlineEdit = QLineEdit(self.groupBox)
        self.seedlineEdit.setObjectName(u"seedlineEdit")
        self.seedlineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.seedlineEdit, 6, 1, 1, 1)

        self.runslineEdit = QLineEdit(self.groupBox)
        self.runslineEdit.setObjectName(u"runslineEdit")
        self.runslineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.runslineEdit, 5, 1, 1, 1)

        self.NlineEdit = QLineEdit(self.groupBox)
        self.NlineEdit.setObjectName(u"NlineEdit")
        self.NlineEdit.setEnabled(False)
        self.NlineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.NlineEdit, 1, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.problineEdit = QLineEdit(self.groupBox_3)
        self.problineEdit.setObjectName(u"problineEdit")
        self.problineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.problineEdit, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.tourlineEdit = QLineEdit(self.groupBox_3)
        self.tourlineEdit.setObjectName(u"tourlineEdit")
        self.tourlineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.tourlineEdit, 1, 1, 1, 1)

        self.opplineEdit = QLineEdit(self.groupBox_3)
        self.opplineEdit.setObjectName(u"opplineEdit")
        self.opplineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.opplineEdit, 2, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 3, 0, 1, 1)

        self.prelineEdit = QLineEdit(self.groupBox_3)
        self.prelineEdit.setObjectName(u"prelineEdit")
        self.prelineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.prelineEdit, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 3, 0, 1, 2)

        self.N = QLabel(self.groupBox)
        self.N.setObjectName(u"N")
        self.N.setEnabled(False)
        self.N.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.N, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.genlineEdit = QLineEdit(self.groupBox_4)
        self.genlineEdit.setObjectName(u"genlineEdit")
        self.genlineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.genlineEdit, 1, 1, 1, 1)

        self.poplineEdit = QLineEdit(self.groupBox_4)
        self.poplineEdit.setObjectName(u"poplineEdit")
        self.poplineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.poplineEdit, 0, 1, 1, 1)

        self.toursizelineEdit = QLineEdit(self.groupBox_4)
        self.toursizelineEdit.setObjectName(u"toursizelineEdit")
        self.toursizelineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.toursizelineEdit, 2, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_18, 4, 0, 1, 1)

        self.crosslineEdit = QLineEdit(self.groupBox_4)
        self.crosslineEdit.setObjectName(u"crosslineEdit")
        self.crosslineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.crosslineEdit, 3, 1, 1, 1)

        self.mutlineEdit = QLineEdit(self.groupBox_4)
        self.mutlineEdit.setObjectName(u"mutlineEdit")
        self.mutlineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.mutlineEdit, 4, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_5.addWidget(self.checkBox, 5, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_4, 4, 0, 1, 2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 10, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 6, 0, 1, 1)

        self.freqlineEdit = QLineEdit(self.groupBox)
        self.freqlineEdit.setObjectName(u"freqlineEdit")
        self.freqlineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.freqlineEdit, 7, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)

        self.groupBox2pPD = QGroupBox(self.groupBox)
        self.groupBox2pPD.setObjectName(u"groupBox2pPD")
        self.gridLayout_3 = QGridLayout(self.groupBox2pPD)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.groupBox2pPD)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox2pPD)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.C3lineEdit = QLineEdit(self.groupBox2pPD)
        self.C3lineEdit.setObjectName(u"C3lineEdit")
        self.C3lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.C3lineEdit, 1, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox2pPD)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.C4lineEdit = QLineEdit(self.groupBox2pPD)
        self.C4lineEdit.setObjectName(u"C4lineEdit")
        self.C4lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.C4lineEdit, 2, 3, 1, 1)

        self.C1lineEdit = QLineEdit(self.groupBox2pPD)
        self.C1lineEdit.setObjectName(u"C1lineEdit")
        self.C1lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.C1lineEdit, 0, 2, 1, 1)

        self.D2lineEdit = QLineEdit(self.groupBox2pPD)
        self.D2lineEdit.setObjectName(u"D2lineEdit")
        self.D2lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.D2lineEdit, 2, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox2pPD)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox2pPD)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox2pPD)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)

        self.C2lineEdit = QLineEdit(self.groupBox2pPD)
        self.C2lineEdit.setObjectName(u"C2lineEdit")
        self.C2lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.C2lineEdit, 0, 3, 1, 1)

        self.D1lineEdit = QLineEdit(self.groupBox2pPD)
        self.D1lineEdit.setObjectName(u"D1lineEdit")
        self.D1lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.D1lineEdit, 1, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox2pPD)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox2pPD)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 3, 1, 1, 1)

        self.D3lineEdit = QLineEdit(self.groupBox2pPD)
        self.D3lineEdit.setObjectName(u"D3lineEdit")
        self.D3lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.D3lineEdit, 3, 2, 1, 1)

        self.D4lineEdit = QLineEdit(self.groupBox2pPD)
        self.D4lineEdit.setObjectName(u"D4lineEdit")
        self.D4lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.D4lineEdit, 3, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox2pPD, 2, 0, 1, 2)

        self.PD2p = QRadioButton(self.groupBox)
        self.PD2p.setObjectName(u"PD2p")
        self.PD2p.setChecked(True)

        self.gridLayout_2.addWidget(self.PD2p, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 9, 0, 1, 2)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_21, 8, 0, 1, 1)

        self.deltalineEdit = QLineEdit(self.groupBox)
        self.deltalineEdit.setObjectName(u"deltalineEdit")
        self.deltalineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.deltalineEdit, 8, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.PD2p, self.PDNp)
        QWidget.setTabOrder(self.PDNp, self.NlineEdit)
        QWidget.setTabOrder(self.NlineEdit, self.C1lineEdit)
        QWidget.setTabOrder(self.C1lineEdit, self.C2lineEdit)
        QWidget.setTabOrder(self.C2lineEdit, self.C3lineEdit)
        QWidget.setTabOrder(self.C3lineEdit, self.D1lineEdit)
        QWidget.setTabOrder(self.D1lineEdit, self.D2lineEdit)
        QWidget.setTabOrder(self.D2lineEdit, self.C4lineEdit)
        QWidget.setTabOrder(self.C4lineEdit, self.D3lineEdit)
        QWidget.setTabOrder(self.D3lineEdit, self.D4lineEdit)
        QWidget.setTabOrder(self.D4lineEdit, self.problineEdit)
        QWidget.setTabOrder(self.problineEdit, self.tourlineEdit)
        QWidget.setTabOrder(self.tourlineEdit, self.opplineEdit)
        QWidget.setTabOrder(self.opplineEdit, self.prelineEdit)
        QWidget.setTabOrder(self.prelineEdit, self.poplineEdit)
        QWidget.setTabOrder(self.poplineEdit, self.genlineEdit)
        QWidget.setTabOrder(self.genlineEdit, self.toursizelineEdit)
        QWidget.setTabOrder(self.toursizelineEdit, self.crosslineEdit)
        QWidget.setTabOrder(self.crosslineEdit, self.mutlineEdit)
        QWidget.setTabOrder(self.mutlineEdit, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.runslineEdit)
        QWidget.setTabOrder(self.runslineEdit, self.seedlineEdit)
        QWidget.setTabOrder(self.seedlineEdit, self.freqlineEdit)
        QWidget.setTabOrder(self.freqlineEdit, self.deltalineEdit)
        QWidget.setTabOrder(self.deltalineEdit, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PD game parameters", None))
        self.PDNp.setText(QCoreApplication.translate("MainWindow", u"NpPD", None))
        self.seedlineEdit.setText("")
        self.runslineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.NlineEdit.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"num_of_runs", None))
        self.groupBox_3.setTitle("")
        self.problineEdit.setText(QCoreApplication.translate("MainWindow", u"0,5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"prob_of_init_C", None))
        self.tourlineEdit.setText(QCoreApplication.translate("MainWindow", u"151", None))
        self.opplineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"num_of_tournaments", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"num_of_opponents \u2a7e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"prehistory l", None))
        self.prelineEdit.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GA parameters", None))
        self.genlineEdit.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.poplineEdit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.toursizelineEdit.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"mutation_prob", None))
        self.crosslineEdit.setText(QCoreApplication.translate("MainWindow", u"0,9", None))
        self.mutlineEdit.setText(QCoreApplication.translate("MainWindow", u"0,003", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"tournament_size", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"crossover_prob", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"pop_size", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"num_of_generations", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"elitist_strategy", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"seed", None))
        self.freqlineEdit.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"freq_gen_start", None))
        self.groupBox2pPD.setTitle(QCoreApplication.translate("MainWindow", u"2pPD payoff function", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.C3lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.C4lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C1lineEdit.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.D2lineEdit.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.C2lineEdit.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.D1lineEdit.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.D3lineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.D4lineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.PD2p.setText(QCoreApplication.translate("MainWindow", u"2pPD", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"debug", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"delta_freq", None))
        self.deltalineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
    # retranslateUi

