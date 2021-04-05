import lightUtility as util
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def buttonPressedGreen():
    print ("Green")

def buttonPressedYellow():
    print ("Yellow")

def buttonPressedRed():
    print ("Red")

GPIO.add_event_detect(24, GPIO.RISING)
GPIO.add_event_detect(12, GPIO.RISING)
GPIO.add_event_detect(6, GPIO.RISING)


while True:
    if GPIO.event_detected(24):
        buttonPressedGreen()
        for x in range(0, 3):
            util.periodSimple(util.Diods.GREEN, 0.3)

    if GPIO.event_detected(12):
        buttonPressedYellow()
        for x in range(0, 3):
            util.periodSimple(util.Diods.YELLOW, 0.3)

    if GPIO.event_detected(6):
        buttonPressedRed()
        for x in range(0, 3):
            util.periodSimple(util.Diods.RED, 0.3)