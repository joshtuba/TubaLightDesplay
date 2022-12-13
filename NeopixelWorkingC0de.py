# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
NeoPixel example for Pico. Turns the NeoPixels red.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import board
import neopixel
import time

print("I've restarted")

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 10

ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(board.GP0, num_pixels, pixel_order=ORDER)
pixels.brightness = 0.25

pixels.fill((0, 0, 0, 0))
pixels.show()
time.sleep(1)

def steppingLED():
    print("stepping LED function")
    myIndex = 0
    preIndex = -1
    prepreIndex = -1
    a = 1
    while True:

        #pixels[prepreIndex] =(0,0,0,0)
        pixels[preIndex] =(0,0,0,0)
        pixels[myIndex] = (255, 0, 0, 0)

        prepreIndex = preIndex
        preIndex = myIndex
        myIndex += a

        #print("myIndex: " + str(myIndex))
        #print("preIndex: " + str(preIndex))
        #print("")

        time.sleep(0.1)

        if (myIndex >= num_pixels-1) or (myIndex <= 0):
            a *= -1



def rainbow():
    maxBright = 255

    r = maxBright
    g = 0
    b = 0

    rchange = 1
    gchange = 0
    bchange = 0

    pixels.fill((r, g, b, 0))
    pixels.show()
    time.sleep(2)

    while True:
        pixels.fill((r, g, b, 0))
        pixels.show()
        r += rchange
        b += bchange
        g += gchange


        if (r >= maxBright) and (b <= 0):
            rchange = 0
            gchange = 1
            bchange = 0 ###
        if (g >= maxBright) and (r >= maxBright):
            rchange = -1
            gchange = 0
            bchange = 0 ###
        if (g >= maxBright) and (r <= 0):
            rchange = 0
            gchange = 0 ###
            bchange = 1
        if (g >= maxBright) and (b >= maxBright):
            rchange = 0 ###
            gchange = -1
            bchange = 0
        if (b >= maxBright) and (g <= 0):
            rchange = 1
            gchange = 0
            bchange = 0 ###
        if (r >= maxBright) and (b >= maxBright):
            rchange = 0
            gchange = 0 ###
            bchange = -1
        #if (r >= maxBright) and (b <= 0):
        #    rchange = 0
        #    #
        #    bchange = 0

        time.sleep(0.01)

##############################

def rainbowHEX():
    color = 0xFFFFFF
    while True:
        pixels.fill(color)
        pixels.show()

        color -= 1
        #print(color)



##################################

#rainbowHEX()
rainbow()
#steppingLED()

while True:
    pixels[0] =(225, 0, 0, 0)
    pixels.show()
    time.sleep(1)
    pixels[0] = 0
    pixels.show()
    time.sleep(1)

    #pixels.fill((225, 0, 0, 0))
    #pixels.show()

    #steppingLED()


    #pixels.fill((255,0,0,0))
    #pixels.fill((0,255,0,0))
    #pixels.show
    #time.sleep(0.1)
    #pixels.fill((0,0,0,0))
    #time.sleep(0.1)

################################################################
# Write your code here :-)
