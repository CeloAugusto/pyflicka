from logging import basicConfig, info, INFO
from random import randrange
from sys import stdout
from time import sleep

from pynput.mouse import Controller

MIN, MAX = -50, 50
MOUSE = Controller()


def flicka():
    runs = randrange(5, 50)
    info("Running '%d' times:" % runs)

    for i in range(runs):
        x, y = randrange(MIN, MAX), randrange(MIN, MAX)
        delay = randrange(0, 100) / 1000
        info("Position x='%d' y='%d'." % (x, y))
        info("Delay '%f' seconds." % delay)

        MOUSE.move(x, y)
        sleep(delay)


def service():
    basicConfig(stream=stdout, level=INFO)
    try:
        while True:
            flicka()

            interval = randrange(1, 60)
            info("Interval of '%d' minutes." % interval)
            sleep(interval * 60)
    except KeyboardInterrupt:
        pass
    except Exception:
        service()
