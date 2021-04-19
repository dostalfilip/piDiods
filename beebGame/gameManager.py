import colorGenerator
import turnValidator
import notification
import ledController
from colorGenerator import Color
import time

totalColor = 4
loseGame = False
extraLife = True
rightAnswer = 0

print('GameManager Start')

def turnValidation(clickedColor):
    global loseGame
    global rightAnswer
    global extraLife
    if x == clickedColor:
        print('True')
        notification.correctMessage()
        time.sleep(0.3)
        rightAnswer = rightAnswer + 1
        return True
    else:
        print('False')
        if(extraLife):
            extraLife = False
            notification.upssMessage()
            return True
        notification.loseWinkMessage()
        loseGame = True
        return False

notification.welcomeMessage()
notification.roundMessage(1)

notification.showMessage('PLAY')
time.sleep(2)
notification.showMessage('')

colorList = colorGenerator.generateColorRandomList(totalColor)
for x in colorList:
    print('////////BLIKING///////')
    print(x)
    if x == Color.GREEN:
        print('Blink Green')
        ledController.greenBlink()
            
    if x == Color.YELLOW:
        print('Blink Yellow')
        ledController.yellowBlink()
        
    if x == Color.RED:
        print('Blink Red')
        ledController.redBlink()


for x in colorList:
    print('////////WAIT FOR THE CLICKS///////')
    print(x)
    notification.showMessage('OK ' + str(rightAnswer) )
    clickedColor = turnValidator.waitForClick()
    if(False == turnValidation(clickedColor)):
        break
        
if(loseGame):
    notification.loseMessage()
else:
    notification.winMessage(totalColor, rightAnswer)
    