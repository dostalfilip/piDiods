from led import lightUtility as util
from spi_matrix32x8 import DisplayUtility as displayUtil
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(26, GPIO.FALLING)
GPIO.add_event_detect(12, GPIO.FALLING)
GPIO.add_event_detect(6, GPIO.FALLING)

device = displayUtil.setupDevice()

def buttonPressedGreen():
    print ("Green")
    displayUtil.showMessage(device,'Green')

def buttonPressedYellow():
    print ("Yellow")
    displayUtil.showMessage(device, 'Yellow')

def buttonPressedRed():
    print ("Red")
    displayUtil.showMessage(device, 'Red')


def detectionEventGreen():
    if GPIO.event_detected(26):
        buttonPressedGreen()

def detectionEventYellow():
    if GPIO.event_detected(12):
        buttonPressedYellow()

def detectionEventRed():
    if GPIO.event_detected(6):
        buttonPressedRed()

def main():
    while True:
        detectionEventGreen()
        detectionEventYellow()
        detectionEventRed()

main()