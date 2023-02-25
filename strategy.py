from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from tile import Tile
from constants import Constants
import datetime
from scanner import Scanner
from interactor import Interactor
class Strategy:
    COLORS = ["black", "blue", "red", "orange"]
    def __init__(self):
        self.scanner = Scanner()
        self.interactor = Interactor(self.scanner)
        self.initialized = False

    def run(self):
        while True: # loop until game ends
            if self.scanner.is_player_turn():
                self.scanner.locate_game_window()
                self.scanner.scan_board_tiles()
                self.interactor.click_sort777()
                self.scanner.scan_player_tiles()
                self.make_move()
    
    def has_tile(self, number, color, board):
        if board[number][color]:
            return True
        return False
    
    def grab_tile(self, number, color, board) -> Tile:
        if self.has_tile(number, color, board):
            return board[number][color].pop()
        return None
    
    def put_tile(self, t, board):
        board[int(t.get_number())][str(t.get_color())].append(t)
    
    def get_size(self, board):
        # Returns the total number of tiles on board
        count = 0
        for i in range(1, len(board)):
            for color in self.COLORS:
                count += len(board[i][color])
        count += len(board["joker"])
    
    def get_size(self, number, color, board):
        # Returns the total number of given tile on board
        return len(board[number][color])
    
    def initialize(self):
        total = 0
        matches = []
        for number in range(13, 0, -1): # iterate all possible tiles
            for color in self.COLORS:
                if self.has_tile(number, color, self.scanner.player_tiles):
                    # Check for Color Match
                    color_match = self.grab_color_match(number, color, self.scanner.player_tiles)
                    if number * len(color_match) >= 30:
                        self.move_tiles_to_board(color_match)
                        self.interactor.end_move()
                        self.initialized = True
                    elif (number * len(color_match)) + total >= 30:
                        matches.append(color_match)
                        self.move_matches_to_board(matches)
                    else:
                        total += number * len(color_match)
                        matches.append(color_match)
                    
        if not self.initialized:
            self.interactor.take_tile()

    def get_first_tile(self, match):
        lowest = None
        for t in match:
            if not lowest:
                lowest = t
            elif t.get_y() <= lowest.get_y() and t.get_x() < lowest.get_x():
                lowest = t
        return lowest

    def move_matches_to_board(self, matches):
        for match in matches:
            first = self.get_first_tile(match)
            self.interactor.move_match(first.get_x(), first.get_y(), self.scanner.board_top_left[0], self.scanner.board_top_left[1], len(match))
        return True
        
    def move_tiles_to_board(self, tiles):
        for t in tiles:
            self.move_tile_to_board(t)                    
    
    def move_tile_to_board(self, t):
        self.move_tile(t, self.scanner.board_top_left[0], self.scanner.board_top_left[1])

    def move_tile(self, t, x, y):
        self.interactor.move_tile(t.get_x(), t.get_y(), x, y)

    
    def grab_color_match(self, number, color, board) -> list[Tile]:
        grab = []
        for xcolor in self.COLORS:
            if xcolor != color:
                if self.has_tile(number, xcolor, self.scanner.player_tiles):
                    grab.append(self.grab_tile(number, xcolor, board))
        if len(grab) >= 2: # has a match
            return grab
        for t in grab: # put back tiles
            self.put_tile(t, board)
        return []
    

                        
    def make_move(self):
        if not self.initialized:
            self.initialize()
        #else:
        #    if self.get_size(self.scanner.player_tiles) > 2:
        #        for i in range(1,14):
        #            for color in self.COLORS:
        #                break

                


strategy = Strategy()
strategy.run()


