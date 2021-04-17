import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/home/pi/git/piDiods')

from led import lightUtility as util
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


def greenBlink():
    util.periodSimple(util.Diods.GREEN, 0.5)

def yellowBlink():
    util.periodSimple(util.Diods.YELLOW, 0.5)

def redBlink():
    util.periodSimple(util.Diods.RED, 0.5)