import pyautogui as pyautogui

with open('commands.txt', 'r') as file:
    commands = file.read().splitlines()

for command in commands:
    pyautogui.typewrite(command)
    pyautogui.press('enter')

