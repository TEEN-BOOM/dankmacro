## Dank macro

A python macro for dank memer discord

### Usage

Install the program by `python -m pip install git+https://github.com/TEEN-BOOM/dankmacro#egg=dankmacro`(python3 or python in your case) or `python setup.py install` after cloning(downloading) the repo.  
Later you may invoke the program by typing `dankmacro -b` in a shell.
<hr>

## WARNING!!

The use of this script has resulted in bans! This software comes without any warranties.
Hence you are responsible for any damages incurred.

#### The Complete guide/Dummy's Guide

1.Open the terminal with `ctrl+alt+t` or open cmd from search on windows and type `python3 -V` if the version is 3.7.3 or above, then you can proceed to the 3rd step.  
2.if you do not have python then follow [this guide](https://realpython.com/installing-python/).  
3.Then type `pip3 install git+https://github.com/TEEN-BOOM/dankmacro#egg=dankmacro` in the terminal. If pip3 is not recognised then install it folllowing [this](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/) guide (if you are using ubuntu )or simply try `pip install git+https://github.com/TEEN-BOOM/dankmacro#egg=dankmacro` (if you are on windows).  
4.verify the install with `dankmacro -V`  

### Help

usage: dankmacro [-h] [-v] [-p] [-f] [-b] [-t TIME] [-d DEPOSIT]

A python macro for dank memer discord.

optional arguments:
+  -h, --help            show this help message and exits.
+  -v, --version         show program's version number and exit
+  -p, --postmemes       Flag to enable `pls pm` choice of meme is random,DO
                        NOT ENABLE WITHOUT LAPTOP!
+  -f, --fish            Flag to enable `pls fish`. REQUIRES FISHING POLE!
+  -b, --beg             Enables `pls beg`
+  -t TIME, --time TIME  specify the amount of delay on top of 30 second,
                        defaults to o.1. Usage:`dankmacro -t 0.9`
+  -d DEPOSIT, --deposit DEPOSIT
                        Specify wether all coins should be deposited at random
                        interval with probablity `1/n`, n can be be specified
                        with `dankmacro -d 10`, defaults to 7.
+  -c COUNTDOWN, --countdown COUNTDOWN
                        specify the amount of time to wait before starting.
                        Defaults to 3 seconds. Usage:`dankmacro -c 9`.
