# This Python file uses the following encoding: utf-8
# This file consists of code which is used to solve Prisoner's Dilemma.
# It is used by mainwindow.py

from PySide6.QtCore import QObject, QRunnable, Slot, Signal
from statistics import mean
import tempfile, random, sys, math

maxrange = 9999999999999999                     # max range of random seed
filename = ''                                   # name of file to open

class PrisonersSignals(QObject):
    show = Signal(str)
    file = Signal(str)

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
        self.freq_gen_start = data[20]
        self.delta_freq = data[21]
        self.debug = data[22]
        self.directory = tempfile.TemporaryDirectory()
        self.strategies = self.directory.name + '\\strat.txt'
        if self.num_of_runs == 1 and self.players == 2:
            self.createResult1()
            self.createResult2()
            self.createResult3()

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
            file.write('#  1\t2\t\t3\n')
            file.write('# gen\tbest_fit\tavg_fit\n')

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
            rng = random.Random(self.seed)
            with open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(self.players ** (2 * self.prehistory_l)):
                        los = rng.random()
                        if los < self.prob_of_init_C: file.write('1 ')
                        else: file.write('0 ')
                    file.write('\n')
            self.prehistory = [rng.randint(0, 1) for i in range(2 * self.prehistory_l)]
        elif self.players != 2 and self.pop_size > 4:
            rng = random.Random(self.seed)
            with open(self.strategies, 'w') as file:
                for i in range(self.pop_size):
                    for j in range(2 ** (self.prehistory_l + self.prehistory_l * math.ceil(math.log2(self.players)))):
                        los = rng.random()
                        if los < self.prob_of_init_C: file.write('1 ')
                        else: file.write('0 ')
                    file.write('\n')
            self.prehistory = [rng.randint(0, 1) for i in range(self.prehistory_l * self.players)]

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

    def ZERO_2PD_structures(self):
        self.SUM_with_opponents = [0 for i in range(self.pop_size)]
        self.c_of_opponents = [0 for i in range(self.pop_size)]
        self.gener_history_freq = list()
        self.P1_strat = list()
        self.P2_strat = list()
        self.history_freq = list()
        self.fitness = [0 for i in range(self.pop_size)]

    def ZERO_NPD_structures(self):
        self.id_N_players = [0 for i in range(self.players)]
        self.N_players_strategies = [0 for i in range(self.players)]
        self.N_players_preh = [0 for i in range(self.players)]
        self.curr_action_N_players = [0 for i in range(self.players)]
        self.num_of_c_neighb_N_players = [0 for i in range(self.players)]
        self.payoff_N_players = [0 for i in range(self.players)]
        self.N_players_strat_id = [0 for i in range(self.players)]
        self.SUM_with_opponents = [0 for i in range(self.pop_size)]
        self.c_of_opponents = [0 for i in range(self.pop_size)]
        self.gener_history_freq = list()
        self.history_freq = list()
        self.fitness = [0 for i in range(self.pop_size)]

    def toDecimal(self, data):
        data = [str(data[i]) for i in range(len(data))]
        data = '0b' + ''.join(data)
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
        self.gener_history_freq[self.strat_id_1 - 1] += 1
        self.gener_history_freq[self.strat_id_2 - 1] += 1
        self.history_freq = [0 for i in range(len(self.P1_strat))]
        if self.num_of_runs == 1:
            with open('.\\RESULTS\\result_2.txt', 'a') as file:
                file.write('#\tfrequency of game histories\n')
                file.write('# ' + '\t'.join([str(i) for i in range(len(self.P1_strat) + 1)]))
                file.write('\n# gen\t' + '\t'.join([str(i) for i in range(len(self.P1_strat))]) + '\n')
            with open('.\\RESULTS\\result_3.txt', 'a') as file:
                file.write('#\tbest strategy\n')
                file.write('# gen\t' + '\t'.join([str(i) for i in range(len(self.P1_strat))]) + '\n')

    def inic_players_NpPD(self):
        for i in range(self.players):
            self.id_N_players[i] = i
            with open(self.strategies, 'r') as file:
                lines = file.readlines()
                self.N_players_strategies[i] = ''.join(lines[i][:-1].split(' '))
            self.c_of_opponents[i] += 1
            # do dokończenia
            sys.exit(1)

    def functions_2PD(self):
        self.ZERO_2PD_structures()
        self.inic_players_2pPD()
        if self.debug == True: self.writeData2()

    def functions_NPD(self):
        self.ZERO_NPD_structures()
        self.inic_players_NpPD()
        if self.debug == True: pass

    def tournament2PD(self):
        for i in range(self.num_of_tournaments):
            self.curr_action_P1 = self.P1_strat[self.strat_id_1 - 1]
            self.curr_action_P2 = self.P2_strat[self.strat_id_2 - 1]
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
            self.gener_history_freq[self.strat_id_1 - 1] += 1
            self.gener_history_freq[self.strat_id_2 - 1] += 1
            if self.debug == True: self.writeData3(i + 1)

    def duel2PD(self):
        self.duel_fulfilment = False
        while self.duel_fulfilment == False:
            self.tournament2PD()
            self.min = min(self.c_of_opponents)
            self.id = self.c_of_opponents.index(self.min)
            if self.min == self.num_of_opponents: self.duel_fulfilment = True
            else:
                temp = self.c_of_opponents
                temp1 = self.history_freq
                self.ZERO_2PD_structures()
                self.c_of_opponents = temp
                self.history_freq = temp1
                self.id_P1 = self.id
                self.id_P2 = random.randint(0, self.pop_size - 1)
                while self.id_P2 == self.id_P1: self.id_P2 = random.randint(0, self.pop_size - 1)
                with open(self.strategies, 'r') as file:
                    lines = file.readlines()
                    self.P1_strat.extend([int(lines[self.id_P1][i]) for i in range(len(lines[self.id_P1])) if lines[self.id_P1][i] != ' ' and lines[self.id_P1][i] != '\n'])
                    self.P2_strat.extend([int(lines[self.id_P2][i]) for i in range(len(lines[self.id_P2])) if lines[self.id_P2][i] != ' ' and lines[self.id_P2][i] != '\n'])
                self.prehistory = [random.randint(0, 1) for i in range(len(self.prehistory))]
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
                self.gener_history_freq[self.strat_id_1 - 1] += 1
                self.gener_history_freq[self.strat_id_2 - 1] += 1
        if self.debug == True: self.writeData2()

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
            pass
        if self.players == 2:
            with open('.\\RESULTS\\result_1.txt', 'a') as file:
                file.write('  %d\t%.2f\t\t%.2f\n' % (self.gen, self.best_fit, self.avg_fit))
            with open('.\\RESULTS\\result_2.txt', 'a') as file:
                file.write('  %d\t' % self.gen)
                file.write('\t'.join([str(round(self.history_freq[i], 2)) for i in range(len(self.history_freq))]) + '\n')
            with open('.\\RESULTS\\result_3.txt', 'a') as file:
                file.write('  %d\t' % self.gen)
                with open(self.strategies, 'r') as file2:
                    line = '\t'.join(file2.readlines()[self.fitness.index(self.best_fit)].split(' '))
                    file.write(line + '\n')
        else:
            pass


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
            #self.GAoperators()
        else:
            pass
            #self.duelNPD()
            #self.fitnessStatistics()
            #self.GAoperators()
