import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def getArguments():
    parser = argparse.ArgumentParser(description='matrix 7219 arguments',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=4, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=-90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()
    return args

def setupDevice():
    args = getArguments()
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90,
                     rotate=0, blocks_arranged_in_reverse_order=False)
    print("Created device")
    
    return device

def flowMessage(device, msg):
    print("Vertical scrolling")
    show_message(device, msg, fill="yellow", font=proportional(LCD_FONT), scroll_delay=0.05)


def showMessage(device, msg):
    print("Simple dosplay")
    with canvas(device) as draw:
        #draw.rectangle(device.bounding_box, outline="white")
        text(draw, (0, 0), msg, fill="white", font=proportional(LCD_FONT))
