import pyautogui, keyboard
from time import sleep

a = input("Mensaje que deseas spammear: \n")
print("Presione 'p' para parar")

while True:
    sleep(2)
    pyautogui.typewrite(a)
    pyautogui.press("enter")
    if keyboard.is_pressed("p"):
        exit(0)