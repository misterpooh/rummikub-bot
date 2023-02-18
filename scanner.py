from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from tiles import Tiles

class Scanner:
    """
    Scans the screen to detect all tiles and stores the location
    """
    def locate_all(path, confidence=0.9, distance=10):
        distance = pow(distance, 2)
        elements = []
        for element in pyautogui.locateAllOnScreen(path, confidence=confidence):
            if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
                elements.append(element)
        return elements
    print("Scanning")
    print("1")
    for i in locate_all(Tiles.BLACK_ONE.image, confidence=0.9):
        print(i)
    print("2")
    for i in locate_all(Tiles.BLACK_TWO.image, confidence=0.9):
        print(i)
    print("3")
    for i in locate_all(Tiles.BLACK_THREE.image, confidence=0.95):
        print(i)
    print("4")
    for i in locate_all(Tiles.BLACK_FOUR.image, confidence=0.9):
        print(i)
    print("5")
    for i in locate_all(Tiles.BLACK_FIVE.image, confidence=0.9):
        print(i)
    print("6")
    for i in locate_all(Tiles.BLACK_SIX.image, confidence=0.9):
        print(i)
    print("7")
    for i in locate_all(Tiles.BLACK_SEVEN.image, confidence=0.9):
        print(i)
    print("8")
    for i in locate_all(Tiles.BLACK_EIGHT.image, confidence=0.9):
        print(i)
    print("9")
    for i in locate_all(Tiles.BLACK_NINE.image, confidence=0.9):
        print(i)
    print("10")
    for i in locate_all(Tiles.BLACK_TEN.image, confidence=0.9):
        print(i)
    print("11")
    for i in locate_all(Tiles.BLACK_ELEVEN.image, confidence=0.9):
        print(i)
    print("12")
    for i in locate_all(Tiles.BLACK_TWELVE.image, confidence=0.9):
        print(i)
    print("13")
    for i in locate_all(Tiles.BLACK_THIRTEEN.image, confidence=0.9):
        print(i)
    print("Joker")
    for i in locate_all(Tiles.BLACK_JOKER.image, confidence=0.5):
        print(i)
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    
    print(currentMouseX)
    print(currentMouseY)