# testing the sensor

from machine import ADC, Pin
import time

fsr_pin = 28

fsr = ADC(Pin(fsr_pin))

while True:
    analog_reading = fsr.read_u16() # read the raw analog values
    analog_reading = analog_reading // 64 # scale it down to 0-1023 range to match arduino
    print("Force sensor reading: ", analog_reading)
    
    if analog_reading < 500:
        print(" -> no pressure")
    elif analog_reading < 900:
        print(" -> light touch")
    elif analog_reading < 1000:
        print(" -> medium touch")
    else:
        print(" -> BIG SQUEEZE")
        
    time.sleep(1)
        
    
    
    
