#!/usr/bin/python2

import sys
import time

from torbot.Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = EightByEight(address=0x70)

grid.clear()
grid.writeRowRaw(0, 1)
