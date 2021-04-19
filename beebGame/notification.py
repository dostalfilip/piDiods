import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/home/pi/git/piDiods')

from spi_matrix32x8 import DisplayUtility as displayUtil

device = displayUtil.setupDevice()

def showMessage(msg):
    displayUtil.showMessage(device,msg)

def correctMessage():
    displayUtil.showMessage(device,'Good')
    
def upssMessage():
    displayUtil.winkMessage(device, 'Upss')
    
def playMessage():
    displayUtil.winkMessage(device, 'PLAY')

def loseWinkMessage():
    displayUtil.winkMessage(device, 'LOSE')
    
def winMessage(totalColor, rightAnswer):
    displayUtil.flowMessage(device, 'Win Game !!! Chose correctly ' + str(rightAnswer) + ' out of ' + str(totalColor) )

def loseMessage():
    displayUtil.flowMessage(device, 'Game Over !!!')
    
def roundMessage(level):
    displayUtil.flowMessage(device, 'Round ' + str(level))
    
def welcomeMessage():
    displayUtil.flowMessage(device, 'Welcome in Click Game !!!')
