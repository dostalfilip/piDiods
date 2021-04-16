from led import lightUtility as util
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.FALLING)

try:
    print("Start Program")
    while True:
        if GPIO.event_detected(26):
            print("Start lighting")
            util.main()
            print("End lighting")
            break
    
finally:
    GPIO.cleanup()    