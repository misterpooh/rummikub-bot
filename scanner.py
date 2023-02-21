from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from tiles import Tiles
import datetime

class Scanner:
    """
    Scans the screen to detect all tiles and stores the location
    """
    GAME_WIDTH = 900
    GAME_HEIGHT = 506
    COLORS = ["black", "blue", "red", "orange"]
    def __init__(self):
        self.game_top_left = None
        self.game_top_left = self.locate_game_window() # (x,y)
        self.initialized = False
        self.board_top_left = None
        self.player_top_left = None
        self.board_tiles = {"joker": []}
        self.player_tiles = {"joker": []}
        for i in range(1, 14):
            self.board_tiles[i] = {"black":[], "blue":[], "red":[], "orange":[]}
            self.player_tiles[i] = {"black":[], "blue":[], "red":[], "orange":[]}

    def locate_player(self, height=GAME_HEIGHT, width=GAME_WIDTH):
        if not self.game_top_left:
            self.locate_game_window()
        player_board_loc = pyautogui.locateOnScreen(Tiles.PLAYER_TILE.image, confidence=0.95, region=tuple([self.game_top_left[0], self.game_top_left[1], self.GAME_WIDTH, self.GAME_HEIGHT]))
        return (player_board_loc.left, player_board_loc.top)
    
    def locate_board(self):
        if not self.game_top_left:
            self.locate_game_window()
        game_board_loc = pyautogui.locateOnScreen(Tiles.BOARD_TILE.image, confidence=0.95, region=tuple([self.game_top_left[0], self.game_top_left[1], self.GAME_WIDTH, self.GAME_HEIGHT]), grayscale=True)
        return (game_board_loc.left, game_board_loc.top)
    
    def click_sort777(self):
        if not self.game_top_left:
            self.locate_game_window()
        sort_button_loc = pyautogui.locateOnScreen(Tiles.SORT777_BUTTON.image, confidence=0.95, region=tuple([self.game_top_left[0], self.game_top_left[1], self.GAME_WIDTH, self.GAME_HEIGHT]), grayscale=True)
        sort_button_center = pyautogui.center(sort_button_loc)
        pyautogui.click(sort_button_center.x, sort_button_center.y)

    def is_player_turn(self):
        if not self.game_top_left:
            self.locate_game_window()
        turn_loc = pyautogui.locateOnScreen(Tiles.TURN.image, confidence=0.9, region=tuple([self.game_top_left[0], self.game_top_left[1], self.GAME_WIDTH, self.GAME_HEIGHT]), grayscale=True)
        if turn_loc: 
            cross_button = pyautogui.center(turn_loc)
            if pyautogui.pixelMatchesColor(int(cross_button.x), int(cross_button.y), (255, 151, 40)):
                print("True")
                return True
        print("False")
        #print(pyautogui.pixel(int(cross_button.x), int(cross_button.y)))
        return False
    

    def locate_all(self, path, confidence=0.9, distance=10 , top_left=None):
        distance = pow(distance, 2)
        elements = []
        if top_left:
            game_window = tuple([top_left[0], top_left[1], top_left[2], top_left[3]])
            for element in pyautogui.locateAllOnScreen(path, confidence=confidence, region=game_window):
                if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
                    elements.append(element)
        else:
            for element in pyautogui.locateAllOnScreen(path, confidence=confidence):
                if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
                    elements.append(element)
        return elements

    def locate_game_window(self, height=GAME_HEIGHT, width=GAME_WIDTH):
        #locate game corner
        if self.game_top_left:
            top_left = self.game_top_left
            corner_img_loc = pyautogui.locateOnScreen(Tiles.GAME_CORNER.image, confidence=0.9, region=tuple([top_left[0]+width-108, top_left[1], 109, 45]), grayscale=True)
            if not corner_img_loc:
                corner_img_loc = pyautogui.locateOnScreen(Tiles.GAME_CORNER.image, confidence=0.9, grayscale=True)
                top_right = (corner_img_loc.left + corner_img_loc.width , corner_img_loc.top)
                top_left = (top_right[0] - width, top_right[1])
        else:
            corner_img_loc = pyautogui.locateOnScreen(Tiles.GAME_CORNER.image, confidence=0.9, grayscale=True)
            top_right = (corner_img_loc.left + corner_img_loc.width , corner_img_loc.top)
            top_left = (top_right[0] - width, top_right[1])
        self.game_top_left = (top_left[0], top_left[1], self.GAME_WIDTH, self.GAME_HEIGHT)        

    def scan_board_tiles(self):
        if not self.board_top_left:
            self.board_top_left = self.locate_board()
        if not self.player_top_left:
            self.player_top_left = self.locate_player()
        board_x = self.board_top_left[0]
        board_y = self.board_top_left[1]
        player_x = self.player_top_left[0]
        player_y = self.player_top_left[1]
        self.scan_all_tiles(self.board_tiles,loc=tuple((board_x, board_y, self.GAME_WIDTH - (self.game_top_left[0] - board_x), player_y - board_y)))
    
    def scan_player_tiles(self):
        if not self.player_top_left:
            self.player_top_left = self.locate_player()
        player_x = self.player_top_left[0]
        player_y = self.player_top_left[1]
        self.scan_all_tiles(self.player_tiles, loc=tuple((player_x, player_y, self.GAME_WIDTH - (player_x - self.game_top_left[0]), self.GAME_HEIGHT - (player_y - self.game_top_left[1]))))
    
    def scan_all_tiles(self, storage, loc=None):
        #TODO: scan speed optimization scan entire game once and sort/store into board_tiles
        # and player_tiles based on x,y position (instead of scanning individually twice)
        self.locate_game_window()
        if not loc:
            loc = self.game_top_left
        start_time = datetime.datetime.now()
        self.click_sort777()
        for k in range(4):
            #print("Scanning " + str(self.COLORS[k].title()))
            for j in range(1,14): 
                #print(j)
                for i in self.locate_all(Tiles[self.COLORS[k].upper() + "_" + str(j)].image, confidence=0.9, top_left=loc):
                    storage[j][self.COLORS[k]].append(i)
            if k == 0 or k == 2:
                for i in self.locate_all(Tiles[self.COLORS[k].upper() + "_JOKER"].image, confidence=0.5, top_left=loc):
                    storage["joker"].append(i)
        time_elapsed = datetime.datetime.now() - start_time
        print("Completed in " + str(
            time_elapsed))

#locate_game_window()
scanner = Scanner()
#scanner.scan_all_tiles()
scanner.is_player_turn()
scanner.scan_board_tiles()
scanner.scan_player_tiles()
#print("Second scan")
#scanner.scan_all_tiles()
#print(scanner.locate_board())
#print(scanner.locate_player())
#print_mouse_pos()
print("board tiles")
print(scanner.board_tiles)
print("player tiles")
print(scanner.player_tiles)
def print_mouse_pos():
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    print(currentMouseX)
    print(currentMouseY)