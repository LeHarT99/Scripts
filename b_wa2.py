import pyautogui, webbrowser
from time import sleep

#sleep(10)

#pyautogui.click(500, 500)

a = input("Mensaje que deseas spammear: \n")

while True:
    sleep(2)
    pyautogui.typewrite(a)
    pyautogui.press("enter")