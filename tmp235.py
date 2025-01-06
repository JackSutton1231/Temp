import board
import time
from analogio import AnalogIn
import pwmio

pot = AnalogIn(board.A0)

while True:
    maximum = 65535
    volts = pot.value / maximum * 3.3 
    tempC = (volts - .5) * 100
    tempF = (9/5) * tempC + 32
    
    print(tempF)
    time.sleep(.5)
