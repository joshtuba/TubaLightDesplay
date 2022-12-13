# This is the working example code for the dotstar strip


# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import random
import board
import adafruit_dotstar as dotstar


# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
#dots = dotstar.DotStar(board.SPI0_CLK, board.SPI0_TX, 30, brightness=0.2)

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# dots = dotstar.DotStar(board.D6, board.D5, 30, brightness=0.2)
dots = dotstar.DotStar(board.GP6, board.GP5, 30, brightness=0.2)


# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32


# MAIN LOOP
n_dots = len(dots)
while True:
    # Fill each dot with a random color
    for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())
    time.sleep(0.25)
