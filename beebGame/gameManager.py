import colorGenerator
import turnValidator
import notification
import ledController
from colorGenerator import Color

print('GameManager Start')

print('Round 1')

#notification.welcomeMessage()

colorList = colorGenerator.generateColorRandomList(4)

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

loseGame = False
items = 0

for x in colorList:
    print('////////WAIT FOR THE CLICKS///////')
    print(x)
    notification.showMessage('OK ' + str(items) )
    clickedColor = turnValidator.waitForClick()
    if x == clickedColor:
        print('True')
        notification.correctMessage()
        items = items + 1
    else:
        print('False')
        notification.wrongMessage()
        loseGame = True
        break
        
if(loseGame):
    notification.loseMessage()
else:
    notification.winMessage()