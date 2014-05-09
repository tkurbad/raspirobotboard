#!/usr/bin/python2

import sys
import time

from torbot.Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = EightByEight(address=0x70)

test = ('011111111',
        '011000011',
        '010000001',
        '000000000',
        '000000000',
        '010000001',
        '011000011',
        '011111111')

grid.clear()
row = 0
for val in test:
    grid.writeRowRaw(row, int(val, 2) >> 1)
    row += 1
