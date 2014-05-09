#!/usr/bin/python2

import sys
import time

from torbot.Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = EightByEight(address=0x70)

test = ('11111111',
        '11000011',
        '10000001',
        '00000000',
        '00000000',
        '10000001',
        '11000011',
        '11111111')

grid.clear()
row = 0
for val in test:
    grid.writeRowRaw(row, int(val, 2) >> 1)
    row += 1
