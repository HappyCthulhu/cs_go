import os
import time
import pyautogui
import wx
from notifiers import get_notifier

# TODO: через 30 секунд прислать мне скрин экрана
# TODO: сделать так, чтоб, если катка не состоялась, он продолжал отслеживать экран

def get_pixel_colour(i_x, i_y):
    import win32gui
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def check_presense_of_green_button():
    time.sleep(1)

    if start_colour != get_pixel_colour(half_width, half_height):
        print('Button present!')
        return True
    else:
        print('Still waiting...')
        return False


app = wx.App(False)
width, height = wx.GetDisplaySize()

telegram = get_notifier('telegram')

half_width = int(width / 2)
half_height = int(height / 2)

time.sleep(3)

start_colour = get_pixel_colour(half_width, half_height)
print(f'Start colour is: {start_colour}')

while not check_presense_of_green_button():
    pass

print(f'Button colour is: {get_pixel_colour(half_width, half_height)}')
pyautogui.click(half_width, half_height, interval=0.5, clicks=5)
print('Clicked the button!')

telegram.notify(message=f'Bro, i just click the button. Get ready to play!', token=os.environ['TELEGRAM_KEY'],
                chat_id=os.environ['TELEGRAM_CHAT_ID'])
