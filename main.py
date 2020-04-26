import time
import sys


def program(n):
    for i in reversed(range(1, 100)):
        if i in reversed(range(3, 100)):
            print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.\nYou take one" +
                  " down, pass it around. " + str(i - 1) + " bottles of beer on the wall.\n")
            time.sleep(n)
        elif i in reversed(range(2, 3)):
            print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.\nYou take one" +
                  " down, pass it around. " + str(i - 1) + " bottle of beer on the wall.")
            time.sleep(n)
        else:
            print(str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer, you take one" +
                  " down, pass it around. " + "No more bottles of beer on the wall.")
    sys.exit()


program(1)
