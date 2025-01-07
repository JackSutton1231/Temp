
import time
import gc
import board
import displayio
import random
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon
from analogio import AnalogIn
import pwmio

pot = AnalogIn(board.A0)


while True:
    maximum = 65535
    volts = pot.value / maximum * 3.3 
    tempC = (volts - .5) * 100
    tempF = (9/5) * tempC + 32
    tempF_str = str(tempF)
    
    print(tempF_str)
    time.sleep(.5)
