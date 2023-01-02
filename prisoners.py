# This Python file uses the following encoding: utf-8
# This file consists of code which is used to solve Prisoner's Dilemma.
# It is used by mainwindow.py

from PySide6.QtCore import QObject, QRunnable, Slot, Signal
import tempfile, random

maxrange = 9999999999999999                     # max range of random seed

class PrisonersSignals(QObject):
    show = Signal(str)

class Prisoners(QRunnable):
    def __init__(self, players, data):
        super().__init__(self)
        self.players = players
        self.signals = PrisonersSignals()
        if self.players == 2: self.payments = [data[i] for i in range(8)]
        self.prob_of_init_C = data[8]
        self.num_of_tournaments = data[9]
        self.num_of_opponents = data[10]
        self.prehistory_l = data[11]
        self.pop_size = data[12]
        self.num_of_generations = data[13]
        self.tournament_size = data[14]
        self.crossover_prob = data[15]
        self.mutation_prob = data[16]
        self.elitist = data[17]
        self.num_of_runs = data[18]
        self.seed = data[19]
        self.freq_gen_start = data[20]
        self.delta_freq = data[21]
        self.debug = data[22]
        self.directory = tempfile.TemporaryDirectory()
        self.strategies = self.directory.name + '/strat.txt'

    def readData(self):
        if self.players == 2 and self.pop_size == 2:
            with open('Strategies-2PD-pop_size=2-length=64.txt', 'r') as f:
                file = open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            with open('Prehistory-1-2PD-l=3.txt', 'r') as f:
                self.prehistory = f.readlines()[1].split()
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
        elif self.players == 2 and self.pop_size == 3:
            with open('Strategies-2PD-pop_size=3-length=64.txt', 'r') as f:
                file = open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            with open('Prehistory-2-2PD-l=3.txt', 'r') as f:
                self.prehistory = f.readlines()[1].split()
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
        elif self.players == 3 and self.pop_size == 3:
            with open('Strategies-1-3PD-pop_size=3,l=2,length=64.txt', 'r') as f:
                file = open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            with open('Prehistory-1-3PD-l=2.txt', 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory = list()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
        elif self.players == 3 and self.pop_size == 4:
            pass
        elif self.players == 2 and self.pop_size > 3:
            if self.seed == '': self.seed = random.randrange(maxrange)
            rng = random.Random(self.seed)
            with open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(self.players ** self.prehistory_l):
                        file.write(str(rng.randint(0, 1)) + ' ')
                    file.write('\n')
            self.prehistory = [rng.randint(0, 1) for i in range(self.prehistory_l)]
        elif self.players != 2 and self.pop_size > 4:
            if self.seed == '': self.seed = random.randrange(maxrange)
            rng = random.Random(self.seed)
            with open(self.strategies, 'w+') as file:
                for i in range(self.pop_size):
                    for j in range(2 ** self.prehistory_l):
                        file.write(str(rng.randint(0, 1)) + ' ')
                    file.write('\n')
            self.prehistory = [rng.randint(0, 1) for i in range(self.prehistory_l)]

    def writeData(self):
        if self.debug == True and self.players == 2 and self.pop_size < 4:
            text = 'Strategies:\n'
            with open(self.strategies, 'r') as file: text += file.read()
            text += '\n\nPrehistory:\n'
            text += ' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))])
            self.signals.show.emit(text)
        if self.debug == True and self.players != 2 and self.pop_size < 5:
            text = 'Strategies_N:\n'
            with open(self.strategies, 'r') as file: text += file.read()
            text += '\n\nPrehistory_N:\n'
            text += ' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))])
            self.signals.show.emit(text)

    @Slot()
    def run(self):
        self.gen = 0
        self.readData()
        self.writeData()
