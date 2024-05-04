import os
from time import sleep
import threading as th

cols, lines = os.get_terminal_size()

WHITE_BG = "\033[47m"
BLUE_BG = "\033[44m" 
BLACK_FONT = "\033[30m"
WIDTH = 10
HEIGHT = 3
X = (lines//2) - (HEIGHT//2)
Y = (cols//2) - (WIDTH//2)
start = True
def key_capture_thread():
    global start
    input()
    start = False
def do_stuff():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    clouds()
    print("\033[0m")
    print("\033c")
def clouds():
    print(BLUE_BG,end="")
    while start:
        try:
            for row in range(0,lines-1):
                for col in range(0,cols-1):
                    if row >= X and row < X + HEIGHT:
                        if col >= Y and col < Y + WIDTH:
                            print(WHITE_BG,end="")
                            print(" ", end="")
                            print(BLUE_BG,end="")
                        else:
                            print(" ",end="")
                    else:
                        print(" ",end="")
        except KeyboardInterrupt:
            print("\033[0m")
            print("\033c")
            exit(0)

if __name__ == "__main__":
    print("\033c")
    print("To start and stop animation press \'ENTER\' ")
    input()
    do_stuff()


