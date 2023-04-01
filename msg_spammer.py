import pyautogui, keyboard
from time import sleep

a = input("Mensaje que deseas spammear: \n")
sleep(5)

while True:
    pyautogui.typewrite(a)
    pyautogui.press("enter")
    if keyboard.is_pressed("p"):
        exit(0)