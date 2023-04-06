from pynput.mouse import Listener
import os

izq = 0
der = 0

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

def stopScript():
    os._exit(0)

def on_click(x, y, button, pressed):
    global izq
    global der

    if button == button.left and pressed:
        izq+=1
    if button == button.right and pressed:
        der+=1

    clear_console()
    print(f"Click izquierdo {izq}")
    print(f"Click derecho {der}")

listener = Listener(on_click=on_click)
listener.start()
listener.join()