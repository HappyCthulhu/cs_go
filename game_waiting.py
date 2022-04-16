# https://www.codegrepper.com/code-examples/python/get+color+of+pixel+on+screen+python
# https://stackoverflow.com/questions/4331573/is-it-possible-to-get-the-color-of-a-particular-pixel-on-the-screen-with-its-x
from PIL import ImageGrab
import time
time.clock()
image = ImageGrab.grab()
for y in range(0, 100, 10):
    for x in range(0, 100, 10):
        color = image.getpixel((x, y))
print(time.clock())