# This Python file uses the following encoding: utf-8
# This file consists of code which is used to solve Prisoner's Dilemma.
# It is used by mainwindow.py

from PySide6.QtCore import QRunnable, Slot

class Prisoners(QRunnable):
    def __init__(self):
        super().__init__(self)
        print('Test')

    @Slot()
    def run(self):
        while True:
            print('abc')
