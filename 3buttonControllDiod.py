import lightUtility as util
import RPi.GPIO as GPIO
import time
# Parallelizing using Pool.apply()
import multiprocessing as mp
import asyncio



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

async def buttonPressedGreen():
    print ("Green")

async def buttonPressedYellow():
    print ("Yellow")

async def buttonPressedRed():
    print ("Red")

GPIO.add_event_detect(24, GPIO.RISING)
GPIO.add_event_detect(12, GPIO.RISING)
GPIO.add_event_detect(6, GPIO.RISING)

async def detectionEventGreen():
    while True:
        if GPIO.event_detected(24):
            buttonPressedGreen()
            for x in range(0, 3):
                util.periodSimple(util.Diods.GREEN, 0.3)
            

async def detectionEventYellow():
    while True:
        if GPIO.event_detected(12):
            buttonPressedYellow()
            for x in range(0, 3):
                util.periodSimple(util.Diods.YELLOW, 0.3)
            

async def detectionEventRed():
    while True:
        if GPIO.event_detected(6):
            buttonPressedRed()
            for x in range(0, 3):
                util.periodSimple(util.Diods.RED, 0.3)
            
            
#pool = mp.Pool(mp.cpu_count())
#print(mp.cpu_count())
# Step 1: Init multiprocessing.Pool()
#pool.apply_async(detectionEventYellow())
#pool.apply_async(detectionEventRed())

#pool.apply_async(detectionEventGreen())
asyncio.run(detectionEventRed())
asyncio.run(detectionEventYellow())


asyncio.run(detectionEventGreen())

#loop.run_until_complete(print_numbers(loop))
print('End')

#pool = mp.Pool(detectionEventYellow())
#pool = mp.Pool(detectionEventGreen())
# Step 3: Don't forget to close
#pool.close()    

#print(results[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]