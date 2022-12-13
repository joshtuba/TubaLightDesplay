import board
import neopixel
import time


def steppingLED():
    #num_pixels = 3
    #ORDER = neopixel.GRBW
    #pixels = neopixel.NeoPixel(board.GP0, num_pixels, pixel_order=ORDER)
    print("stepping LED function")
    myIndex = 0
    preIndex = -1
    prepreIndex = -1
    a = 1
    while True:

        #pixels[prepreIndex] =(0,0,0,0)
        pixels[preIndex] =(0,0,0,0)
        pixels[myIndex] = (0, 255, 0, 0)

        prepreIndex = preIndex
        preIndex = myIndex
        myIndex += a

        #print("myIndex: " + str(myIndex))
        #print("preIndex: " + str(preIndex))
        #print("")

        time.sleep(0.05)

        if (myIndex >= num_pixels-1) or (myIndex <= 0):
            a *= -1

