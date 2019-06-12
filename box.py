#!/usr/bin/env python

#
# MUSIC CARD
# Application
#

import re
import sys
import subprocess
import os
import time
from CardList import CardList
from Reader import Reader

import config as cfg    # Get config from file

reader = Reader()
cardList = CardList()


# Create address path
address = cfg.ip + ':' + cfg.port

# Create command line
if cfg.location == '':
    # Command for global playing
    commandLine = address + ' '
else:
    # Command for local playing
    commandLine = address + ' ' + cfg.location + '/'


print 'Ready: place a card on top of the reader'

while True:
    card = reader.readCard()
    try:
        print 'Read card : ', card
        plist = cardList.getPlaylist(card)
        print 'Command : ', plist
        if plist != '':
            subprocess.check_call(["./sonosplay.sh %s" % commandLine + plist], shell=True)
            # subprocess.check_call( ["./haplaylist.sh %s" % plist], shell=True)
            range(10000)       # some payload code
            time.sleep(0.2)    # sane sleep time of 0.1 seconds
    except OSError as e:
        print "Execution failed:"
        range(10000)       # some payload code
        time.sleep(0.2)    # sane sleep time of 0.1 seconds

