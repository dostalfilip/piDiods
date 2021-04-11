#!/usr/bin/env python
    
import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT



def verticalScroll(device):
    print("Vertical scrolling")
    words = [
        " Filipek", "Misicka", "Olivererek", "Berynka", " "
    ]

    for i in range(1 - 10):
        virtual = viewport(device, width=device.width, height=len(words) * 8)
        with canvas(virtual) as draw:
            for i, word in enumerate(words):
                text(draw, (0, i * 8), word, fill="yellow", font=proportional(CP437_FONT))

        for i in range(virtual.height - device.height):
            virtual.set_position((0, i))
            time.sleep(0.1)


def bright(device):
    msg = "msg Brighting" #brighting
    print(msg)
    show_message(device, msg, fill="yellow")

    time.sleep(1)
    with canvas(device) as draw:
        text(draw, (0, 0), "Olik", fill="yellow")

    time.sleep(1)
    for _ in range(5):
        for intensity in range(16):
            device.contrast(intensity * 16)
            time.sleep(0.1)

    device.contrast(0x80)
    time.sleep(1)



def demo(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print("Created device")

    # start demo
    msg = "MAX7219 LED Matrix Welcome"
    print(msg)
    show_message(device, msg, fill="yellow", font=proportional(CP437_FONT))
    time.sleep(1)

    msg = ""
    msg = re.sub(" +", " ", msg)
    print(msg)
    show_message(device, msg, fill="yellow", font=proportional(LCD_FONT), scroll_delay=0)

    msg = "Olivere !!!! Poslouchej dobre.. chlapecku"
    print(msg)
    show_message(device, msg, fill="yellow", font=proportional(LCD_FONT), scroll_delay=0.1)


    verticalScroll(device)

    bright(device)

    msg = "Alternative font!"
    print(msg)
    show_message(device, msg, fill="yellow", font=SINCLAIR_FONT)

    time.sleep(1)
    msg = "Proportional font"
    print(msg)
    show_message(device, msg, fill="yellow", font=proportional(SINCLAIR_FONT))

    # http://www.squaregear.net/fonts/tiny.shtml
    time.sleep(1)
    msg = "Tiny font"
    msg = re.sub(" +", " ", msg)
    print(msg)
    show_message(device, msg, fill="yellow", font=proportional(TINY_FONT))

    time.sleep(1)
    msg = "CP437 Characters Dostupne znaky"
    print(msg)
    show_message(device, msg)

    time.sleep(1)
    for x in range(256):
        with canvas(device) as draw:
            text(draw, (0, 0), chr(x), fill="yellow")
            time.sleep(0.1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=4, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=-90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
    except KeyboardInterrupt:
        pass

