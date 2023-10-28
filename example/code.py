import board
from busio import UART
from ch9329 import CH9329, Keycode as KC
import time

uart = UART(tx=board.IO7, rx=board.IO6, baudrate=9600)
hid = CH9329(uart)

print("setup")
hid.debug = True

while True:
    # print("press A key")
    # hid.keyboard_press(KC.A)
    # time.sleep(0.1)
    # hid.keyboard_release(KC.A)
    # time.sleep(1)

    # print("press Shift+A key")
    # hid.keyboard_press(KC.A, KC.LEFT_SHIFT)
    # time.sleep(0.1)
    # hid.keyboard_release(KC.A, KC.LEFT_SHIFT)
    # time.sleep(1)

    # print("mouse up")
    # hid.mouse_move(0, -10, 0)

    # time.sleep(5)

    # print("hold abc")
    # hid.keyboard_press(KC.A)
    # time.sleep(1)
    # hid.keyboard_press(KC.B)
    # time.sleep(1)
    # hid.keyboard_press(KC.C)
    # time.sleep(1)
    # hid.keyboard_release(KC.A)
    # time.sleep(1)
    # hid.keyboard_release(KC.B)
    # time.sleep(1)
    # hid.keyboard_release(KC.C)
    # time.sleep(1)
    # hid.keyboard_release_all()

    # time.sleep(5)

    print("right click")
    hid.mouse_move(0, -10, 0)
    time.sleep(0.5)
    hid.mouse_press(CH9329.MOUSE_KEYCODE.LEFT_BUTTON)
    b = hid._uart.read()
    if b is not None:
        print("ch9329 recv:", " ".join(map(hex, b)))
    else:
        print("ch9329 no recv")
    time.sleep(1)
    hid.mouse_release_all()
    time.sleep(5)
