import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/home/pi/git/piDiods')

from spi_matrix32x8 import DisplayUtility as displayUtil

device = displayUtil.setupDevice()

def showMessage(msg):
    displayUtil.showMessage(device,msg)

def correctMessage():
    displayUtil.showMessage(device,'Right move')

def wrongMessage():
    displayUtil.showMessage(device, 'Wrong move')

def winMessage():
    displayUtil.flowMessage(device, 'Win Game !!!')

def loseMessage():
    displayUtil.flowMessage(device, 'Lose Game !!!')
    
def welcomeMessage():
    displayUtil.flowMessage(device, 'Welcome in click Game !!!')
