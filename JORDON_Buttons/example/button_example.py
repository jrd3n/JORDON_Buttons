import time
from lib.JORDON_Buttons.JORDON_ButtonV2 import Buttons
from lib.neopixel import NeoPixel
import board

pad = Buttons()

while True:
    #global PixelNumber
    pad.refresh()

    if pad.A() == "PRESSED":
        print("A")

    if pad.B() == "PRESSED":
        print("B")

    if pad.UP() == "PRESSED":
        print("UP")
        #BrightnessPlus()
    if pad.DOWN() == "PRESSED":
        print("DOWN")
        #BrightnessMinus()
    if pad.LEFT() == "PRESSED":
        print("LEFT")
    if pad.RIGHT() == "PRESSED":
        print("RIGHT")

    if pad.SELECT() == "PRESSED":
        print("SELECT")

    if pad.START() == "PRESSED":
        print("START")