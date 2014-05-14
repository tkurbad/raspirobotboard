#!/usr/bin/python2
# -*- coding: utf-8 -*-


class MatrixChars:
    """ Class that holds all the characters and symbols to display on
        the LED matrix.
    """

    ### Binary string matrices. Note that the symbols are rotated 90°
    ### ccw.
    
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

    def __init__(self):
        """ Init some parameters. """
        self.transform_matrices()

    def row2led(self, _bin = None):
        """ Transforms a given binary string into an input row for the
            Adafruit I2C 8x8 LED backpack.
        """
        if _bin is None:
            return
        return int(_bin[7] + _bin[0:7], 2)

    def matrix2led(self, _bin = None):
        """ Transform a raw binary 'matrix' to input for the Adafruit I2C
            8x8 LED backpack.
        """
        if _bin is None:
            return
        binList = []
        for row in _bin:
            binList.append(self.row2led(row))
        return binList

    def transform_matrices(self):
        """ Transform all raw binary 'matrices' to input 'characters'
            for the Adafruit I2C 8x8 LED backpack.
        """

        # Take each _RAW_xxx string input matrix and assign the
        # corresponding numerical LED backpack matrix to the variable _xxx.
        for varName in vars(MatrixChars).keys():
            if varName.startswith('_RAW_') and (varName != '_RAW__'):
                vars(MatrixChars)[varName[4:]] = self.matrix2led(eval(varName))

    def string2matrix(self, message):
        """ Convert a string message to an input stream for the LED
            backpack.
        """
