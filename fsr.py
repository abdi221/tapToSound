# testing the sensor

from machine import ADC, Pin
import time

fsr_pin = 28

fsr = ADC(Pin(fsr_pin))

while True:
    analog_reading = fsr.read_16() # read the raw analog values
    analog_reading = analog_reading // 64 # scale it down to 0-1023 range to match arduino
    print("Force sensor reading: ", analog_reading)
    
    if analog_reading < 6553: # from 0 to 6552
        print(" -> no pressure")
    elif analog_reading < 13107: # from 6552 to 13106
        print(" -> light touch")
    elif analog_reading < 32767: # from 13106 to 32766
        print(" -> light squeeze")
    elif analog_reading < 52428: # from 32766 to 52427
        print(" -> medium touch")
    else:
        print(" -> BIG SQUEEZE")
        
    
    
    
