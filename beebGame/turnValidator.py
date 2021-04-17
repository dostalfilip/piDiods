import RPi.GPIO as GPIO
from colorGenerator import Color

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(26, GPIO.RISING)
GPIO.add_event_detect(12, GPIO.RISING)
GPIO.add_event_detect(6, GPIO.RISING)

def detectionEventGreen():
    if GPIO.event_detected(26):
        print ("Clicked Green")
        return True
    else:
        return False

def detectionEventYellow():
    if GPIO.event_detected(12):
        print ("Clicked Yellow")
        return True
    else:
        return False

def detectionEventRed():
    if GPIO.event_detected(6):
        print ("Clicked Red")
        return True
    else:
        return False

def waitForClick():
    if detectionEventGreen():
        print ("ReClick")
        waitForClick()
    if detectionEventYellow():
        print ("ReClick")
        waitForClick()
    if detectionEventRed():
        print ("ReClick")
        waitForClick()
    
    while True:
        if detectionEventGreen():
            return Color(1)
        if detectionEventYellow():
            return Color(2)
        if detectionEventRed():
            return Color(3)
        