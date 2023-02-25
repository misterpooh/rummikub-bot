from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from constants import Constants
import datetime

class Interactor:
    def __init__(self, scanner):
        self.scanner = scanner

    def click_sort777(self):
        sort777_loc = self.scanner.locate_sort777()
        pyautogui.click(sort777_loc.x, sort777_loc.y)
    
    def move_tile(self, tile_x, tile_y, target_x, target_y):
        pyautogui.moveTo(tile_x, tile_y)
        pyautogui.dragTo(target_x, target_y, button="left")
    
    def move_match(self, tile_x, tile_y, target_x, target_y, count):
        pyautogui.moveTo(tile_x, tile_y)
        pyautogui.mouseDown()
        pyautogui.sleep(count/2)
        pyautogui.moveTo(target_x, target_y)
        pyautogui.mouseUp()
    
    def end_move(self):
        end_turn_loc = self.scanner.locate_end_turn()
        pyautogui.click(end_turn_loc.x, end_turn_loc.y)

    def take_tile(self):
        take_tile_loc = self.scanner.locate_take_tile()
        pyautogui.click(take_tile_loc.x, take_tile_loc.y)
