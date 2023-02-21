from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from tiles import Tiles
import datetime

class Interactor:
    def __init__(self, scanner):
        self.scanner = scanner

    def click_sort777(self):
        sort777_loc = self.scanner.locate_sort777()
        pyautogui.click(sort777_loc.x, sort777_loc.y)
    
