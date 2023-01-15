# This Python file uses the following encoding: utf-8
# Main file of a program
# It is responsible for GUI.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtCore import QThreadPool, Qt
import matplotlib, numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from scipy.interpolate import pchip
import prisoners

matplotlib.use('Qt5Agg')

file = 'form.ui'                                    # form.ui filename
file2 = 'dialog.ui'                                 # dialog.ui filename
windowTitle = "Prisoner's Dilemma"                  # main window title
dialogTitle = "PD Debug"                            # debug dialog
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
        self.threadpool = QThreadPool()
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
        self.dialog = loader.load(file2, self)
        self.dialog.setWindowTitle(dialogTitle)
        self.dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.dialog.setWindowFlag(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint, True)

    def setConnects(self):
        self.window.PD2p.clicked.connect(self.selectOption)
        self.window.PDNp.clicked.connect(self.selectOption)
        self.window.checkBox_2.clicked.connect(self.showDebug)
        self.window.pushButton.clicked.connect(self.start)

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
        self.window.freqlineEdit.setValidator(QIntValidator(bottom, top))
        self.window.deltalineEdit.setValidator(QIntValidator(bottom, top))

    def showPlots(self):
        self.fig = Figure(tight_layout = True, facecolor=color)
        self.plot = self.fig.add_subplot(subplot)
        self.plot.plot([])
        self.plot.xaxis.set_visible(False)
        self.plot.yaxis.set_visible(False)
        self.plot.set_title(titlePlot, fontsize=fontSize)

        self.fig2 = Figure(tight_layout = True, facecolor=color)
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

    def showDebug(self):
        if self.window.checkBox_2.isChecked() == True: self.dialog.show()
        else:
            self.dialog.hide()
            self.dialog.textEdit.clear()

    def printDebug(self, data):
        self.dialog.textEdit.append(data)

    def showFileDialog(self, title):
        prisoners.filename = QFileDialog.getOpenFileName(self, title, '.\\DATA', 'Text files (*.txt)')

    def drawScreen1(self, path):
        results = list()
        with open(path, 'r') as file:
            for line in file:
                if line.startswith('#'): continue
                results.append([float(el) for el in line.split(' ') if el != ''])
        gens = [results[i][0] for i in range(len(results))]
        best = [results[i][1] for i in range(len(results))]
        avg = [results[i][2] for i in range(len(results))]
        self.plot.clear()
        self.plot.set_title(titlePlot, fontsize=fontSize)
        self.plot.plot(gens, best, label = 'average total payoff of best indiv', color='orange')
        self.plot.plot(gens, avg, label = 'average payoff of the population', color='blue')
        self.plot.xaxis.set_visible(True)
        self.plot.yaxis.set_visible(True)
        self.plot.set_xlabel('generations')
        self.plot.legend(fontsize = 8)
        self.wykres.draw()

    def drawScreen2(self, path, gen):
        results = list()
        with open(path, 'r') as file:
            for line in file:
                if line.startswith('#'): continue
                results.append(float(''.join(line.split()[1:])))
        history = [i for i in range(len(results))]
        f = pchip(history, results)
        xnew = numpy.linspace(history[0], history[-1], num = 500, endpoint=True)
        elems = f(xnew)
        for i in range(len(elems)):
            if elems[i] < 0: elems[i] = 0
        self.plot2.plot(xnew, elems, label = ('gen %d' % gen))
        self.plot2.xaxis.set_visible(True)
        self.plot2.yaxis.set_visible(True)
        self.plot2.set_xlabel('strategies')
        self.plot2.legend(fontsize = 8)
        self.wykres2.draw()

    def clearScreens(self):
        global legend
        legend = 0
        self.plot.clear()
        self.plot.plot([])
        self.plot.xaxis.set_visible(False)
        self.plot.yaxis.set_visible(False)
        self.plot.set_title(titlePlot, fontsize=fontSize)
        self.plot2.clear()
        self.plot2.plot([])
        self.plot2.xaxis.set_visible(False)
        self.plot2.yaxis.set_visible(False)
        self.plot2.set_title(titlePlot2, fontsize=fontSize)

    def start(self):
        self.window.pushButton.setEnabled(False)
        self.clearScreens()
        players = 2
        data = [int(self.window.C1lineEdit.text()), int(self.window.C2lineEdit.text()), int(self.window.C3lineEdit.text()),
                int(self.window.D1lineEdit.text()), int(self.window.D2lineEdit.text()), int(self.window.C4lineEdit.text()),
                int(self.window.D3lineEdit.text()), int(self.window.D4lineEdit.text()), self.window.problineEdit.text(),
                int(self.window.tourlineEdit.text()), int(self.window.opplineEdit.text()), int(self.window.prelineEdit.text()),
                int(self.window.poplineEdit.text()), int(self.window.genlineEdit.text()), int(self.window.toursizelineEdit.text()),
                self.window.crosslineEdit.text(), self.window.mutlineEdit.text(), self.window.checkBox.isChecked(),
                int(self.window.runslineEdit.text()), self.window.seedlineEdit.text(), int(self.window.freqlineEdit.text()),
                int(self.window.deltalineEdit.text()), self.window.checkBox_2.isChecked()]
        for i in range(len(data)):
            if type(data[i]) == type(str()) and data[i] != '':
                data[i] = float(data[i].replace(',', '.'))
        if self.window.PD2p.isChecked() == False: players = int(self.window.NlineEdit.text())
        dilemma = prisoners.Prisoners(players, data)
        dilemma.signals.show.connect(self.printDebug)
        dilemma.signals.file.connect(self.showFileDialog)
        dilemma.signals.draw1.connect(self.drawScreen1)
        dilemma.signals.draw2.connect(self.drawScreen2)
        dilemma.signals.end.connect(lambda: self.window.pushButton.setEnabled(True))
        self.threadpool.start(dilemma)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())
