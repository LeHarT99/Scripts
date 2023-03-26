import pyautogui
from time import sleep
import random

pyautogui.FAILSAFE = False

while True:
    sleep(0.1)
    pyautogui.rightClick(int(random.random()*1920), int(random.random()*1920))
