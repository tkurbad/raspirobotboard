#!/usr/bin/python2

def row2led(_bin = None):
    """ Transforms a given binary string into an input row for the
        Adafruit I2C 8x8 LED backpack.
    """
    if _bin is None:
        return
    return int(_bin[7] + _bin[0:7], 2)

def matrix2led(_bin = None):
    """ Transform a raw binary 'matrix' to input for the Adafruit I2C
        8x8 LED backpack.
    """
    if _bin is None:
        return
    binList = []
    for row in _bin:
        binList.append(row2led(row))
    return binList

### Binary string matrices. Note that the symbols are rotated 90° ccw. #

# Example
_RAW__ = ['xxxxxxxx',
          'xxxxxxxx',
          'xxxxxxxx',
          'xxxxxxxx',
          'xxxxxxxx',
          'xxxxxxxx',
          'xxxxxxxx',
          'xxxxxxxx']

# Letter 'A'
_RAW_A = ['00000000',
          '00000011',
          '00001110',
          '00111110',
          '11100110',
          '00111110',
          '00001110',
          '00000011']

# Letter 'B'
_RAW_B = ['00000000',
          '01100110',
          '11111111',
          '11011011',
          '11011011',
          '11011011',
          '11111111',
          '11111111']

# Letter 'C'
_RAW_C = ['00000000',
          '01100110',
          '11100111',
          '11000011',
          '11000011',
          '11100111',
          '11111111',
          '00111100']

### Numeric matrices ready to send to the LED backpack. ################

# Take each _RAW_xxx string input matrix and assign the corresponding
# numerical LED backpack matrix to the variable _xxx.
for varName in vars().keys():
    if varName.startswith('_RAW_'):
        vars()[varName[4:] = matrix2led(eval(varName))
