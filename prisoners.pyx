# This Python file uses the following encoding: utf-8
# This file consists of code which is used to solve Prisoner's Dilemma.
# It is used by mainwindow.pyx
import functools
import glob
import math
import os
import random
import re
import tempfile
from itertools import cycle
from statistics import mean
import numpy as np
from PySide6.QtCore import QObject, Slot, Signal
from more_itertools import roundrobin, flatten, grouper
import cython
maxrange = 9999999999999999  # max range of random seed
filename = ''  # name of file to open
from fs.memoryfs import MemoryFS

N_bin = 16
bin_dict = dict()
for i in range(16):
    pass


class PrisonersSignals(QObject):
    file = Signal(str)
    draw1 = Signal(str)
    draw2 = Signal(str, int)
    clear = Signal()
    end = Signal()


class Prisoners(QObject):
    def __init__(self, players, data):
        super().__init__()
        self.P2_strat = []
        self.chosenStrategies = []
        self.num_of_c_neighb_N_players = []
        self.id_N_players = []
        self.parents_strategies = []
        self.id_N_players = []
        self.P2_preh = []
        self.P1_preh = []
        self.c_of_opponents = []
        self.P2_preh = []
        self.P1_preh = []
        self.c_of_opponents = []
        self.payoff_N_players = []
        self.curr_action_N_players = []
        self.fitness = []
        self.P1_strat = []
        self.SUM_with_opponents = []
        self.prehistory = []
        self.exper = -1
        self.gen = -1
        self.N_players_preh = []
        self.N_players_strat_id = []
        self.gener_history_freq = []
        self.history_freq = []
        self.history_id = []
        self.tournaments = []
        self.players = players
        self.log_n_players = math.ceil(math.log2(self.players))
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
        self.directory = tempfile.TemporaryDirectory()
        self.strategies = 'strat.txt'
        self.tempstrategies = 'tempstrat.txt'
        self.childstrategies = 'childstrat.txt'
        self.Nstrategies = 'Nstrat.txt'
        directory = glob.glob('.\\RESULTS')
        directory2 = glob.glob('.\\RESULTS_MULTIRUN')
        if len(directory) == 0: os.mkdir('.\\RESULTS')
        if len(directory2) == 0: os.mkdir('.\\RESULTS_MULTIRUN')
        files = glob.glob('.\\RESULTS\\*')
        for file in files: os.remove(file)
        if self.debug:
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
            self.bests = [[0] * (self.num_of_generations + 1) for _ in range(self.num_of_runs)]
        elif self.players != 2:
            self.choices_C = 0
            self.tournaments_num = 0
            self.createResult1N()
            self.createResult2N()
        self.mem_fs = None

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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('#  1 2 3\n')
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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('#  1 2 3\n')
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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# 10 best frequencies\n')
            file.write('# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21\n')
            file.write('# gen ' + 20 * 'history_id freq ' + '\n')

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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
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
            if self.elitist:
                file.write('# elitist_strategy = True\n')
            else:
                file.write('# elitist_strategy = False\n')
            file.write('# num_of_runs = %d\n' % self.num_of_runs)
            file.write('# seed = %d\n' % self.seed)
            file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
            file.write('# delta_freq = %d\n' % self.delta_freq)
            file.write('# gen avg_best std_best\n')



    @staticmethod
    def clearFileName():
        global filename
        filename = ''

    def getFileName(self, title):
        global filename
        self.signals.file.emit(title)
        while filename == '': ...
        filename = filename[0]

    def readData(self):
        if self.players == 2 and self.pop_size == 2:
            self.getFileName('Choose a file of strategies for 2pPD and pop_size = 2...')
            with open(filename, 'r') as f:
                file = self.mem_fs.open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 2pPD and pop_size = 2...')
            with open(filename, 'r') as f:
                self.prehistory = f.readlines()[1].split()
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 2 and self.pop_size == 3:
            self.getFileName('Choose a file of strategies for 2pPD and pop_size = 3...')
            with open(filename, 'r') as f:
                file = self.mem_fs.open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 2pPD and pop_size = 3...')
            with open(filename, 'r') as f:
                self.prehistory = f.readlines()[1].split()
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 3 and self.pop_size == 3:
            self.getFileName('Choose a file of strategies for 3pPD and pop_size = 3...')
            with open(filename, 'r') as f:
                file = self.mem_fs.open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 3pPD and pop_size = 3...')
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory.clear()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 3 and self.pop_size == 4:
            self.getFileName('Choose a file of strategies for 3pPD and pop_size = 4...')
            with open(filename, 'r') as f:
                file = self.mem_fs.open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 3pPD and pop_size = 4...')
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory.clear()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 2 and self.pop_size > 3:
            with self.mem_fs.open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(self.players ** (2 * self.prehistory_l)):
                        los = self.rng.random()
                        if los < self.prob_of_init_C:
                            file.write('1 ')
                        else:
                            file.write('0 ')
                    file.write('\n')
            self.prehistory = [self.rng.randint(0, 1) for i in range(2 * self.prehistory_l)]
        elif self.players != 2 and self.pop_size >= 4:
            with self.mem_fs.open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players)))):
                        los = self.rng.random()
                        if los < self.prob_of_init_C:
                            file.write('1 ')
                        else:
                            file.write('0 ')
                    file.write('\n')
            self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]

    def writeData(self):
        if self.debug and self.players == 2 and self.pop_size < 4:
            with open('debug.txt', 'a') as file:
                file.write('print_11:\n\n')
                file.write('Strategies:\n')
                with self.mem_fs.open(self.strategies, 'r') as file2:
                    for line in file2: file.write(line)
                file.write('\n\nPrehistory:\n')
                file.write(' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))]))
                file.write('\n')
        if self.debug and self.players != 2 and self.pop_size < 5:
            with open('debug.txt', 'a') as file:
                file.write('print_21:\n\n')
                file.write('Strategies_N:\n')
                with self.mem_fs.open(self.strategies, 'r') as file2:
                    for line in file2: file.write(line)
                file.write('\n\nPrehistory_N:')
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
            with self.mem_fs.open(self.tempstrategies, 'r') as file2:
                for line in file2: file.write(line)
            file.write('\nParent_strategies:\n')
            for p in self.parents_strategies:
                file.write(str(p) + ' ')
            file.write('\n\nChild_strategies:\n')
            with self.mem_fs.open(self.childstrategies, 'r') as file2:
                for line in file2: file.write(line)
            file.write('\n\nStrategies:\n')
            with self.mem_fs.open(self.strategies, 'r') as file2:
                for line in file2: file.write(line)

    def writeData5(self):
        with open('debug.txt', 'a') as file:
            file.write('\nprint_22:\n\n')
            file.write('id_N_players:\n')
            for i in range(len(self.id_N_players)):
                file.write(str(self.id_N_players[i]) + ' ')
            file.write('\n\nc_of_opponents:\n')
            for i in range(len(self.c_of_opponents)):
                file.write(str(self.c_of_opponents[i]) + ' ')
            file.write('\n\nN_players_strategies:\n')
            with self.mem_fs.open(self.Nstrategies, 'r') as file2:
                for line in file2:
                    file.write(line)
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
                    if self.N_players_preh[i] == 0:
                        text += ' 0 '
                    else:
                        text += ' 1 '
            text = text[:-1]
            file.write(text)
            file.write('\n\nN_players_strat_id:\n')
            for x in self.N_players_strat_id:
                file.write(str(x) + ' ')
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
            for x in self.curr_action_N_players:
                file.write(str(x) + ' ')
            file.write('\nnum_of_C_neighb_N_players:\n')
            for x in self.num_of_c_neighb_N_players:
                file.write(str(x) + ' ')
            file.write('\npayoff_N_players:\n')
            for x in self.payoff_N_players:
                file.write(str(x) + ' ')
            file.write('\nSUM_with_opponents:\n')
            for x in self.SUM_with_opponents:
                file.write(str(x) + ' ')
            file.write('\nPrehistory_N:\n')
            for i in range(len(self.prehistory)):
                if i % self.players == 0 and i != 0:
                    file.write('\n')
                file.write(str(self.prehistory[i]) + ' ')
            file.write('\nN_players_preh:\n')
            w = 0
            text = ''
            for x in self.N_players_preh:
                if type(x) == str:
                    text += x
                    w += 1
                    if w == self.prehistory_l:
                        text += '\n'
                        w = 0
                else:
                    if x == 0:
                        text += ' 0 '
                    else:
                        text += ' 1 '
            file.write(text[:-1])
            file.write('\nN_players_strat_id:\n')
            for x in self.N_players_strat_id[i]:
                file.write(str(x) + ' ')
            file.write('\ngener_history_freq:\n')
            temp = sorted(self.history_id[:])
            for t in temp:
                file.write('%d: %d\n' % (t, self.tournaments[self.history_id.index(t)]))

    def writeData7(self):
        with open('debug.txt', 'a') as file:
            file.write('\n\nprint_24:\n\n')
            file.write('DUEL NpPD\n')
            file.write('New set of players - strategies:\n\n')
            file.write('id_N_players:\n')
            for x in self.id_N_players:
                file.write(str(x) + ' ')
            file.write('\n\nN_players_strategies:\n')
            with self.mem_fs.open(self.Nstrategies, 'r') as file2:
                for line in file2: file.write(line)
            file.write('\n\nPrehistory_N:\n')
            for i in range(len(self.prehistory)):
                if i % self.players == 0 and i != 0: file.write('\n')
                file.write(str(self.prehistory[i]) + ' ')
            file.write('\n\nN_players_preh:\n')
            w = 0
            text = ''
            for x in self.N_players_preh:
                if type(x) == str:
                    text += x
                    w += 1
                    if w == self.prehistory_l:
                        text += '\n'
                        w = 0
                else:
                    if x == 0:
                        text += ' 0 '
                    else:
                        text += ' 1 '
            file.write(text[:-1])
            file.write('\n\nN_players_strat_id:\n')
            for x in self.N_players_strat_id:
                file.write(str(x) + ' ')
            file.write('\n\ngener_history_freq:\n')
            temp = sorted(self.history_id[:])
            for x in temp:
                file.write('%d: %d\n' % (x, self.tournaments[self.history_id.index(x)]))

    def ZERO_2PD_structures(self):
        self.SUM_with_opponents = [0] * self.pop_size
        self.c_of_opponents = [0] * self.pop_size
        self.gener_history_freq.clear()
        self.P1_strat.clear()
        self.P2_strat.clear()
        self.history_freq = [0] * (4 ** self.prehistory_l)
        self.fitness = [0] * self.pop_size

    def ZERO_NPD_structures(self, variant):
        self.id_N_players = [0] * self.players
        self.N_players_preh.clear()
        self.curr_action_N_players = [0] * self.players
        self.num_of_c_neighb_N_players = [0] * self.players
        self.payoff_N_players = [0] * self.players
        self.N_players_strat_id.clear()
        self.history_freq.clear()
        self.fitness = [0 for i in range(self.pop_size)]
        if variant == 'functions_NPD':
            self.c_of_opponents = [0] * self.pop_size
            self.SUM_with_opponents = [0] * self.pop_size
        if variant != 'duelNPD':
            self.history_id.clear()
            self.tournaments.clear()

    @staticmethod
    def toDecimal(data):
        return Prisoners.to_decTuple(tuple(data))

    @staticmethod
    @functools.cache
    def to_decTuple(d):
        return int("".join(str(i) for i in d), 2)

    def inic_players_2pPD(self):
        self.id_P1 = 0
        self.id_P2 = 1
        with self.mem_fs.open(self.strategies, 'r') as file:
            lines = file.readlines()
            self.P1_strat.extend([int(lines[0][i]) for i in range(len(lines[0])) if lines[0][i] != ' ' and lines[0][i] != '\n'])
            self.P2_strat.extend([int(lines[1][i]) for i in range(len(lines[1])) if lines[1][i] != ' ' and lines[1][i] != '\n'])
        self.P1_preh = self.prehistory[:]
        self.P2_preh = [0] * len(self.P1_preh)
        i = 0
        while i < len(self.P1_preh):
            self.P2_preh[i] = self.P1_preh[i + 1]
            self.P2_preh[i + 1] = self.P1_preh[i]
            i += 2
            if i >= len(self.P1_preh): break
        self.strat_id_1 = self.toDecimal(self.P1_preh)
        self.strat_id_2 = self.toDecimal(self.P2_preh)
        self.c_of_opponents = [0] * self.pop_size
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

    @functools.cache
    def int2bin(self, num):
        return format(num, f'0{self.log_n_players}b')

    def set_N_players_preh(self):
        tmp_preh = tuple(grouper(self.prehistory, self.players, incomplete='fill', fillvalue=None))
        coops = map(sum, tmp_preh)
        tmp_preh = roundrobin(*tmp_preh)
        self.N_players_preh = list(flatten((pr, self.int2bin(cc - pr)) for pr, cc in zip(tmp_preh, cycle(coops))))

    @staticmethod
    @functools.cache
    def bin2dec(num):
        return int(num, 2)

    def set_N_players_strat_id(self):
        self.N_players_strat_id = list(Prisoners.bin2dec(''.join(map(str, row))) for row in grouper(self.N_players_preh, 2 * self.prehistory_l))

    def set_gener_history_freq(self):
        for x in self.N_players_strat_id:
            self.history_id.append(x)
        self.history_id = list(dict.fromkeys(self.history_id))
        self.tournaments = [0] * len(self.history_id)
        for i in self.N_players_strat_id:
            self.tournaments[self.history_id.index(i)] += 1

    def update_gener_history_freq(self):

        for x in self.N_players_strat_id:
            if not (x in self.history_id):
                self.history_id.append(x)
                self.tournaments.append(1)
            else:
                ind = self.history_id.index(x)
                self.tournaments[ind] += 1

    def inic_players_NpPD(self):
        for i in range(self.players):
            self.id_N_players[i] = i
            number = 0
            with self.mem_fs.open(self.strategies, 'r') as file:
                Nstrats = self.mem_fs.open(self.Nstrategies, 'a')
                for line in file:
                    if number == i:
                        Nstrats.write(line)
                        break
                    number += 1
                Nstrats.close()
            self.c_of_opponents[i] += 1
        self.set_N_players_preh()
        self.set_N_players_strat_id()
        self.set_gener_history_freq()

    def functions_2PD(self):
        self.ZERO_2PD_structures()
        self.inic_players_2pPD()
        if self.debug: self.writeData2()

    def functions_NPD(self):
        self.ZERO_NPD_structures("functions_NPD")
        self.inic_players_NpPD()
        if self.debug: self.writeData5()

    def tournament2PD(self):
        for i in range(self.num_of_tournaments):
            self.curr_action_P1 = self.P1_strat[self.strat_id_1]
            self.curr_action_P2 = self.P2_strat[self.strat_id_2]
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
            self.P2_preh = [0] * len(self.P1_preh)
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
            if self.debug: self.writeData3(i + 1)

    def getStrategies(self):
        self.chosenStrategies = []
        with self.mem_fs.open(self.Nstrategies, 'r') as file:
            for line in file:
                self.chosenStrategies.append(''.join(line.split()))

    def tournamentNPD(self):
        for k in range(self.num_of_tournaments):
            self.curr_action_N_players = [int(self.chosenStrategies[i][self.N_players_strat_id[i]]) for i in range(self.players)]
            coops = sum(self.curr_action_N_players)
            self.num_of_c_neighb_N_players = [(coops - x) for x in self.curr_action_N_players]
            self.payoff_N_players = [2 * x + (0 if y == 1 else 1) for x, y in zip(self.num_of_c_neighb_N_players, self.curr_action_N_players)]
            for x, y in zip(self.id_N_players, self.payoff_N_players):
                self.SUM_with_opponents[x] += y
            self.choices_C += coops
            self.prehistory = self.curr_action_N_players + self.prehistory[:-self.players]
            self.set_N_players_preh()
            self.set_N_players_strat_id()
            self.update_gener_history_freq()
            if self.debug:
                self.writeData6(k + 1)
        self.tournaments_num += self.num_of_tournaments

    def duel2PD(self):
        self.duel_fulfilment = False
        while not self.duel_fulfilment:
            self.tournament2PD()
            self.min = min(self.c_of_opponents)
            self.id = self.c_of_opponents.index(self.min)
            if self.min == self.num_of_opponents:
                self.duel_fulfilment = True
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
                with self.mem_fs.open(self.strategies, 'r') as file:
                    lines = file.readlines()
                    self.P1_strat.extend([int(lines[self.id_P1][i]) for i in range(len(lines[self.id_P1])) if lines[self.id_P1][i] != ' ' and lines[self.id_P1][i] != '\n'])
                    self.P2_strat.extend([int(lines[self.id_P2][i]) for i in range(len(lines[self.id_P2])) if lines[self.id_P2][i] != ' ' and lines[self.id_P2][i] != '\n'])
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
                if self.debug: self.writeData2()

    def duelNPD(self):
        self.duel_fulfilment = False
        while not self.duel_fulfilment:
            self.getStrategies()
            self.tournamentNPD()
            self.min = min(self.c_of_opponents)
            self.id = self.c_of_opponents.index(self.min)
            if self.min >= self.num_of_opponents:
                self.duel_fulfilment = True
            else:
                self.ZERO_NPD_structures('duelNPD')
                with self.mem_fs.open(self.Nstrategies, 'w') as file:
                    pass
                self.id_N_players = [-1] * self.players
                self.id_N_players[0] = self.id
                self.c_of_opponents[self.id] += 1
                for i in range(1, self.players):
                    id = self.rng.randint(0, self.pop_size - 1)
                    while (id in self.id_N_players): id = self.rng.randint(0, self.pop_size - 1)
                    self.id_N_players[i] = id
                    self.c_of_opponents[id] += 1
                for i in range(self.players):
                    number = 0
                    with self.mem_fs.open(self.Nstrategies, 'a') as file:
                        strats = self.mem_fs.open(self.strategies, 'r')
                        for line in strats:
                            if number == self.id_N_players[i]:
                                if line.endswith('\n'):
                                    file.write(line)
                                else:
                                    file.write(line + '\n')
                                break
                            number += 1
                        strats.close()
                self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]
                self.set_N_players_preh()
                self.set_N_players_strat_id()
                self.update_gener_history_freq()
                if self.debug: self.writeData7()

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
        else:
            self.hist_freq_show_fulfilment = False
        if self.players == 2:
            with open('.\\RESULTS\\result_1.txt', 'a') as file:
                file.write('  %d %.2f %.2f\n' % (self.gen, round(self.best_fit, 2), round(self.avg_fit, 2)))
            with open('.\\RESULTS\\result_2.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                file.write(' '.join([str(round(self.history_freq[i], 2)) for i in range(len(self.history_freq))]) + '\n')
            with open('.\\RESULTS\\result_3.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                with self.mem_fs.open(self.strategies, 'r') as file2:
                    number = 0
                    for line in file2:
                        if number == self.fitness.index(self.best_fit):
                            line = ' '.join(line.split(' '))
                            file.write(line)
                            if not line.endswith('\n'): file.write('\n')
                            break
                        number += 1
            self.signals.draw1.emit('.\\RESULTS\\result_1.txt')
            if self.hist_freq_show_fulfilment:
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
                    if self.elitist:
                        file.write('# elitist_strategy = True\n')
                    else:
                        file.write('# elitist_strategy = False\n')
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
            temp3.sort(reverse=True)
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
            with open('.\\RESULTS\\result_2N.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                for i in range(len(temp)):
                    file.write('%d %.2f ' % (temp[i][0], round(temp[i][1], 2)))
                file.write('\n')
            self.signals.draw1.emit('.\\RESULTS\\result_1N.txt')
            if self.hist_freq_show_fulfilment:
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
                    if self.elitist:
                        file.write('# elitist_strategy = True\n')
                    else:
                        file.write('# elitist_strategy = False\n')
                    file.write('# num_of_runs = %d\n' % self.num_of_runs)
                    file.write('# seed = %d\n' % self.seed)
                    file.write('# freq_gen_start = %d\n' % self.freq_gen_start)
                    file.write('# delta_freq = %d\n' % self.delta_freq)
                    file.write('# 1 2\n')
                    file.write('# history freq_of_history\n')
                    for i in range(len(temp)):
                        file.write('  %d %.2f\n' % (temp[i][0], round(temp[i][1], 2)))
                self.signals.draw2.emit(path, self.gen)

    def tournament_fun(self):
        winner = None
        for i in range(self.tournament_size):
            ind = self.rng.randint(0, self.pop_size - 1)
            if winner is None or self.fitness[ind] > self.fitness[winner]:
                winner = ind
        return winner

    def crossover_fun(self, strat1, strat2):
        los = self.rng.randint(1, (len(strat1) - 1))
        return strat1[:los] + strat2[los:], strat2[:los] + strat1[los:]

    def mutation_fun(self):
        strats = list()
        with self.mem_fs.open(self.strategies, 'r') as file:
            for line in file: strats.append(''.join(line.split()))
        for i in range(len(strats)):
            for j in range(len(strats[i])):
                los = self.rng.random()
                if los < self.mutation_prob:
                    if strats[i][j] == '0':
                        strats[i] = strats[i][:j] + '1' + strats[i][j + 1:]
                    else:
                        strats[i] = strats[i][:j] + '0' + strats[i][j + 1:]
        with self.mem_fs.open(self.strategies, 'w') as file:
            for x in strats:
                line = ' '.join(list(x)) + '\n'
                file.write(line)

    def elitist_fun(self, best_strat):
        strats = set()
        with self.mem_fs.open(self.strategies, 'r') as file:
            for line in file:
                strats.add(line[:-1])
        if not (best_strat in strats):
            with self.mem_fs.open(self.strategies, 'w') as file:
                for x in strats[:-1]:
                    line = x + '\n'
                    file.write(line)
                if best_strat.endswith('\n'):
                    file.write(best_strat)
                else:
                    line = best_strat + '\n'
                    file.write(line)

    def GAoperators(self):
        for i in range(self.num_of_generations):
            self.gen = i + 1
            winners = set()
            best_strat = ''
            number = 0
            with self.mem_fs.open(self.strategies, 'r') as file:
                best = self.fitness.index(max(self.fitness))
                for line in file:
                    if number == best:
                        best_strat = line
                        break
                    number += 1
            # tournament selection
            for j in range(self.pop_size):
                winner = self.tournament_fun()
                winners.add(winner)
                with self.mem_fs.open(self.tempstrategies, 'a') as file:
                    number = 0
                    strat = self.mem_fs.open(self.strategies, 'r')
                    for line in strat:
                        if number == winner:
                            if not line.endswith('\n'):
                                file.write(line + '\n')
                            else:
                                file.write(line)
                            break
                        number += 1
                    strat.close()
            # crossover
            self.parents_strategies = [0] * self.pop_size
            for j in range(len(self.parents_strategies)):
                if (j in winners):
                    los = self.rng.random()
                    if los < self.crossover_prob: self.parents_strategies[j] = 1
            strat1 = ''
            strat2 = ''
            new_pop_size = 0
            while new_pop_size != self.pop_size:
                with self.mem_fs.open(self.strategies, 'r') as file:
                    children = self.mem_fs.open(self.childstrategies, 'a')
                    chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    while self.parents_strategies[chosen] != 1:
                        chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    chosen2 = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    while self.parents_strategies[chosen2] != 1 or chosen2 == chosen:
                        chosen2 = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    number = 0
                    for line in file:
                        if number == chosen:
                            strat1 = ''.join(line.split())
                        elif number == chosen2:
                            strat2 = ''.join(line.split())
                        elif number > chosen and number > chosen2:
                            break
                        number += 1
                    (strat1, strat2) = self.crossover_fun(strat1, strat2)
                    children.write(' '.join(list(strat1)) + '\n')
                    children.write(' '.join(list(strat2)) + '\n')
                    new_pop_size += 2
                    if new_pop_size == (self.pop_size - 1):
                        chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                        while self.parents_strategies[chosen] != 1:
                            chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                        file.seek(0)
                        children.write(file.readlines()[chosen])
                        new_pop_size += 1
                    children.close()
            # mutation
            with self.mem_fs.open(self.strategies, 'w') as file:
                children = self.mem_fs.open(self.childstrategies, 'r')
                for line in children:
                    if line.endswith('\n'):
                        file.write(line)
                    else:
                        file.write(line + '\n')
                children.close()
            self.mutation_fun()
            # elitist
            if self.elitist: self.elitist_fun(best_strat)
            if self.debug: self.writeData4()
            with self.mem_fs.open(self.tempstrategies, 'w') as file:
                pass
            with self.mem_fs.open(self.childstrategies, 'w') as file:
                pass
            if self.players == 2:
                self.SUM_with_opponents = [0] * self.pop_size
                self.c_of_opponents = [0] * self.pop_size
                self.gener_history_freq = [0] * len(self.P1_strat)
                self.history_freq = [0] * len(self.P1_strat)
                self.c_of_opponents[self.id_P1] += 1
                self.c_of_opponents[self.id_P2] += 1
                self.duel2PD()
            elif self.players != 2:
                self.SUM_with_opponents = [0] * self.pop_size
                self.c_of_opponents = [0] * self.pop_size
                self.history_id.clear()
                self.tournaments.clear()
                self.set_gener_history_freq()
                self.history_freq.clear()
                self.ZERO_NPD_structures("GAoperators")
                with self.mem_fs.open(self.Nstrategies, 'w') as _:
                    pass
                self.id_N_players = [-1] * self.players
                self.id_N_players[0] = self.id
                self.c_of_opponents[self.id] += 1
                for j in range(1, self.players):
                    id = self.rng.randint(0, self.pop_size - 1)
                    while id in self.id_N_players:
                        id = self.rng.randint(0, self.pop_size - 1)
                    self.id_N_players[j] = id
                    self.c_of_opponents[id] += 1
                number = 0
                with self.mem_fs.open(self.Nstrategies, 'a') as file:
                    strats = self.mem_fs.open(self.strategies, 'r')
                    for pl_id in self.id_N_players:
                        for line in strats:
                            if number == pl_id:
                                if line.endswith('\n'):
                                    file.write(line)
                                else:
                                    file.write(line + '\n')
                                strats.seek(0)
                                number = 0
                                break
                            number += 1
                    strats.close()
                self.prehistory = [self.rng.randint(0, 1) for _ in range(self.prehistory_l * self.players)]
                self.set_N_players_preh()
                self.set_N_players_strat_id()
                self.update_gener_history_freq()
                if self.debug: self.writeData5()
                self.duelNPD()
            self.fitnessStatistics()

    @Slot()
    def launch(self):
        with MemoryFS() as self.mem_fs:
            for i in range(self.num_of_runs):
                if self.num_of_runs > 1 and self.players == 2:
                    self.exper = i + 1
                    self.createResult1()
                    self.createResult2()
                    self.createResult3()
                    self.start = self.freq_gen_start
                    if self.exper != 1:
                        with open('.\\RESULTS_MULTIRUN\\m_result_1.txt', 'a') as file: file.write('\n')
                elif self.num_of_runs > 1 and self.players != 2:
                    self.createResult1N()
                    self.createResult2N()
                    self.start = self.freq_gen_start
                self.gen = 0
                self.readData()
                self.writeData()
                if self.players == 2:
                    self.functions_2PD()
                else:
                    self.functions_NPD()
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
            self.signals.end.emit()
