import RPi.GPIO as GPIO
import time
from enum import Enum


class Diods(Enum):
   GREEN=16
   YELLOW=19
   RED=21

def pinCoolDown():
    GPIO.output(21, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

print ("Setup")
setup()


def on(diod : Diods):
    GPIO.output(diod.value, GPIO.HIGH)
    
def off(diod : Diods):
    GPIO.output(diod.value, GPIO.LOW)

def period(diod : Diods, lightOn : float, lightOff : float):
    on(diod)
    time.sleep(lightOn)
    off(diod)
    time.sleep(lightOff)
    
def periodSimple(diod : Diods, lightEqualLength : float):
    period(diod, lightEqualLength, lightEqualLength)

print ("Start")


#GPIO.output(21, GPIO.HIGH)
#GPIO.output(19, GPIO.HIGH)
#time.sleep(2)
#GPIO.output(21, GPIO.LOW)


#while 1:
def main():
    for x in range(0, 5):
        periodSimple(Diods.GREEN, 0.05)
        periodSimple(Diods.YELLOW, 0.1)
        periodSimple(Diods.RED, 0.2)
    
    for x in range(0, 5):
        periodSimple(Diods.RED, 0.05)
        periodSimple(Diods.YELLOW, 0.1)
        periodSimple(Diods.GREEN, 0.2)

#main()

pinCoolDown()
print ("End")