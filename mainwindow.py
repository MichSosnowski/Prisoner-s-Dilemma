# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIntValidator, QDoubleValidator
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')

file = 'form.ui'                                    # ui filename
windowTitle = "Prisoner's Dilemma"                  # main window title
width = 1000                                        # main window width
height = 700                                        # main window height
bottomN = 3                                         # the smallest number of players in NpPD
bottom = 0                                          # bottom of interval
top = 1000000000                                    # top of interval
topD = 1                                            # top of interval for double
numberAfterDot = 3                                  # numbers after dot in double (QDoubleValidator)
color = '#f0f0f0'                                   # color of figure
subplot = 111                                       # subplot for add_subplot
titlePlot = 'average total payoff (ATP)'            # title for the first plot
titlePlot2 = 'frequencies of applied strategies'    # title for the second plot
fontSize = 9                                        # font size for titles of plots

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        self.window = loader.load(file, None)
        self.window.setWindowTitle(windowTitle)
        self.window.resize(width, height)
        self.setConnects()
        self.setValidators()
        self.showPlots()
        self.window.show()

    def setConnects(self):
        self.window.PD2p.clicked.connect(self.selectOption)
        self.window.PDNp.clicked.connect(self.selectOption)

    def setValidators(self):
        self.window.NlineEdit.setValidator(QIntValidator(bottomN, top))
        self.window.C1lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.C2lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.C3lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.C4lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.D1lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.D2lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.D3lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.D4lineEdit.setValidator(QIntValidator(bottom, top))
        self.window.problineEdit.setValidator(QDoubleValidator(bottom, topD, numberAfterDot))
        self.window.tourlineEdit.setValidator(QIntValidator(bottom, top))
        self.window.opplineEdit.setValidator(QIntValidator(bottom, top))
        self.window.prelineEdit.setValidator(QIntValidator(bottom, top))
        self.window.poplineEdit.setValidator(QIntValidator(bottom, top))
        self.window.genlineEdit.setValidator(QIntValidator(bottom, top))
        self.window.toursizelineEdit.setValidator(QIntValidator(bottom, top))
        self.window.crosslineEdit.setValidator(QDoubleValidator(bottom, topD, numberAfterDot))
        self.window.mutlineEdit.setValidator(QDoubleValidator(bottom, topD, numberAfterDot))
        self.window.runslineEdit.setValidator(QIntValidator(bottom, top))
        self.window.seedlineEdit.setValidator(QIntValidator(bottom, top))
        self.window.freqlineEdit.setValidator(QIntValidator(bottom, top))
        self.window.deltalineEdit.setValidator(QIntValidator(bottom, top))

    def showPlots(self):
        self.fig = Figure(tight_layout=True, facecolor=color)
        self.plot = self.fig.add_subplot(subplot)
        self.plot.plot([])
        self.plot.xaxis.set_visible(False)
        self.plot.yaxis.set_visible(False)
        self.plot.set_title(titlePlot, fontsize=fontSize)

        self.fig2 = Figure(tight_layout=True, facecolor=color)
        self.plot2 = self.fig2.add_subplot(subplot)
        self.plot2.plot([])
        self.plot2.xaxis.set_visible(False)
        self.plot2.yaxis.set_visible(False)
        self.plot2.set_title(titlePlot2, fontsize=fontSize)

        self.wykres = FigureCanvasQTAgg(self.fig)
        self.wykres2 = FigureCanvasQTAgg(self.fig2)

        self.layout = QGridLayout()
        self.layout.addWidget(self.wykres)

        self.layout2 = QGridLayout()
        self.layout2.addWidget(self.wykres2)

        self.window.plot.setLayout(self.layout)
        self.window.plot2.setLayout(self.layout2)

    def selectOption(self):
        if self.window.PD2p.isChecked() == True:
            self.window.N.setEnabled(False)
            self.window.NlineEdit.setEnabled(False)
            self.window.groupBox2pPD.setEnabled(True)
        elif self.window.PDNp.isChecked() == True:
            self.window.N.setEnabled(True)
            self.window.NlineEdit.setEnabled(True)
            self.window.groupBox2pPD.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())
