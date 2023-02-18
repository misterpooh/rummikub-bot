from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import tiles

class Scanner:
    """
    Scans the screen to detect all tiles and stores the location
    """
    pyautogui.locateAllOnScreen('png')