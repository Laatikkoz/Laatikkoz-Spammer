import os
import pyautogui, time

print("""
█░░ ▄▀█ ▄▀█ ▀█▀ █ █▄▀ █▄▀ █▀█   █▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
█▄▄ █▀█ █▀█ ░█░ █ █░█ █░█ █▄█   ▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄""")


time.sleep(1.5)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

clearConsole()

teksti = input("Spam Text: ")


input("Press Enter When You Are Ready")


while True:
    pyautogui.typewrite(teksti)
    pyautogui.press("enter")


