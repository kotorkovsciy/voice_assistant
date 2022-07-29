from pyfirmata import Arduino

board = Arduino('COM3')


def on_light():
    board.digital[8].write(1)


def off_light():
    board.digital[8].write(0)
