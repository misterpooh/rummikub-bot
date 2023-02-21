from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from tiles import Tiles
import datetime
from scanner import Scanner
from interactor import Interactor
class Strategy:
    def __init__(self):
        self.scanner = Scanner()
        self.interactor = Interactor(self.scanner)

    def run(self):
        while True: # loop until game ends
            if self.scanner.is_player_turn():
                self.scanner.locate_game_window()
                self.scanner.scan_board_tiles()
                self.interactor.click_sort777()
                self.scanner.scan_player_tiles()
                self.make_move()

    def make_move(self):
        return


strategy = Strategy()
strategy.run()


