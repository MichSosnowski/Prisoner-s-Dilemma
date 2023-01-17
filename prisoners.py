# This Python file uses the following encoding: utf-8
# This file consists of code which is used to solve Prisoner's Dilemma.
# It is used by mainwindow.py

from PySide6.QtCore import QObject, QRunnable, Slot, Signal
from statistics import mean
import tempfile, random, math, os, glob

maxrange = 9999999999999999                     # max range of random seed
filename = ''                                   # name of file to open

class PrisonersSignals(QObject):
    show = Signal(str)
    file = Signal(str)
    draw1 = Signal(str)
    draw2 = Signal(str, int)
    end = Signal()

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
        if self.seed == '': self.seed = random.randrange(maxrange)
        self.rng = random.Random(self.seed)
        self.freq_gen_start = data[20]
        self.start = self.freq_gen_start
        self.delta_freq = data[21]
        self.debug = data[22]
        self.directory = tempfile.TemporaryDirectory()
        self.strategies = self.directory.name + '\\strat.txt'
        self.tempstrategies = self.directory.name + '\\tempstrat.txt'
        self.childstrategies = self.directory.name + '\\childstrat.txt'
        self.Nstrategies = self.directory.name + '\\Nstrat.txt'
        directory = glob.glob('.\\RESULTS')
        if len(directory) == 0: os.mkdir('.\\RESULTS')
        files = glob.glob('.\\RESULTS\\*')
        for file in files: os.remove(file)
        if self.num_of_runs == 1 and self.players == 2:
            self.createResult1()
            self.createResult2()
            self.createResult3()
        elif self.num_of_runs == 1 and self.players != 2:
            self.createResult1N()
            self.createResult2N()

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
            file.write('# NpPD\n')
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
            file.write('#  1 2 3\n')
            file.write('# gen best_fit avg_fit\n')

    def createResult2N(self):
        with open('.\\RESULTS\\result_2N.txt', 'w') as file:
            file.write('# NpPD\n')
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
            self.getFileName('Choose a file of strategies for 2pPD and pop_size = 2...')
            with open(filename, 'r') as f:
                file = open(self.strategies, 'w')
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
                file = open(self.strategies, 'w')
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
                file = open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 3pPD and pop_size = 3...')
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory = list()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 3 and self.pop_size == 4:
            self.getFileName('Choose a file of strategies for 3pPD and pop_size = 4...')
            with open(filename, 'r') as f:
                file = open(self.strategies, 'w')
                lines = f.readlines()[1:]
                for line in lines: file.write(line)
                file.close()
            self.clearFileName()
            self.getFileName('Choose a file of prehistory for 3pPD and pop_size = 4...')
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                self.prehistory = list()
                for line in lines:
                    self.prehistory.extend(line.split())
                self.prehistory = [int(self.prehistory[i]) for i in range(len(self.prehistory))]
            self.clearFileName()
        elif self.players == 2 and self.pop_size > 3:
            with open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(self.players ** (2 * self.prehistory_l)):
                        los = self.rng.random()
                        if los < self.prob_of_init_C: file.write('1 ')
                        else: file.write('0 ')
                    file.write('\n')
            self.prehistory = [self.rng.randint(0, 1) for i in range(2 * self.prehistory_l)]
        elif self.players != 2 and self.pop_size >= 4:
            with open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players)))):
                        los = self.rng.random()
                        if los < self.prob_of_init_C: file.write('1 ')
                        else: file.write('0 ')
                    file.write('\n')
            self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]

    def writeData(self):
        if self.debug == True and self.players == 2 and self.pop_size < 4:
            text = 'Strategies:\n'
            with open(self.strategies, 'r') as file:
                for line in file: text += line
            text += '\n\nPrehistory:\n'
            text += ' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))])
            self.signals.show.emit(text)
        if self.debug == True and self.players != 2 and self.pop_size < 5:
            text = 'Strategies_N:\n'
            with open(self.strategies, 'r') as file:
                for line in file: text += line
            text += '\n\nPrehistory_N:'
            for i in range(len(self.prehistory)):
                if i % self.players == 0: text += '\n'
                text += str(self.prehistory[i]) + ' '
            text += '\n'
            self.signals.show.emit(text)

    def writeData2(self):
        text = '\nP1_strat:\n'
        text += ' '.join([str(self.P1_strat[i]) for i in range(len(self.P1_strat))])
        text += '\n\nP2_strat:\n'
        text += ' '.join([str(self.P2_strat[i]) for i in range(len(self.P2_strat))])
        text += '\n\nstrat_id_1 = ' + str(self.strat_id_1)
        text += '\nstrat_id_2 = ' + str(self.strat_id_2)
        self.signals.show.emit(text)
        text = '\nc_of_opponents:\n'
        text += ' '.join([str(self.c_of_opponents[i]) for i in range(len(self.c_of_opponents))])
        text += '\n\ngener_history_freq:\n'
        text += ' '.join([str(self.gener_history_freq[i]) for i in range(len(self.gener_history_freq))])
        self.signals.show.emit(text)

    def writeData3(self, game):
        text = '\nTOURNAMENT - 2 players\n\n'
        text += 'game = %d\n' % game
        text += 'curr_action_P1 = %d\n' % self.curr_action_P1
        text += 'curr_action_P2 = %d\n' % self.curr_action_P2
        text += 'payoff_P1 = %d\n' % self.payoff_P1
        text += 'payoff_P2 = %d' % self.payoff_P2
        self.signals.show.emit(text)
        text = 'SUM_with_opponents:\n'
        text += ' '.join([str(self.SUM_with_opponents[i]) for i in range(len(self.SUM_with_opponents))])
        text += '\nPrehistory:\n'
        text += ' '.join([str(self.prehistory[i]) for i in range(len(self.prehistory))])
        text += '\nP1_preh:\n'
        text += ' '.join([str(self.P1_preh[i]) for i in range(len(self.P1_preh))])
        text += '\nP2_preh:\n'
        text += ' '.join([str(self.P2_preh[i]) for i in range(len(self.P2_preh))])
        self.signals.show.emit(text)
        text = 'strat_id_1 = ' + str(self.strat_id_1)
        text += '\nstrat_id_2 = ' + str(self.strat_id_2)
        text += '\ngener_history_freq:\n'
        text += ' '.join([str(self.gener_history_freq[i]) for i in range(len(self.gener_history_freq))]) + '\n'
        self.signals.show.emit(text)

    def writeData4(self):
        text = '\n\nAfter GA operators\n\n'
        text += 'Temp_strategies:\n'
        with open(self.tempstrategies, 'r') as file:
            for line in file: text += line
        self.signals.show.emit(text)
        text = 'Parent_strategies:\n'
        for i in range(len(self.parents_strategies)): text += str(self.parents_strategies[i]) + ' '
        text += '\n\nChild_strategies:\n'
        with open(self.childstrategies, 'r') as file:
            for line in file: text += line
        self.signals.show.emit(text)
        text = '\nStrategies:\n'
        with open(self.strategies, 'r') as file:
            for line in file: text += line
        self.signals.show.emit(text)

    def writeData5(self):
        text = 'id_N_players:\n'
        for i in range(len(self.id_N_players)): text += str(self.id_N_players[i]) + ' '
        text += '\n\nc_of_opponents:\n'
        for i in range(len(self.c_of_opponents)): text += str(self.c_of_opponents[i]) + ' '
        self.signals.show.emit(text)
        text = '\nN_players_strategies:\n'
        with open(self.strategies, 'r') as file:
            for line in file: text += line
        self.signals.show.emit(text)
        text = '\nN_players_strat_id:\n'
        for i in range(len(self.N_players_strat_id)): text += str(self.N_players_strat_id[i]) + ' '
        self.signals.show.emit(text)

    def writeData6(self, k):
        text = '\nTOURNAMENT_N_PLAYERS\n'
        text += 'k = %d\n' % k
        text += 'curr_action_N_players:\n'
        for i in range(self.players): text += str(self.curr_action_N_players[i]) + ' '
        text += '\nnum_of_C_neighb_N_players:\n'
        for i in range(self.players): text += str(self.num_of_c_neighb_N_players[i]) + ' '
        self.signals.show.emit(text)
        text = 'payoff_N_players:\n'
        for i in range(self.players): text += str(self.payoff_N_players[i]) + ' '
        text += '\nSUM_with_opponents:\n'
        for i in range(self.players): text += str(self.SUM_with_opponents[i]) + ' '
        text += '\nPrehistory_N:\n'
        for i in range(len(self.prehistory)):
            if i % self.players == 0 and i != 0: text += '\n'
            text += str(self.prehistory[i]) + ' '
        self.signals.show.emit(text)
        text = 'N_players_preh:\n'
        w = 0
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
        self.signals.show.emit(text)
        text = 'N_players_strat_id:\n'
        for i in range(self.players): text += str(self.N_players_strat_id[i]) + ' '
        self.signals.show.emit(text)

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
        with open(self.strategies, 'r') as file:
            lines = file.readlines()
            self.P1_strat.extend([int(lines[0][i]) for i in range(len(lines[0])) if lines[0][i] != ' ' and lines[0][i] != '\n'])
            self.P2_strat.extend([int(lines[1][i]) for i in range(len(lines[1])) if lines[1][i] != ' ' and lines[1][i] != '\n'])
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
        #self.gener_history_freq[self.strat_id_1] += 1
        #self.gener_history_freq[self.strat_id_2] += 1
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
        temp = []
        for i in range(len(self.N_players_preh[0])):
            temp.append([self.N_players_preh[j][i] for j in range(len(self.N_players_preh))])
        self.N_players_preh.clear()
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                self.N_players_preh.append(temp[i][j])
                self.N_players_preh.append('')
        temp.clear()
        k = 0
        for i in range(self.prehistory_l):
            row = self.prehistory[k:(k + self.players)]
            k += self.players
            temp.append(row)
        coops = []
        for i in range(len(temp)):
            coops.append(sum(temp[i]))
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
            with open(self.strategies, 'r') as file:
                Nstrats = open(self.Nstrategies, 'a')
                Nstrats.write(file.readlines()[i])
                Nstrats.close()
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

    def tournamentNPD(self):
        for k in range(self.num_of_tournaments):
            for i in range(self.players):
                strat_id = self.N_players_strat_id[i]
                with open(self.Nstrategies, 'r') as file:
                    line = file.readlines()[i]
                    line = ''.join(line.split())
                    self.curr_action_N_players[i] = int(line[strat_id])
            coops = sum(self.curr_action_N_players)
            for i in range(self.players):
                self.num_of_c_neighb_N_players[i] = coops - self.curr_action_N_players[i]
            for i in range(self.players):
                if self.curr_action_N_players[i] == 1: self.payoff_N_players[i] = 2 * self.num_of_c_neighb_N_players[i]
                else: self.payoff_N_players[i] = 2 * self.num_of_c_neighb_N_players[i] + 1
            for i in range(self.players):
                population_id = self.id_N_players[i]
                self.SUM_with_opponents[population_id] += self.payoff_N_players[i]
            if k < (self.num_of_tournaments - 1):
                self.prehistory = self.curr_action_N_players + self.prehistory[:-self.players]
                self.N_players_preh.clear()
                self.set_N_players_preh()
                self.N_players_strat_id.clear()
                self.set_N_players_strat_id()
                self.update_gener_history_freq()
            if self.debug == True: self.writeData6(k + 1)

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
                self.ZERO_2PD_structures()
                self.c_of_opponents = temp
                self.SUM_with_opponents = temp1
                self.id_P1 = self.id
                self.id_P2 = self.rng.randint(0, self.pop_size - 1)
                while self.id_P2 == self.id_P1: self.id_P2 = self.rng.randint(0, self.pop_size - 1)
                with open(self.strategies, 'r') as file:
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
                self.gener_history_freq = [0 for i in range(len(self.P1_strat))]
                self.strat_id_1 = self.toDecimal(self.P1_preh)
                self.strat_id_2 = self.toDecimal(self.P2_preh)
                self.c_of_opponents[self.id_P1] += 1
                self.c_of_opponents[self.id_P2] += 1
                #self.gener_history_freq[self.strat_id_1] += 1
                #self.gener_history_freq[self.strat_id_2] += 1
        if self.debug == True: self.writeData2()

    def duelNPD(self):
        self.duel_fulfilment = False
        while self.duel_fulfilment == False:
            self.tournamentNPD()
            self.min = min(self.c_of_opponents)
            self.id = self.c_of_opponents.index(self.min)
            if self.min == self.num_of_opponents: self.duel_fulfilment = True
            else:
                temp = self.c_of_opponents
                temp1 = self.SUM_with_opponents
                self.ZERO_NPD_structures()
                with open(self.Nstrategies, 'w') as file: pass
                self.c_of_opponents = temp
                self.SUM_with_opponents = temp1
                self.id_N_players = [-1 for i in range(self.players)]
                self.id_N_players[0] = self.id
                self.c_of_opponents[self.id] += 1
                for i in range(1, self.players):
                    id = self.rng.randint(0, self.pop_size - 1)
                    while (id in self.id_N_players) == True: id = self.rng.randint(0, self.pop_size - 1)
                    self.id_N_players[i] = id
                    self.c_of_opponents[id] += 1
                for i in range(self.players):
                    with open(self.Nstrategies, 'a') as file:
                        strats = open(self.strategies, 'r')
                        file.write(strats.readlines()[self.id_N_players[i]])
                        strats.close()
                self.prehistory = [self.rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]
                self.set_N_players_preh()
                self.set_N_players_strat_id()
                self.update_gener_history_freq()

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
                file.write('  %d %.2f %.2f\n' % (self.gen, self.best_fit, self.avg_fit))
            with open('.\\RESULTS\\result_2.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                file.write(' '.join([str(round(self.history_freq[i], 2)) for i in range(len(self.history_freq))]) + '\n')
            with open('.\\RESULTS\\result_3.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                with open(self.strategies, 'r') as file2:
                    line = ' '.join(file2.readlines()[self.fitness.index(self.best_fit)].split(' '))
                    file.write(line)
                    if line.endswith('\n') == False: file.write('\n')
            self.signals.draw1.emit('.\\RESULTS\\result_1.txt')
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
                        file.write('  %d %.2f\n' % (i, freqs[i]))
                self.signals.draw2.emit(path, self.gen)
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
                file.write('  %d %.2f %.2f\n' % (self.gen, self.best_fit, self.avg_fit))
            with open('.\\RESULTS\\result_2N.txt', 'a') as file:
                file.write('  %d ' % self.gen)
                for i in range(len(temp)):
                    file.write('%d %.2f ' % (temp[i][0], temp[i][1]))
                file.write('\n')
            self.signals.draw1.emit('.\\RESULTS\\result_1N.txt')
            if self.hist_freq_show_fulfilment == True:
                path = '.\\RESULTS\\result_2N_' + str(self.gen) + '.txt'
                with open(path, 'w') as file:
                    file.write('# NpPD\n')
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
                        file.write('  %d %.2f\n' % (temp[i][0], temp[i][1]))
                self.signals.draw2.emit(path, self.gen)

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
        with open(self.strategies, 'r') as file:
            for line in file: strats.append(''.join(line.split()))
        for i in range(len(strats)):
            for j in range(len(strats[i])):
                los = self.rng.random()
                if los < self.mutation_prob:
                    if strats[i][j] == '0': strats[i] = strats[i][:j] + '1' + strats[i][j+1:]
                    else: strats[i] = strats[i][:j] + '0' + strats[i][j+1:]
        with open(self.strategies, 'w') as file:
            for i in range(len(strats)):
                line = ' '.join(list(strats[i])) + '\n'
                file.write(line)

    def elitist_fun(self, best_strat):
        strats = list()
        with open(self.strategies, 'r') as file:
            for line in file: strats.append(line[:-1])
        if (best_strat in strats) == False:
            with open(self.strategies, 'w') as file:
                for i in range(len(strats) - 1):
                    line = strats[i] + '\n'
                    file.write(line)
                if best_strat.endswith('\n'): file.write(best_strat)
                else:
                    line = best_strat + '\n'
                    file.write(line)

    def GAoperators(self):
        for i in range(self.num_of_generations):
            self.gen = i + 1
            winners = []
            best_strat = ''
            with open(self.strategies, 'r') as file:
                best = self.fitness.index(max(self.fitness))
                best_strat = file.readlines()[best]
            # tournament selection
            for j in range(self.pop_size):
                winner = self.tournament_fun()
                if (winner in winners) == False: winners.append(winner)
                with open(self.tempstrategies, 'a') as file:
                    strat = open(self.strategies, 'r')
                    line = strat.readlines()[winner]
                    if line.endswith('\n') == False: file.write(line + '\n')
                    else: file.write(line)
                    strat.close()
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
                with open(self.strategies, 'r') as file:
                    children = open(self.childstrategies, 'a')
                    chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    while self.parents_strategies[chosen] != 1: chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    chosen2 = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    while self.parents_strategies[chosen2] != 1 or chosen2 == chosen:
                        chosen2 = self.rng.randint(0, (len(self.parents_strategies) - 1))
                    strat1 = ''.join(file.readlines()[chosen].split())
                    file.seek(0)
                    strat2 = ''.join(file.readlines()[chosen2].split())
                    (strat1, strat2) = self.crossover_fun(strat1, strat2)
                    children.write(' '.join(list(strat1)) + '\n')
                    children.write(' '.join(list(strat2)) + '\n')
                    new_pop_size += 2
                    if new_pop_size == (self.pop_size - 1):
                        chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                        while self.parents_strategies[chosen] != 1: chosen = self.rng.randint(0, (len(self.parents_strategies) - 1))
                        file.seek(0)
                        children.write(file.readlines()[chosen])
                        new_pop_size += 1
                    children.close()
            # mutation
            with open(self.strategies, 'w') as file:
                children = open(self.childstrategies, 'r')
                for line in children:
                    if line.endswith('\n') == True: file.write(line)
                    else: file.write(line + '\n')
                children.close()
            self.mutation_fun()
            # elitist
            if self.elitist == True: self.elitist_fun(best_strat)
            if self.debug == True: self.writeData4()
            with open(self.tempstrategies, 'w') as file: pass
            with open(self.childstrategies, 'w') as file: pass
            if self.players == 2:
                self.SUM_with_opponents = [0 for i in range(self.pop_size)]
                self.c_of_opponents = [0 for i in range(self.pop_size)]
                self.history_freq = [0 for i in range(len(self.P1_strat))]
                self.duel2PD()
            elif self.players != 2:
                self.SUM_with_opponents = [0 for i in range(self.pop_size)]
                self.c_of_opponents = [0 for i in range(self.pop_size)]
                self.history_freq = list()
                self.duelNPD()
            self.fitnessStatistics()

    @Slot()
    def run(self):
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
        self.signals.end.emit()
