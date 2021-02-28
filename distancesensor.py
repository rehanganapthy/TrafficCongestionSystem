import RPi.GPIO as gpio
import time

def distance(measure='m'):
    try:
        gpio.setmode(gpio.BOARD)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.IN)
        
        gpio.output(12, False)
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()

        tl = sig - nosig

        if measure == 'm':
            distance = tl / 0.00058

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance

		
if __name__ == "__main__":
    print(distance('cm'))
		
