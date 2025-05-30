# This Python file uses the following encoding: utf-8
# This file consists of code which is used to solve Prisoner's Dilemma.
# It is used by mainwindow.py

from PySide6.QtCore import QObject, Slot, Signal
from statistics import mean
import random, math, os, glob, time
import numpy as np
import re

maxrange = 9999999999999999                     # max range of random seed
filename = ''                                   # name of file to open

class PrisonersSignals(QObject):
    file = Signal(str)
    draw1 = Signal(str)
    draw2 = Signal(str, int)
    clear = Signal()
    end = Signal()

class Prisoners(QObject):
    def __init__(self, players, data):
        super().__init__()
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
        if self.seed == '': self.seed = random.randrange(maxrange)
        self.rng = random.Random(self.seed)
        self.freq_gen_start = data[20]
        self.start = self.freq_gen_start
        self.delta_freq = data[21]
        self.debug = data[22]
        self.strategies = list()
        self.tempstrategies = list()
        self.childstrategies = list()
        self.Nstrategies = list()
        directory = glob.glob('.\\RESULTS')
        directory2 = glob.glob('.\\RESULTS_MULTIRUN')
        if len(directory) == 0: os.mkdir('.\\RESULTS')
        if len(directory2) == 0: os.mkdir('.\\RESULTS_MULTIRUN')
        files = glob.glob('.\\RESULTS\\*')
        for file in files: os.remove(file)
        files = glob.glob('.\\RESULTS_MULTIRUN\\*')
        for file in files: os.remove(file)
        if self.debug == True:
            with open('debug.txt', 'w') as file: pass
        if self.num_of_runs == 1 and self.players == 2:
            self.createResult1()
            self.createResult2()
            self.createResult3()
        elif self.num_of_runs > 1 and self.players == 2:
            self.createResult1()
            self.createResult2()
            self.createResult3()
            self.createMResult1()
            self.createMResult2()
            self.bests = [[0 for i in range(self.num_of_generations + 1)] for j in range(self.num_of_runs)]
        elif self.num_of_runs == 1 and self.players != 2:
            self.choices_C = 0
            self.tournaments_num = 0
            self.rounds_num = 0
            self.createResult1N()
            self.createResult2N()
            self.createResult1a()
        elif self.num_of_runs > 1 and self.players != 2:
            self.choices_C = 0
            self.tournaments_num = 0
            self.rounds_num = 0
            self.createResult1N()
            self.createResult2N()
            self.createResult1a()
            self.createMResult3()
            self.createMResult1a()

    def createResult1(self):
        with open('.\\RESULTS\\result_1.txt', 'w') as file:
            file.write('# 2pPD\n')
            file.write('# C C %d %d\n' % (self.payments[0], self.payments[1]))
            file.write('# C D %d %d\n' % (self.payments[2], self.payments[3]))
            file.write('# D C %d %d\n' % (self.payments[4], self.payments[5]))
            file.write('# D D %d %d\n' % (self.payments[6], self.payments[7]))
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# 1 2 3\n')
            file.write('# gen best_fit avg_fit\n')

    def createResult2(self):
        with open('.\\RESULTS\\result_2.txt', 'w') as file:
            file.write('# 2pPD\n')
            file.write('# C C %d %d\n' % (self.payments[0], self.payments[1]))
            file.write('# C D %d %d\n' % (self.payments[2], self.payments[3]))
            file.write('# D C %d %d\n' % (self.payments[4], self.payments[5]))
            file.write('# D D %d %d\n' % (self.payments[6], self.payments[7]))
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)

    def createResult3(self):
        with open('.\\RESULTS\\result_3.txt', 'w') as file:
            file.write('# 2pPD\n')
            file.write('# C C %d %d\n' % (self.payments[0], self.payments[1]))
            file.write('# C D %d %d\n' % (self.payments[2], self.payments[3]))
            file.write('# D C %d %d\n' % (self.payments[4], self.payments[5]))
            file.write('# D D %d %d\n' % (self.payments[6], self.payments[7]))
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)

    def createResult1N(self):
        with open('.\\RESULTS\\result_1N.txt', 'w') as file:
            file.write('# %dpPD\n' % self.players)
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# 1 2 3 4 5\n')
            file.write('# gen best_fit avg_fit avg_N_of_C %_avg_C\n')

    def createResult2N(self):
        with open('.\\RESULTS\\result_2N.txt', 'w') as file:
            file.write('# %dpPD\n' % self.players)
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# 10 best frequencies\n')
            file.write('# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21\n')
            file.write('# gen ' + 20 * 'history_id freq ' + '\n')

    def createResult1a(self):
        with open('.\\RESULTS\\result_1a.txt', 'w') as file:
            file.write('# %dpPD\n' % self.players)
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# 1 2\n')
            file.write('# gen avg_N_payoff\n')

    def createMResult1(self):
        with open('.\\RESULTS_MULTIRUN\\m_result_1.txt', 'w') as file:
            file.write('# 2pPD\n')
            file.write('# C C %d %d\n' % (self.payments[0], self.payments[1]))
            file.write('# C D %d %d\n' % (self.payments[2], self.payments[3]))
            file.write('# D C %d %d\n' % (self.payments[4], self.payments[5]))
            file.write('# D D %d %d\n' % (self.payments[6], self.payments[7]))
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)

    def createMResult2(self):
        with open('.\\RESULTS_MULTIRUN\\std_result_1.txt', 'w') as file:
            file.write('# 2pPD\n')
            file.write('# C C %d %d\n' % (self.payments[0], self.payments[1]))
            file.write('# C D %d %d\n' % (self.payments[2], self.payments[3]))
            file.write('# D C %d %d\n' % (self.payments[4], self.payments[5]))
            file.write('# D D %d %d\n' % (self.payments[6], self.payments[7]))
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# gen avg_best std_best\n')

    def createMResult3(self):
        with open('.\\RESULTS_MULTIRUN\\m_result_N.txt', 'w') as file:
            file.write('# %dpPD\n' % self.players)
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)

    def createMResult1a(self):
        with open('.\\RESULTS_MULTIRUN\\m_result_1a.txt', 'w') as file:
            file.write('# %dpPD\n' % self.players)
            file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
            file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
            file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
            file.write('# prehistory l = %d\n' % self.prehistory_l)
            file.write('# pop_size = %d\n' % self.pop_size)
            file.write('# num_of_generations = %d\n' % self.num_of_generations)
            file.write('# tournament_size = %d\n' % self.tournament_size)
            file.write('# crossover_prob = %f\n' % self.crossover_prob)
            file.write('# mutation_prob = %f\n' % self.mutation_prob)
            if self.elitist == True: file.write('# elitist_strategy = True\n')
            else: file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)

    def createGnuplotScripts(self):
        files = glob.glob('.\\RESULTS\\*') + glob.glob('.\\RESULTS_MULTIRUN\\*')
        if '.\\RESULTS\\result_1.txt' in files:
            with open('.\\RESULTS\\result_1.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "average total payoff (ATP)"\n')
                file.write("plot 'result_1.txt' using 1:2 with lines lt 4 lw 3 title \"best fit\",\\\n")
                file.write("'result_1.txt' using 1:3 with lines lt 3 lw 3 title \"avg fit\"")
        a = re.compile('.*_2_.*txt')
        files2 = list(filter(a.match, files))
        if len(files2) != 0:
            for i in files2:
                path = i[:-3] + 'plt'
                name = i[10:]
                with open(path, 'w') as file:
                    file.write('set xlabel \"history\"\n')
                    file.write('set ylabel \"freq of game history\"\n')
                    file.write('set title "frequency of applied strategy"\n')
                    file.write("plot '%s' using 1:2 with lines lt 4 lw 3 title \"freq\"" % name)
        if '.\\RESULTS\\result_1N.txt' in files:
            with open('.\\RESULTS\\result_1N.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "average total payoff (ATP)"\n')
                file.write("plot 'result_1N.txt' using 1:2 with lines lt 4 lw 3 title \"best fit\",\\\n")
                file.write("'result_1N.txt' using 1:3 with lines lt 3 lw 3 title \"avg fit\"")
        if '.\\RESULTS\\result_1a.txt' in files:
            with open('.\\RESULTS\\result_1a.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "average N payoff"\n')
                file.write("plot 'result_1a.txt' using 1:2 with lines lt 4 lw 3 title \"avg N payoff\"")
        a = re.compile('.*_2N_.*txt')
        files2 = list(filter(a.match, files))
        if len(files2) != 0:
            for i in files2:
                path = i[:-3] + 'plt'
                name = i[10:]
                with open(path, 'w') as file:
                    file.write('set xlabel \"history\"\n')
                    file.write('set ylabel \"freq of game history\"\n')
                    file.write('set title "frequency of applied strategy"\n')
                    file.write("plot '%s' using 1:2 with lines lt 4 lw 3 title \"freq\"" % name)
        if '.\\RESULTS_MULTIRUN\\m_result_1.txt' in files:
            with open('.\\RESULTS_MULTIRUN\\m_result_1.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "average total payoff (ATP)"\n')
                file.write("plot 'm_result_1.txt' using 1:2 with lines lt 4 lw 3 title \"best fit\",\\\n")
                file.write("'m_result_1.txt' using 1:3 with lines lt 3 lw 3 title \"avg fit\"")
        if '.\\RESULTS_MULTIRUN\\std_result_1.txt' in files:
            with open('.\\RESULTS_MULTIRUN\\std_result_1.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "std deviation for avg best"\n')
                file.write("plot 'std_result_1.txt' using 1:2 with lines lt 4 lw 3 title \"avg best\",\\\n")
                file.write("'std_result_1.txt' using 1:2:3 with yerrorbars title \"std best\"")
        if '.\\RESULTS_MULTIRUN\\m_result_N.txt' in files:
            with open('.\\RESULTS_MULTIRUN\\m_result_N.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "average total payoff (ATP)"\n')
                file.write("plot 'm_result_N.txt' using 1:2 with lines lt 4 lw 3 title \"best fit\",\\\n")
                file.write("'m_result_N.txt' using 1:3 with lines lt 3 lw 3 title \"avg fit\"")
        if '.\\RESULTS_MULTIRUN\\m_result_1a.txt' in files:
            with open('.\\RESULTS_MULTIRUN\\m_result_1a.plt', 'w') as file:
                file.write('set xlabel \"gen\"\n')
                file.write('set title "average N payoff"\n')
                file.write("plot 'm_result_1a.txt' using 1:2 with lines lt 4 lw 3 title \"avg N payoff\"")

    def clearFileName(self):
        global filename
        filename = ''

    def getFileName(self, title):
        global filename
        self.signals.file.emit(title)
        while filename == '': ...
        filename = filename[0]

    def readData(self):
        if self.players == 2 and self.pop_size == 2:
            self.getFileName('Choose a file of strategies for 2pPD, pop_size = 2 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as file:
                lines = file.readlines()[1:]
                for line in lines:
                    individual = int(''.join(line.rsplit()), 2)
                    self.strategies.append(individual)
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 2pPD, pop_size = 2 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as f:
                self.prehistory = f.readlines()[1].split()
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 2 and self.pop_size == 3:
            self.getFileName('Choose a file of strategies for 2pPD, pop_size = 3 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as file:
                lines = file.readlines()[1:]
                for line in lines:
                    individual = int(''.join(line.rsplit()), 2)
                    self.strategies.append(individual)
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 2pPD, pop_size = 3 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as f:
                self.prehistory = f.readlines()[1].split()
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 3 and self.pop_size == 3:
            self.getFileName('Choose a file of strategies for 3pPD, pop_size = 3 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as file:
                lines = file.readlines()[1:]
                for line in lines:
                    individual = int(''.join(line.rsplit()), 2)
                    self.strategies.append(individual)
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 3pPD, pop_size = 3 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory = list()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 3 and self.pop_size == 4:
            self.getFileName('Choose a file of strategies for 3pPD, pop_size = 4 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as file:
                lines = file.readlines()[1:]
                for line in lines:
                    individual = int(''.join(line.rsplit()), 2)
                    self.strategies.append(individual)
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 3pPD, pop_size = 4 and l = %d...' % self.prehistory_l)
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory = list()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 2 and self.pop_size > 3:
            for i in range(self.pop_size):
                individual = 0
                for j in range(self.players ** (2 * self.prehistory_l)):
                    los = self.rng.random()
                    if los < self.prob_of_init_C: individual = 2 * individual + 1
                    else: individual = 2 * individual
                self.strategies.append(individual)
            self.prehistory = [self.rng.randint(0, 1) for i in range(2 * self.prehistory_l)]
        elif self.players != 2 and self.pop_size >= 4:
            for i in range(self.pop_size):
                individual = 0
                for j in range(2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players)))):
                    los = self.rng.random()
                    if los < self.prob_of_init_C: individual = 2 * individual + 1
                    else: individual = 2 * individual
                self.strategies.append(individual)
            self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]

    def writeData(self):
        if self.debug == True and self.players == 2 and self.pop_size < 4:
            with open('debug.txt', 'a') as file:
                file.write('print_11:\n\n')
                file.write('Strategies:\n')
                for i in self.strategies:
                    individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                    file.write(' '.join(individual) + '\n')
                file.write('\nPrehistory:\n')
                file.write(' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))]))
                file.write('\n')
        if self.debug == True and self.players != 2 and self.pop_size < 5:
            with open('debug.txt', 'a') as file:
                file.write('print_21:\n\n')
                file.write('Strategies_N:\n')
                for i in self.strategies:
                    individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                    file.write(' '.join(individual) + '\n')
                file.write('\nPrehistory_N:')
                for i in range(len(self.prehistory)):
                    if i % self.players == 0: file.write('\n')
                    file.write(str(self.prehistory[i]) + ' ')
                file.write('\n\n')

    def writeData2(self):
        with open('debug.txt', 'a') as file:
            file.write('\nprint_12:\n\n')
            file.write('P1_strat:\n')
            file.write(' '.join([str(self.P1_strat[i]) for i in range(len(self.P1_strat))]))
            file.write('\n\nP2_strat:\n')
            file.write(' '.join([str(self.P2_strat[i]) for i in range(len(self.P2_strat))]))
            file.write('\n\nstrat_id_1 = ' + str(self.strat_id_1))
            file.write('\nstrat_id_2 = ' + str(self.strat_id_2))
            file.write('\n\nprint_13:\n\n')
            file.write('c_of_opponents:\n')
            file.write(' '.join([str(self.c_of_opponents[i]) for i in range(len(self.c_of_opponents))]))
            file.write('\n\ngener_history_freq:\n')
            file.write(' '.join([str(self.gener_history_freq[i]) for i in range(len(self.gener_history_freq))]))
            file.write('\n')

    def writeData3(self, game):
        with open('debug.txt', 'a') as file:
            file.write('\nprint_14:\n\n')
            file.write('TOURNAMENT - 2 players\n\n')
            file.write('game = %d\n' % game)
            file.write('curr_action_P1 = %d\n' % self.curr_action_P1)
            file.write('curr_action_P2 = %d\n' % self.curr_action_P2)
            file.write('payoff_P1 = %d\n' % self.payoff_P1)
            file.write('payoff_P2 = %d' % self.payoff_P2)
            file.write('\nSUM_with_opponents:\n')
            file.write(' '.join([str(self.SUM_with_opponents[i]) for i in range(len(self.SUM_with_opponents))]))
            file.write('\nPrehistory:\n')
            file.write(' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))]))
            file.write('\nP1_preh:\n')
            file.write(' '.join([str(self.P1_preh[i]) for i in range(len(self.P1_preh))]))
            file.write('\nP2_preh:\n')
            file.write(' '.join([str(self.P2_preh[i]) for i in range(len(self.P2_preh))]))
            file.write('\nstrat_id_1 = ' + str(self.strat_id_1))
            file.write('\nstrat_id_2 = ' + str(self.strat_id_2))
            file.write('\ngener_history_freq:\n')
            file.write(' '.join([str(self.gener_history_freq[i]) for i in range(len(self.gener_history_freq))]) + '\n')

    def writeData4(self):
        with open('debug.txt', 'a') as file:
            file.write('\n\nprint_31:\n\n')
            file.write('After GA operators\n\n')
            file.write('Temp_strategies:\n')
            for i in self.tempstrategies:
                individual = 0
                if self.players == 2:
                    individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                else:
                    individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                file.write(' '.join(individual) + '\n')
            file.write('\nParent_strategies:\n')
            for i in range(len(self.parents_strategies)): file.write(str(self.parents_strategies[i]) + ' ')
            file.write('\n\nChild_strategies:\n')
            for i in self.childstrategies:
                individual = 0
                if self.players == 2:
                    individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                else:
                    individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                file.write(' '.join(individual) + '\n')
            file.write('\n\nStrategies:\n')
            for i in self.strategies:
                individual = 0
                if self.players == 2:
                    individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                else:
                    individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                file.write(' '.join(individual) + '\n')

    def writeData5(self):
        with open('debug.txt', 'a') as file:
            file.write('\nprint_22:\n\n')
            file.write('id_N_players:\n')
            for i in range(len(self.id_N_players)): file.write(str(self.id_N_players[i]) + ' ')
            file.write('\n\nc_of_opponents:\n')
            for i in range(len(self.c_of_opponents)): file.write(str(self.c_of_opponents[i]) + ' ')
            file.write('\n\nN_players_strategies:\n')
            for i in self.Nstrategies:
                individual = 0
                if self.players == 2:
                    individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                else:
                    individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                file.write(' '.join(individual) + '\n')
            file.write('\n\nN_players_preh:\n')
            w = 0
            text = ''
            for i in range(len(self.N_players_preh)):
                if type(self.N_players_preh[i]) == str:
                    text += self.N_players_preh[i]
                    w += 1
                    if w == self.prehistory_l:
                        text += '\n'
                        w = 0
                else:
                    if self.N_players_preh[i] == 0: text += ' 0 '
                    else: text += ' 1 '
            text = text[:-1]
            file.write(text)
            file.write('\n\nN_players_strat_id:\n')
            for i in range(len(self.N_players_strat_id)): file.write(str(self.N_players_strat_id[i]) + ' ')
            file.write('\n\ngener_history_freq:\n')
            temp = sorted(self.history_id[:])
            for i in range(len(temp)):
                file.write('%d: %d\n' % (temp[i], self.tournaments[self.history_id.index(temp[i])]))

    def writeData6(self, k):
        with open('debug.txt', 'a') as file:
            file.write('\n\nprint_23:\n\n')
            file.write('TOURNAMENT_N_PLAYERS\n\n')
            file.write('k = %d\n' % k)
            file.write('curr_action_N_players:\n')
            for i in range(self.players): file.write(str(self.curr_action_N_players[i]) + ' ')
            file.write('\nnum_of_C_neighb_N_players:\n')
            for i in range(self.players): file.write(str(self.num_of_c_neighb_N_players[i]) + ' ')
            file.write('\npayoff_N_players:\n')
            for i in range(self.players): file.write(str(self.payoff_N_players[i]) + ' ')
            file.write('\nSUM_payoff_N_players:\n')
            for i in self.SUM_payoff_N_players: file.write(str(i) + ' ')
            file.write('\nSUM_with_opponents:\n')
            for i in range(self.pop_size): file.write(str(self.SUM_with_opponents[i]) + ' ')
            file.write('\nPrehistory_N:\n')
            for i in range(len(self.prehistory)):
                if i % self.players == 0 and i != 0: file.write('\n')
                file.write(str(self.prehistory[i]) + ' ')
            file.write('\nN_players_preh:\n')
            w = 0
            text = ''
            for i in range(len(self.N_players_preh)):
                if type(self.N_players_preh[i]) == str:
                    text += self.N_players_preh[i]
                    w += 1
                    if w == self.prehistory_l:
                        text += '\n'
                        w = 0
                else:
                    if self.N_players_preh[i] == 0: text += ' 0 '
                    else: text += ' 1 '
            text = text[:-1]
            file.write(text)
            file.write('\nN_players_strat_id:\n')
            for i in range(self.players): file.write(str(self.N_players_strat_id[i]) + ' ')
            file.write('\ngener_history_freq:\n')
            temp = sorted(self.history_id[:])
            for i in range(len(temp)):
                file.write('%d: %d\n' % (temp[i], self.tournaments[self.history_id.index(temp[i])]))

    def writeData7(self):
        with open('debug.txt', 'a') as file:
            file.write('\n\nprint_24:\n\n')
            file.write('DUEL NpPD\n')
            file.write('New set of players - strategies:\n\n')
            file.write('id_N_players:\n')
            for i in range(len(self.id_N_players)): file.write(str(self.id_N_players[i]) + ' ')
            file.write('\n\nN_players_strategies:\n')
            for i in self.Nstrategies:
                individual = 0
                if self.players == 2:
                    individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                else:
                    individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                file.write(' '.join(individual) + '\n')
            file.write('\n\nc_of_opponents:\n')
            for i in range(len(self.c_of_opponents)): file.write(str(self.c_of_opponents[i]) + ' ')
            file.write('\n\nPrehistory_N:\n')
            for i in range(len(self.prehistory)):
                if i % self.players == 0 and i != 0: file.write('\n')
                file.write(str(self.prehistory[i]) + ' ')
            file.write('\n\nN_players_preh:\n')
            w = 0
            text = ''
            for i in range(len(self.N_players_preh)):
                if type(self.N_players_preh[i]) == str:
                    text += self.N_players_preh[i]
                    w += 1
                    if w == self.prehistory_l:
                        text += '\n'
                        w = 0
                else:
                    if self.N_players_preh[i] == 0: text += ' 0 '
                    else: text += ' 1 '
            text = text[:-1]
            file.write(text)
            file.write('\n\nN_players_strat_id:\n')
            for i in range(self.players): file.write(str(self.N_players_strat_id[i]) + ' ')
            file.write('\n\ngener_history_freq:\n')
            temp = sorted(self.history_id[:])
            for i in range(len(temp)):
                file.write('%d: %d\n' % (temp[i], self.tournaments[self.history_id.index(temp[i])]))

    def ZERO_2PD_structures(self):
        self.SUM_with_opponents = [0 for i in range(self.pop_size)]
        self.c_of_opponents = [0 for i in range(self.pop_size)]
        self.gener_history_freq = list()
        self.P1_strat = list()
        self.P2_strat = list()
        self.history_freq = [0 for i in range(4 ** self.prehistory_l)]
        self.fitness = [0 for i in range(self.pop_size)]

    def ZERO_NPD_structures(self):
        self.id_N_players = [0 for i in range(self.players)]
        self.N_players_preh = list()
        self.curr_action_N_players = [0 for i in range(self.players)]
        self.num_of_c_neighb_N_players = [0 for i in range(self.players)]
        self.payoff_N_players = [0 for i in range(self.players)]
        self.SUM_payoff_N_players = [0 for i in range(self.players)]
        self.N_players_strat_id = list()
        self.SUM_with_opponents = [0 for i in range(self.pop_size)]
        self.c_of_opponents = [0 for i in range(self.pop_size)]
        self.history_id = list()
        self.tournaments = list()
        self.history_freq = list()
        self.fitness = [0 for i in range(self.pop_size)]

    def toDecimal(self, data):
        data = [str(data[i]) for i in range(len(data))]
        data = ''.join(data)
        return int(data, 2)

    def inic_players_2pPD(self):
        self.id_P1 = 0
        self.id_P2 = 1
        self.P1_strat.extend(list(format(self.strategies[0], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]))
        self.P2_strat.extend(list(format(self.strategies[1], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]))
        self.P1_preh = self.prehistory[:]
        self.P2_preh = [0 for i in range(len(self.P1_preh))]
        i = 0
        while i < len(self.P1_preh):
            self.P2_preh[i] = self.P1_preh[i + 1]
            self.P2_preh[i + 1] = self.P1_preh[i]
            i += 2
            if i >= len(self.P1_preh): break
        self.strat_id_1 = self.toDecimal(self.P1_preh)
        self.strat_id_2 = self.toDecimal(self.P2_preh)
        self.c_of_opponents = [0 for i in range(self.pop_size)]
        self.c_of_opponents[self.id_P1] += 1
        self.c_of_opponents[self.id_P2] += 1
        self.gener_history_freq = [0 for i in range(len(self.P1_strat))]
        self.gener_history_freq[self.strat_id_1] += 1
        self.gener_history_freq[self.strat_id_2] += 1
        self.history_freq = [0 for i in range(len(self.P1_strat))]
        if self.num_of_runs == 1:
            with open('.\\RESULTS\\result_2.txt', 'a') as file:
                file.write('# frequency of game histories\n')
                file.write('# ' + ' '.join([str(i) for i in range(len(self.P1_strat) + 1)]))
                file.write('\n# gen ' + ' '.join([str(i) for i in range(len(self.P1_strat))]) + '\n')
            with open('.\\RESULTS\\result_3.txt', 'a') as file:
                file.write('# best strategy\n')
                file.write('# gen ' + ' '.join([str(i) for i in range(len(self.P1_strat))]) + '\n')

    def set_N_players_preh(self):
        k = 0
        for i in range(self.prehistory_l):
            row = self.prehistory[k:(k + self.players)]
            k += self.players
            self.N_players_preh.append(row)
        temp = [[self.N_players_preh[i][j] for i in range(len(self.N_players_preh))] for j in range(len(self.N_players_preh[0]))]
        temp2 = self.N_players_preh[:]
        self.N_players_preh = [x for i in range(len(temp)) for j in range(len(temp[0])) for x in (temp[i][j], '')]
        coops = [sum(temp2[i]) for i in range(len(temp2))]
        k = 0
        for i in range(len(self.N_players_preh)):
            if type(self.N_players_preh[i]) == str: continue
            coop = coops[k] - self.N_players_preh[i]
            result = bin(coop)[2:]
            while len(result) < math.ceil(math.log2(self.players)): result = '0' + result
            self.N_players_preh[self.N_players_preh.index('')] = result
            k += 1
            if k >= len(coops): k = 0

    def set_N_players_strat_id(self):
        i = 0
        while i < len(self.N_players_preh):
            row = self.N_players_preh[i:(i + (2 * self.prehistory_l))]
            row = [row[i] if type(row[i]) == str else str(row[i]) for i in range(len(row))]
            row = ''.join(row)
            self.N_players_strat_id.append(int(row, 2))
            i += 2 * self.prehistory_l

    def set_gener_history_freq(self):
        for i in range(len(self.N_players_strat_id)): self.history_id.append(self.N_players_strat_id[i])
        self.history_id = list(dict.fromkeys(self.history_id))
        self.tournaments = [0 for i in range(len(self.history_id))]
        for i in self.N_players_strat_id:
            self.tournaments[self.history_id.index(i)] += 1

    def update_gener_history_freq(self):
        for i in range(len(self.N_players_strat_id)):
            if (self.N_players_strat_id[i] in self.history_id) == False:
                self.history_id.append(self.N_players_strat_id[i])
                self.tournaments.append(0)
        for i in range(len(self.N_players_strat_id)):
            ind = self.history_id.index(self.N_players_strat_id[i])
            self.tournaments[ind] += 1

    def inic_players_NpPD(self):
        for i in range(self.players):
            self.id_N_players[i] = i
            self.Nstrategies.append(self.strategies[i])
            self.c_of_opponents[i] += 1
        self.set_N_players_preh()
        self.set_N_players_strat_id()
        self.set_gener_history_freq()

    def functions_2PD(self):
        self.ZERO_2PD_structures()
        self.inic_players_2pPD()
        if self.debug == True: self.writeData2()

    def functions_NPD(self):
        self.ZERO_NPD_structures()
        self.inic_players_NpPD()
        if self.debug == True: self.writeData5()

    def tournament2PD(self):
        for i in range(self.num_of_tournaments):
            self.curr_action_P1 = int(self.P1_strat[self.strat_id_1])
            self.curr_action_P2 = int(self.P2_strat[self.strat_id_2])
            if self.curr_action_P1 * self.curr_action_P2 == 1:
                self.payoff_P1 = self.payments[0]
                self.payoff_P2 = self.payments[1]
            elif self.curr_action_P1 == 1:
                self.payoff_P1 = self.payments[2]
                self.payoff_P2 = self.payments[3]
            elif self.curr_action_P2 == 1:
                self.payoff_P1 = self.payments[4]
                self.payoff_P2 = self.payments[5]
            else:
                self.payoff_P1 = self.payments[6]
                self.payoff_P2 = self.payments[7]
            self.SUM_with_opponents[self.id_P1] += self.payoff_P1
            self.SUM_with_opponents[self.id_P2] += self.payoff_P2
            self.prehistory = [self.curr_action_P1, self.curr_action_P2] + self.prehistory[:-2]
            self.P1_preh = self.prehistory[:]
            self.P2_preh = [0 for i in range(len(self.P1_preh))]
            j = 0
            while j < len(self.P1_preh):
                self.P2_preh[j] = self.P1_preh[j + 1]
                self.P2_preh[j + 1] = self.P1_preh[j]
                j += 2
                if j >= len(self.P1_preh): break
            self.strat_id_1 = self.toDecimal(self.P1_preh)
            self.strat_id_2 = self.toDecimal(self.P2_preh)
            self.gener_history_freq[self.strat_id_1] += 1
            self.gener_history_freq[self.strat_id_2] += 1
            if self.debug == True: self.writeData3(i + 1)

    def getStrategies(self):
        self.chosenStrategies = []
        for i in self.Nstrategies:
            individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
            self.chosenStrategies.append(individual)

    def tournamentNPD(self):
        for k in range(self.num_of_tournaments):
            for i in range(self.players):
                strat_id = self.N_players_strat_id[i]
                self.curr_action_N_players[i] = int(self.chosenStrategies[i][strat_id])
            coops = sum(self.curr_action_N_players)
            self.num_of_c_neighb_N_players = [(coops - self.curr_action_N_players[i]) for i in range(self.players)]
            self.payoff_N_players = [(2 * self.num_of_c_neighb_N_players[i]) if self.curr_action_N_players[i] == 1 else (2 * self.num_of_c_neighb_N_players[i] + 1) for i in range(self.players)]
            for i in range(self.players):
                self.SUM_with_opponents[self.id_N_players[i]] += self.payoff_N_players[i]
                self.SUM_payoff_N_players[i] += self.payoff_N_players[i]
            self.choices_C += coops
            self.prehistory = self.curr_action_N_players + self.prehistory[:-self.players]
            self.N_players_preh.clear()
            self.set_N_players_preh()
            self.N_players_strat_id.clear()
            self.set_N_players_strat_id()
            self.update_gener_history_freq()
            if self.debug == True: self.writeData6(k + 1)
        self.tournaments_num += self.num_of_tournaments


    def duel2PD(self):
        self.duel_fulfilment = False
        while self.duel_fulfilment == False:
            self.tournament2PD()
            self.min = min(self.c_of_opponents)
            self.id = self.c_of_opponents.index(self.min)
            if self.min == self.num_of_opponents: self.duel_fulfilment = True
            else:
                temp = self.c_of_opponents
                temp1 = self.SUM_with_opponents
                temp2 = self.gener_history_freq
                self.ZERO_2PD_structures()
                self.c_of_opponents = temp
                self.SUM_with_opponents = temp1
                self.gener_history_freq = temp2
                self.id_P1 = self.id
                self.id_P2 = self.rng.randint(0, self.pop_size - 1)
                while self.id_P2 == self.id_P1: self.id_P2 = self.rng.randint(0, self.pop_size - 1)
                self.P1_strat.extend(list(format(self.strategies[self.id_P1], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]))
                self.P2_strat.extend(list(format(self.strategies[self.id_P2], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]))
                self.prehistory = [self.rng.randint(0, 1) for i in range(len(self.prehistory))]
                self.P1_preh = self.prehistory[:]
                i = 0
                while i < len(self.P1_preh):
                    self.P2_preh[i] = self.P1_preh[i + 1]
                    self.P2_preh[i + 1] = self.P1_preh[i]
                    i += 2
                    if i >= len(self.P1_preh): break
                self.strat_id_1 = self.toDecimal(self.P1_preh)
                self.strat_id_2 = self.toDecimal(self.P2_preh)
                self.c_of_opponents[self.id_P1] += 1
                self.c_of_opponents[self.id_P2] += 1
                self.gener_history_freq[self.strat_id_1] += 1
                self.gener_history_freq[self.strat_id_2] += 1
                if self.debug == True: self.writeData2()

    def duelNPD(self):
        self.duel_fulfilment = False
        while self.duel_fulfilment == False:
            self.getStrategies()
            self.tournamentNPD()
            self.rounds_num += 1
            self.min = min(self.c_of_opponents)
            self.id = self.c_of_opponents.index(self.min)
            if self.min >= self.num_of_opponents: self.duel_fulfilment = True
            else:
                temp = self.c_of_opponents
                temp1 = self.SUM_with_opponents
                temp2 = self.history_id
                temp3 = self.tournaments
                temp4 = self.SUM_payoff_N_players
                self.ZERO_NPD_structures()
                self.Nstrategies.clear()
                self.c_of_opponents = temp
                self.SUM_with_opponents = temp1
                self.history_id = temp2
                self.tournaments = temp3
                self.SUM_payoff_N_players = temp4
                self.id_N_players = [-1 for i in range(self.players)]
                self.id_N_players[0] = self.id
                self.c_of_opponents[self.id] += 1
                for i in range(1, self.players):
                    id = self.rng.randint(0, self.pop_size - 1)
                    while (id in self.id_N_players) == True: id = self.rng.randint(0, self.pop_size - 1)
                    self.id_N_players[i] = id
                    self.c_of_opponents[id] += 1
                for i in range(self.players):
                    self.Nstrategies.append(self.strategies[self.id_N_players[i]])
                self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]
                self.set_N_players_preh()
                self.set_N_players_strat_id()
                self.update_gener_history_freq()
                if self.debug == True: self.writeData7()

    def fitnessStatistics(self):
        for i in range(self.pop_size):
            self.fitness[i] = self.SUM_with_opponents[i] / (self.num_of_tournaments * self.c_of_opponents[i])
        self.best_fit = max(self.fitness)
        self.avg_fit = mean(self.fitness)
        self.SUM_gen_hist_freq = 0
        if self.players == 2:
            for i in range(len(self.P1_strat)):
                self.SUM_gen_hist_freq += self.gener_history_freq[i]
            for i in range(len(self.P1_strat)):
                self.history_freq[i] = self.gener_history_freq[i] / self.SUM_gen_hist_freq
        else:
                self.SUM_gen_hist_freq = sum(self.tournaments)
                self.history_freq = [0 for i in range(len(self.tournaments))]
                for i in range(len(self.history_id)):
                    self.history_freq[i] = self.tournaments[i] / self.SUM_gen_hist_freq
        if self.gen == self.start:
            self.hist_freq_show_fulfilment = True
            self.start += self.delta_freq
        else: self.hist_freq_show_fulfilment = False
        if self.players == 2:
            with open('.\\RESULTS\\result_1.txt', 'a') as file:
                file.write('  %d %.2f %.2f\n' % (self.gen, round(self.best_fit, 2), round(self.avg_fit, 2)))
            with open('.\\RESULTS\\result_2.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                file.write(' '.join([str(round(self.history_freq[i], 2)) for i in range(len(self.history_freq))]) + '\n')
            with open('.\\RESULTS\\result_3.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                individual = ' '.join(list(format(self.strategies[self.fitness.index(self.best_fit)], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]))
                file.write(individual + '\n')
            self.signals.draw1.emit('.\\RESULTS\\result_1.txt')
            time.sleep(0.5)
            if self.hist_freq_show_fulfilment == True:
                path = '.\\RESULTS\\result_2_' + str(self.gen) + '.txt'
                with open(path, 'w') as file:
                    file.write('# 2pPD\n')
                    file.write('# C C %d %d\n' % (self.payments[0], self.payments[1]))
                    file.write('# C D %d %d\n' % (self.payments[2], self.payments[3]))
                    file.write('# D C %d %d\n' % (self.payments[4], self.payments[5]))
                    file.write('# D D %d %d\n' % (self.payments[6], self.payments[7]))
                    file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
                    file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
                    file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
                    file.write('# prehistory l = %d\n' % self.prehistory_l)
                    file.write('# pop_size = %d\n' % self.pop_size)
                    file.write('# num_of_generations = %d\n' % self.num_of_generations)
                    file.write('# tournament_size = %d\n' % self.tournament_size)
                    file.write('# crossover_prob = %f\n' % self.crossover_prob)
                    file.write('# mutation_prob = %f\n' % self.mutation_prob)
                    if self.elitist == True: file.write('# elitist_strategy = True\n')
                    else: file.write('# elitist_strategy = False\n')
                    file.write('# num_of_runs = %d\n' % self.num_of_runs)
                    file.write('# seed = %d\n' % self.seed)
                    file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
                    file.write('# delta_freq = %d\n' % self.delta_freq)
                    file.write('# 1 2\n')
                    file.write('# history freq_of_game_histories\n')
                    freqs = [round(self.history_freq[i], 2) for i in range(len(self.history_freq))]
                    for i in range(len(freqs)):
                        file.write('  %d %.2f\n' % (i, round(freqs[i], 2)))
                self.signals.draw2.emit(path, self.gen)
                time.sleep(0.5)
            if self.num_of_runs > 1:
                with open('.\\RESULTS_MULTIRUN\\m_result_1.txt', 'a') as file:
                    if self.gen == 0:
                        file.write('# Exper %d\n' % self.exper)
                        file.write('# 1 2 3\n')
                        file.write('# gen best_fit avg_fit\n')
                    file.write('  %d %.2f %.2f\n' % (self.gen, self.best_fit, self.avg_fit))
                self.bests[self.exper - 1][self.gen] += self.best_fit
        else:
            temp = []
            temp1, temp2, temp3 = self.history_id[:], self.history_freq[:], self.history_freq[:]
            temp3.sort(reverse = True)
            temp3 = temp3[:10]
            for i in range(len(temp3)):
                ind = temp2.index(temp3[i])
                temp.append([temp1[ind], temp2[ind]])
                temp1.pop(ind)
                temp2.pop(ind)
            temp.sort()
            with open('.\\RESULTS\\result_1N.txt', 'a') as file:
                choices = self.choices_C / self.tournaments_num
                file.write('  %d %.2f %.2f %.2f %.2f\n' % (self.gen, round(self.best_fit, 2), round(self.avg_fit, 2), round(choices, 2), round((choices / self.players), 2)))
            self.choices_C = 0
            self.tournaments_num = 0
            average = np.sum(self.SUM_payoff_N_players) / (self.rounds_num * self.num_of_tournaments * self.players)
            with open('.\\RESULTS\\result_1a.txt', 'a') as file:
                file.write('  %d %.2f\n' % (self.gen, round(average, 2)))
            self.rounds_num = 0
            with open('.\\RESULTS\\result_2N.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                for i in range(len(temp)):
                    file.write('%d %.2f ' % (temp[i][0], round(temp[i][1], 2)))
                file.write('\n')
            self.signals.draw1.emit('.\\RESULTS\\result_1N.txt')
            time.sleep(0.5)
            if self.hist_freq_show_fulfilment == True:
                path = '.\\RESULTS\\result_2N_' + str(self.gen) + '.txt'
                with open(path, 'w') as file:
                    file.write('# %dpPD\n' % self.players)
                    file.write('# prob_of_init_C = %f\n' % self.prob_of_init_C)
                    file.write('# num_of_tournaments = %d\n' % self.num_of_tournaments)
                    file.write('# num_of_opponents = %d\n' % self.num_of_opponents)
                    file.write('# prehistory l = %d\n' % self.prehistory_l)
                    file.write('# pop_size = %d\n' % self.pop_size)
                    file.write('# num_of_generations = %d\n' % self.num_of_generations)
                    file.write('# tournament_size = %d\n' % self.tournament_size)
                    file.write('# crossover_prob = %f\n' % self.crossover_prob)
                    file.write('# mutation_prob = %f\n' % self.mutation_prob)
                    if self.elitist == True: file.write('# elitist_strategy = True\n')
                    else: file.write('# elitist_strategy = False\n')
                    file.write('# num_of_runs = %d\n' % self.num_of_runs)
                    file.write('# seed = %d\n' % self.seed)
                    file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
                    file.write('# delta_freq = %d\n' % self.delta_freq)
                    file.write('# 1 2\n')
                    file.write('# history freq_of_history\n')
                    for i in range(len(temp)):
                        file.write('  %d %.2f\n' % (temp[i][0], round(temp[i][1], 2)))
                self.signals.draw2.emit(path, self.gen)
                time.sleep(0.5)
            if self.num_of_runs > 1:
                with open('.\\RESULTS_MULTIRUN\\m_result_N.txt', 'a') as file:
                    if self.gen == 0:
                        file.write('# Exper %d\n' % self.exper)
                        file.write('# 1 2 3\n')
                        file.write('# gen best_fit avg_fit\n')
                    file.write('  %d %.2f %.2f\n' % (self.gen, self.best_fit, self.avg_fit))
                with open('.\\RESULTS_MULTIRUN\\m_result_1a.txt', 'a') as file:
                    if self.gen == 0:
                        file.write('# Exper %d\n' % self.exper)
                        file.write('# 1 2\n')
                        file.write('# gen avg_N_payoff\n')
                    file.write('  %d %.2f\n' % (self.gen, round(average, 2)))

    def tournament_fun(self):
        winner = None
        for i in range(self.tournament_size):
            ind = self.rng.randint(0, self.pop_size - 1)
            if winner == None or self.fitness[ind] > self.fitness[winner]:
                winner = ind
        return winner

    def crossover_fun(self, strat1, strat2):
        los = self.rng.randint(1, (len(strat1) - 1))
        return (strat1[:los] + strat2[los:], strat2[:los] + strat1[los:])

    def mutation_fun(self):
        strats = list()
        for i in self.strategies:
            individual = 0
            if self.players == 2:
                individual = format(i, '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
            else:
                individual = format(i, '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
            strats.append(individual)
        for i in range(len(strats)):
            for j in range(len(strats[i])):
                los = self.rng.random()
                if los < self.mutation_prob:
                    if strats[i][j] == '0': strats[i] = strats[i][:j] + '1' + strats[i][j+1:]
                    else: strats[i] = strats[i][:j] + '0' + strats[i][j+1:]
        self.strategies.clear()
        for i in strats:
            self.strategies.append(int(i, 2))

    def elitist_fun(self, best_strat):
        strats = list()
        for i in self.strategies:
            strats.append(i)
        if (best_strat in strats) == False:
            self.strategies.clear()
            for i in strats:
                self.strategies.append(i)
            self.strategies.pop()
            self.strategies.append(best_strat)

    def GAoperators(self):
        for i in range(self.num_of_generations):
            self.gen = i + 1
            winners = []
            best = self.fitness.index(max(self.fitness))
            best_strat = self.strategies[best]
            # tournament selection
            for j in range(self.pop_size):
                winner = self.tournament_fun()
                if (winner in winners) == False: winners.append(winner)
                self.tempstrategies.append(self.strategies[winner])
            # crossover
            self.parents_strategies = [0 for i in range(self.pop_size)]
            for j in range(len(self.parents_strategies)):
                if (j in winners) == True:
                    los = self.rng.random()
                    if los < self.crossover_prob: self.parents_strategies[j] = 1
            strat1 = ''
            strat2 = ''
            new_pop_size = 0
            while new_pop_size != self.pop_size:
                chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                while self.parents_strategies[chosen] != 1:
                    chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                chosen2 = self.rng.randint(0, (len(self.parents_strategies) - 1))
                while self.parents_strategies[chosen2] != 1 or chosen2 == chosen:
                    chosen2 = self.rng.randint(0, (len(self.parents_strategies) - 1))
                if self.players == 2:
                    strat1 = format(self.strategies[chosen], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                    strat2 = format(self.strategies[chosen2], '#0%db' % (self.players ** (2 * self.prehistory_l) + 2))[2:]
                else:
                    strat1 = format(self.strategies[chosen], '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                    strat2 = format(self.strategies[chosen2], '#0%db' % (2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players))) + 2))[2:]
                (strat1, strat2) = self.crossover_fun(strat1, strat2)
                self.childstrategies.append(int(strat1, 2))
                self.childstrategies.append(int(strat2, 2))
                new_pop_size += 2
                if new_pop_size == (self.pop_size - 1):
                    chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    while self.parents_strategies[chosen] != 1:
                        chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    self.childstrategies.append(self.strategies[chosen])
                    new_pop_size += 1
            # mutation
            self.strategies = self.childstrategies[:]
            self.mutation_fun()
            # elitist
            if self.elitist == True: self.elitist_fun(best_strat)
            if self.debug == True: self.writeData4()
            self.tempstrategies.clear()
            self.childstrategies.clear()
            if self.players == 2:
                self.SUM_with_opponents = [0 for i in range(self.pop_size)]
                self.c_of_opponents = [0 for i in range(self.pop_size)]
                self.gener_history_freq = [0 for i in range(len(self.P1_strat))]
                self.history_freq = [0 for i in range(len(self.P1_strat))]
                self.c_of_opponents[self.id_P1] += 1
                self.c_of_opponents[self.id_P2] += 1
                self.duel2PD()
            elif self.players != 2:
                self.history_id = list()
                self.tournaments = list()
                self.set_gener_history_freq()
                self.history_freq = list()
                self.ZERO_NPD_structures()
                self.Nstrategies.clear()
                self.id_N_players = [-1 for i in range(self.players)]
                self.id_N_players[0] = self.id
                self.c_of_opponents[self.id] += 1
                for i in range(1, self.players):
                    id = self.rng.randint(0, self.pop_size - 1)
                    while (id in self.id_N_players) == True: id = self.rng.randint(0, self.pop_size - 1)
                    self.id_N_players[i] = id
                    self.c_of_opponents[id] += 1
                for i in range(self.players):
                    self.Nstrategies.append(self.strategies[self.id_N_players[i]])
                self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]
                self.set_N_players_preh()
                self.set_N_players_strat_id()
                self.update_gener_history_freq()
                if self.debug == True: self.writeData5()
                self.duelNPD()
            self.fitnessStatistics()

    @Slot()
    def launch(self):
        for i in range(self.num_of_runs):
            if self.num_of_runs > 1 and self.players == 2:
                self.exper = i + 1
                self.createResult1()
                self.createResult2()
                self.createResult3()
                self.strategies.clear()
                self.tempstrategies.clear()
                self.childstrategies.clear()
                self.start = self.freq_gen_start
                if self.exper != 1:
                    with open('.\\RESULTS_MULTIRUN\\m_result_1.txt', 'a') as file: file.write('\n')
            elif self.num_of_runs > 1 and self.players != 2:
                self.exper = i + 1
                self.createResult1N()
                self.createResult2N()
                self.strategies.clear()
                self.tempstrategies.clear()
                self.childstrategies.clear()
                self.Nstrategies.clear()
                self.start = self.freq_gen_start
                if self.exper != 1:
                    with open('.\\RESULTS_MULTIRUN\\m_result_N.txt', 'a') as file: file.write('\n')
                    with open('.\\RESULTS_MULTIRUN\\m_result_1a.txt', 'a') as file: file.write('\n')
            self.gen = 0
            self.readData()
            self.writeData()
            if self.players == 2: self.functions_2PD()
            else: self.functions_NPD()
            if self.players == 2 and self.pop_size == 2:
                self.tournament2PD()
                self.fitnessStatistics()
            elif self.players == 2 and self.pop_size > 2:
                self.duel2PD()
                self.fitnessStatistics()
                self.GAoperators()
            elif self.players != 2:
                self.duelNPD()
                self.fitnessStatistics()
                self.GAoperators()
            if self.num_of_runs > 1:
                self.signals.clear.emit()
                self.rng = random.Random(random.randrange(maxrange))
        if self.num_of_runs > 1 and self.players == 2:
            self.gen = 0
            self.bests = [[self.bests[i][j] for i in range(len(self.bests))] for j in range(len(self.bests[0]))]
            while self.gen <= self.num_of_generations:
                with open('.\\RESULTS_MULTIRUN\\std_result_1.txt', 'a') as file:
                    file.write('  %d %.2f %.2f\n' % (self.gen, round(mean(self.bests[self.gen]), 2), round(np.std(self.bests[self.gen]), 2)))
                self.gen += 1
        self.createGnuplotScripts()
        if self.num_of_runs > 1:
            files = glob.glob('.\\RESULTS\\*')
            for file in files: os.remove(file)
        self.signals.end.emit()
