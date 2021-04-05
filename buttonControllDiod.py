import lightUtility as util
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(24, GPIO.IN, GPIO.PUD_DOWN)


try:
    print("Start Program")
    while True:
        vstup = GPIO.input(24)
        if vstup == True:
            print("Start lighting")
            util.main()
            print("End lighting")
            break
    
finally:
    GPIO.cleanup()    