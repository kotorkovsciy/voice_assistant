from pyfirmata import Arduino

board = Arduino('COM3')


def on_light():
    board.digital[8].write(1)
    board.digital[2].write(1)
    board.digital[3].write(1)


def off_light():
    board.digital[8].write(0)
    board.digital[2].write(0)
    board.digital[3].write(0)
