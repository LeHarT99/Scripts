import webbrowser
from time import sleep

link = input("Link que quieres abrir: \n")

while True:
    sleep(0.5)
    webbrowser.open_new_tab(link)