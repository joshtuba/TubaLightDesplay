# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import random
import board
import adafruit_dotstar as dotstar
import neopixel
from math import floor

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
dots = dotstar.DotStar(board.GP6, board.GP5, 30, brightness=0.2)

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 60

ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(board.GP0, num_pixels, pixel_order=ORDER)
pixels.brightness = 0.25


# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32





# MAIN LOOP
n_dots = len(dots)
timedelay = 0.025


while True:
    # Fill each dot with a random color
    #for dot in range(n_dots*2):
    #    dots[floor(dot/2)] = (random_color(), random_color(), random_color())
    #    #pixels[dot] =(random_color(),random_color(), random_color(), 0)
    #    time.sleep(timedelay)
    ##time.sleep(0.25)
    #for dot60 in range (num_pixels/2):
    #    pixels[dot60*2] = (random_color(),random_color(), random_color(), 0)
    #    time.sleep(timedelay*2)

    #red
    for dot in range(n_dots):
        dots[floor(dot)] = (255, 0, 0)
        pixels[dot*2] = (0,255, 0, 0) # make 60s white
        time.sleep(timedelay)
    for dot in range(n_dots):
        dots[floor(dot)] = (255, 255, 255)
        pixels[dot*2] = (255,0, 0, 0) # make 60s white
        time.sleep(timedelay)
    for dot in range(n_dots):
        dots[floor(dot)] = (0, 255, 0)
        pixels[dot*2] = (255,255, 255, 0) # make 60s white
        time.sleep(timedelay)



    #for dot in range(n_dots):
    #    dots[-floor(dot)] = (0, 255, 0)
    #    pixels[-dot*2] = (255,255, 255, 0) # make 60s white
    #    time.sleep(timedelay)
    #time.sleep(0.25)
    #for dot in range(n_dots):
    #    dots[-floor(dot)] = (255, 255, 255)
    #    pixels[-dot*2] = (255,0, 0, 0) # make 60s white
     #   time.sleep(timedelay)
    #for dot in range(n_dots):
    #    dots[floor(-dot)] = (255, 0, 0)
    #    pixels[-dot*2] = (0,255, 0, 0) # make 60s white
    #    time.sleep(timedelay)
