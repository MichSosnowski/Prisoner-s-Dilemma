# This Python file uses the following encoding: utf-8
# Main file of a program
# It is responsible for GUI.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFileDialog
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtCore import QThread
import matplotlib, numpy, math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from scipy.interpolate import pchip
from operator import itemgetter
from ui_form import Ui_MainWindow
import prisoners

matplotlib.use('Qt5Agg')

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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.load_ui()

    def load_ui(self):
        self.setWindowTitle(windowTitle)
        self.resize(width, height)
        self.setConnects()
        self.setValidators()
        self.showPlots()
        self.show()

    def setConnects(self):
        self.PD2p.clicked.connect(self.selectOption)
        self.PDNp.clicked.connect(self.selectOption)
        self.pushButton.clicked.connect(self.start)

    def setValidators(self):
        self.NlineEdit.setValidator(QIntValidator(bottomN, top))
        self.C1lineEdit.setValidator(QIntValidator(bottom, top))
        self.C2lineEdit.setValidator(QIntValidator(bottom, top))
        self.C3lineEdit.setValidator(QIntValidator(bottom, top))
        self.C4lineEdit.setValidator(QIntValidator(bottom, top))
        self.D1lineEdit.setValidator(QIntValidator(bottom, top))
        self.D2lineEdit.setValidator(QIntValidator(bottom, top))
        self.D3lineEdit.setValidator(QIntValidator(bottom, top))
        self.D4lineEdit.setValidator(QIntValidator(bottom, top))
        self.problineEdit.setValidator(QDoubleValidator(bottom, topD, numberAfterDot))
        self.tourlineEdit.setValidator(QIntValidator(bottom, top))
        self.opplineEdit.setValidator(QIntValidator(bottom, top))
        self.prelineEdit.setValidator(QIntValidator(bottom, top))
        self.poplineEdit.setValidator(QIntValidator(bottom, top))
        self.genlineEdit.setValidator(QIntValidator(bottom, top))
        self.toursizelineEdit.setValidator(QIntValidator(bottom, top))
        self.crosslineEdit.setValidator(QDoubleValidator(bottom, topD, numberAfterDot))
        self.mutlineEdit.setValidator(QDoubleValidator(bottom, topD, numberAfterDot))
        self.runslineEdit.setValidator(QIntValidator(bottom, top))
        self.freqlineEdit.setValidator(QIntValidator(bottom, top))
        self.deltalineEdit.setValidator(QIntValidator(bottom, top))

    def showPlots(self):
        self.fig = Figure(tight_layout = True, facecolor=color)
        self.plots = self.fig.add_subplot(subplot)
        self.plots.plot([])
        self.plots.xaxis.set_visible(False)
        self.plots.yaxis.set_visible(False)
        self.plots.set_title(titlePlot, fontsize=fontSize)

        self.fig2 = Figure(tight_layout = True, facecolor=color)
        self.plots2 = self.fig2.add_subplot(subplot)
        self.plots2.plot([])
        self.plots2.xaxis.set_visible(False)
        self.plots2.yaxis.set_visible(False)
        self.plots2.set_title(titlePlot2, fontsize=fontSize)

        self.wykres = FigureCanvasQTAgg(self.fig)
        self.wykres2 = FigureCanvasQTAgg(self.fig2)

        self.layout = QGridLayout()
        self.layout.addWidget(self.wykres)

        self.layout2 = QGridLayout()
        self.layout2.addWidget(self.wykres2)

        self.plot.setLayout(self.layout)
        self.plot2.setLayout(self.layout2)

    def selectOption(self):
        if self.PD2p.isChecked() == True:
            self.N.setEnabled(False)
            self.NlineEdit.setEnabled(False)
            self.groupBox2pPD.setEnabled(True)
        elif self.PDNp.isChecked() == True:
            self.N.setEnabled(True)
            self.NlineEdit.setEnabled(True)
            self.groupBox2pPD.setEnabled(False)

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
        self.plots.clear()
        self.plots.set_title(titlePlot, fontsize=fontSize)
        self.plots.plot(gens, best, label = 'average total payoff of best indiv', color='orange')
        self.plots.plot(gens, avg, label = 'average payoff of the population', color='blue')
        self.plots.xaxis.set_visible(True)
        self.plots.yaxis.set_visible(True)
        self.plots.set_xlabel('generations')
        self.plots.legend(fontsize = 8)
        self.wykres.draw()

    def drawScreen2(self, path, gen):
        players = 2
        if self.PD2p.isChecked() == False: players = int(self.NlineEdit.text())
        results = list()
        history = []
        if players == 2:
            with open(path, 'r') as file:
                for line in file:
                    if line.startswith('#'): continue
                    results.append(float(''.join(line.split()[1:])))
            history = [i for i in range(len(results))]
        else:
            with open(path, 'r') as file:
                for line in file:
                    if line.startswith('#'): continue
                    line = line.split()
                    results.append([int(line[0]), float(line[1])])
            history = [i for i in range(2 ** (int(self.prelineEdit.text()) + int(self.prelineEdit.text()) * math.ceil(math.log2(players))))]
            temp = results[:]
            results = [0 for i in range(len(history))]
            k = 0
            for i in range(len(results)):
                if i == itemgetter(k)(temp)[0]:
                    results[i] = itemgetter(k)(temp)[1]
                    k += 1
                    if k >= len(temp): break
        f = pchip(history, results)
        xnew = numpy.linspace(history[0], history[-1], num = 500, endpoint=True)
        elems = f(xnew)
        for i in range(len(elems)):
            if elems[i] < 0: elems[i] = 0
        self.plots2.plot(xnew, elems, label = ('gen %d' % gen))
        self.plots2.xaxis.set_visible(True)
        self.plots2.yaxis.set_visible(True)
        self.plots2.set_xlabel('strategies')
        self.plots2.legend(fontsize = 8)
        self.wykres2.draw()

    def clearScreens(self):
        self.plots.clear()
        self.plots.plot([])
        self.plots.xaxis.set_visible(False)
        self.plots.yaxis.set_visible(False)
        self.plots.set_title(titlePlot, fontsize=fontSize)
        self.wykres.draw()
        self.plots2.clear()
        self.plots2.plot([])
        self.plots2.xaxis.set_visible(False)
        self.plots2.yaxis.set_visible(False)
        self.plots2.set_title(titlePlot2, fontsize=fontSize)
        self.wykres2.draw()

    def start(self):
        self.pushButton.setEnabled(False)
        self.clearScreens()
        players = 2
        data = [int(self.C1lineEdit.text()), int(self.C2lineEdit.text()), int(self.C3lineEdit.text()),
                int(self.D1lineEdit.text()), int(self.D2lineEdit.text()), int(self.C4lineEdit.text()),
                int(self.D3lineEdit.text()), int(self.D4lineEdit.text()), self.problineEdit.text(),
                int(self.tourlineEdit.text()), int(self.opplineEdit.text()), int(self.prelineEdit.text()),
                int(self.poplineEdit.text()), int(self.genlineEdit.text()), int(self.toursizelineEdit.text()),
                self.crosslineEdit.text(), self.mutlineEdit.text(), self.checkBox.isChecked(),
                int(self.runslineEdit.text()), self.seedlineEdit.text(), int(self.freqlineEdit.text()),
                int(self.deltalineEdit.text()), self.checkBox_2.isChecked()]
        for i in range(len(data)):
            if type(data[i]) == type(str()) and data[i] != '':
                data[i] = float(data[i].replace(',', '.'))
        if self.PD2p.isChecked() == False: players = int(self.NlineEdit.text())
        self.dilemma = prisoners.Prisoners(players, data)
        self.dilemma.signals.file.connect(self.showFileDialog)
        self.dilemma.signals.draw1.connect(self.drawScreen1)
        self.dilemma.signals.draw2.connect(self.drawScreen2)
        self.dilemma.signals.clear.connect(self.clearScreens)
        self.dilemma.signals.end.connect(lambda: self.pushButton.setEnabled(True))
        self.dilemma.signals.end.connect(lambda: self.thread.quit())
        self.dilemma.signals.end.connect(lambda: self.dilemma.deleteLater())
        self.dilemma.signals.end.connect(lambda: self.thread.deleteLater())
        self.thread = QThread(parent = self)
        self.dilemma.moveToThread(self.thread)
        self.thread.started.connect(self.dilemma.launch)
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())
