import os
import time
import pyautogui

import wx
from PIL import ImageGrab
from notifiers import get_notifier


def switch_from_cs_window():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


def get_button_coordinates(x_scale, y_scale):
    coordinates_colours = []
    all_colours = []
    coords = []

    image = ImageGrab.grab()

    for x in range(x_scale):

        for y in range(y_scale):
            coords.append((x, y))
            colour = image.getpixel((x, y))
            all_colours.append(colour)

            if colour == button_colour:
                coordinates_colours.append((x, y))

    return coordinates_colours


def get_center_of_the_button(button_coordinates: list):
    left_border = sorted(button_coordinates, key=lambda coord_colour: coord_colour[0])[0]
    right_border = sorted(button_coordinates, key=lambda coord_colour: coord_colour[0], reverse=True)[0]
    upper_border = sorted(button_coordinates, key=lambda coord_colour: coord_colour[1])[0]
    bottom_border = sorted(button_coordinates, key=lambda coord_colour: coord_colour[1], reverse=True)[0]
    button_center_horizontal = int(left_border[0] + (right_border[0] - left_border[0]) / 2)
    button_center_vertical = int(upper_border[1] + (bottom_border[1] - upper_border[1]) / 2)
    button_center = (button_center_horizontal, button_center_vertical)

    # pyautogui.moveTo(*left_border)
    # time.sleep(0.5)
    # pyautogui.moveTo(*right_border)
    # time.sleep(0.5)
    # pyautogui.moveTo(*upper_border)
    # time.sleep(0.5)
    # pyautogui.moveTo(*bottom_border)
    # time.sleep(0.5)
    # pyautogui.moveTo(*button_center)
    # time.sleep(0.5)
    #
    # print(f'left_border: {left_border}\n'
    #       f'right_border: {right_border}\n'
    #       f'upper_border: {upper_border}\n'
    #       f'bottom_border: {bottom_border}\n'
    #       f'center: {button_center}')

    return button_center


def check_existing_of_pixels_with_button_colour(x_scale, y_scale):
    image = ImageGrab.grab()
    for x in range(x_scale):
        colours = []

        for y in range(y_scale):

            colour = image.getpixel((x, y))
            colours.append(colour)

            if colour != button_colour:
                pass
            else:
                print('Found button colour!')
                return True

    return False


button_colour = (76, 175, 80)

app = wx.App(False)
width, height = wx.GetDisplaySize()
print(width, height)
telegram = get_notifier('telegram')


time.sleep(4)

image = ImageGrab.grab()
start_colour_of_screen_center = image.getpixel((width / 2, height / 2))
# switch_from_cs_window()

while not check_existing_of_pixels_with_button_colour(width, height):
    pass

button_coordinates: list = get_button_coordinates(width, height)
button_center = get_center_of_the_button(button_coordinates)
pyautogui.click(*button_center, interval=0.5, clicks=5)
telegram.notify(message=f'Bro, i just click the button. I hope other players will accept game request!', token=os.environ['TELEGRAM_KEY'],
                chat_id=os.environ['TELEGRAM_CHAT_ID'])

# switch_from_cs_window()
time.sleep(25)
colour_of_screen_center = image.getpixel((width / 2, height / 2))
if colour_of_screen_center == start_colour_of_screen_center:
    telegram.notify(message=f'Some idiot did`nt press join button...', token=os.environ['TELEGRAM_KEY'],
                    chat_id=os.environ['TELEGRAM_CHAT_ID'])

else:
    telegram.notify(message=f'All players excepted join request 2 the game! Get ready to play!', token=os.environ['TELEGRAM_KEY'],
                    chat_id=os.environ['TELEGRAM_CHAT_ID'])

switch_from_cs_window()
