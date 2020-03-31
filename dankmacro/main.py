"""Top-level implementation of the dankmacro program."""

# MIT License
# 
# Copyright (c) 2020 TEEN-BOOM
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
from math import floor
import sys
from random import choice, randint
from time import sleep

from pynput.keyboard import Controller, Key

import dankmacro

keyboard = Controller()

parser = argparse.ArgumentParser(description="A python macro for dank memer discord.")
parser.add_argument("-v","--version", action="version",version="DANKMACRO-" + dankmacro.__version__)
parser.add_argument("-p","--postmemes", action="store_true",help="Flag to enable `pls pm` choice of meme is random,DO NOT ENABLE WITHOUT LAPTOP!")
parser.add_argument("-f", "--fish", action="store_true",help="Flag to enable `pls fish`. REQUIRES FISHING POLE!")
parser.add_argument("-b", "--beg", action="store_true",help="Enables `pls beg`")
parser.add_argument("-t", "--time", action="store",help="specify the amount of delay on top of 30 second, defaults to o.1. Usage:`dankmacro -t 0.9`",type=float)
parser.add_argument("-d", "--deposit", action="store",help="Specify wether all coins should be deposited at random interval with probablity `1/n`, n can be be specified with `dankmacro -d 10`, defaults to 7", type=int)

def send(text:str):
    keyboard.type(text)
    keyboard.press(Key.enter)
    sleep(0.09)
    keyboard.release(Key.enter)
    return None

def fish_macro():
    #TIME = 0.19 seconds
    send("pls fish")
    sleep(0.1)
    return None

def beg_macro():
    #TIME = 0.19 seconds
    send("pls beg")
    sleep(0.1)
    return None

def pm_macro():
    #TIME = 0.59 seconds
    send("pls pm")
    c = choice(["n","r","d","n","r","d","e"])
    #edgy meme seems to break laptop
    #OBSERVATION:
    # __________________
    #|RESULT  |FREQUENCY|
    #|▔▔▔▔▔▔▔▔|▔▔▔▔▔▔▔▔▔|
    #|TRENDING|    2    |
    #|NORMAL  |    5    |
    #|HATED   |    5    | \\DOESN"T INCLUDE BROKEN 
    #|BROKEN  |    3    |
    #|TOTAL   |    15   | 
    # ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ 
    #EVEN THOUGH RESULT DEPENDS ON RANDOMNESS OF `choice()`
    sleep(0.5)
    send(c)
    return None

def random(n):
    #TIME = 1.68 seconds
    r = randint(1,n)
    if r == floor((n + 1)/2):
        sleep(1)
        send("pls dep all")
        return None
    else:
        return None

def main(argv=sys.argv):
    args = parser.parse_args(argv[1:])
    if args.time is not None:
        t = 30 + args.time
    else:
        t = 30.1
    print(f"DELAY SET TO : {t} seconds")
    if not len(sys.argv) > 1:
        print("No flags or args given, use dankmacro -h. Exiting... ")
        return None
    a = range(2)
    try:
        while True:
            for i in a:
                if args.beg is True:
                    beg_macro()
                if args.fish is True:
                    fish_macro()
                sleep(t)
            else:
                if args.postmemes is True:
                    pm_macro()
                if args.deposit is not None:
                    random(args.d)
    except KeyboardInterrupt:
        print("EXITING")
        return None