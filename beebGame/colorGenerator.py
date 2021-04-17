from enum import Enum
import random

class Color(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 3

def generateRandomColor():
    randomColor = random.choice(list(Color))
    print('Generated')
    print(randomColor)
    return randomColor


def generateColorRandomList(size):
    colors = []
    for x in range(size):
        colors.append(generateRandomColor())
    return colors
        
#print(generateColorRandomList(4))