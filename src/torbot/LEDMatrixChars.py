#!/usr/bin/python2
# -*- coding: latin-1 -*-

import re

class MatrixChars:
    """ Class that holds all the characters and symbols to display on
        the LED matrix.
    """

    ### Binary string matrices.
    
    # Example
    _RAW__ = ['xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx']

    ## NUMBERS

    ## LETTERS

    # Letter 'A'
    _RAW_A = ['00010000',
              '00111000',
              '00111000',
              '01101100',
              '01101100',
              '11111110',
              '11111110',
              '11000110',]

    ## Letter 'B'
    _RAW_B = ['11111100',
              '11111110',
              '11000110',
              '11111100',
              '11111100',
              '11000110',
              '11111110',
              '11111100',]
    
    # Letter 'C'
    _RAW_C = ['01111100',
              '01111110',
              '11100110',
              '11000000',
              '11000000',
              '11100110',
              '01111110',
              '01111100',]

    # Letter 'D'
    _RAW_D = [
              '11111000',
              '11111100',
              '11000110',
              '11000110',
              '11000110',
              '11000110',
              '11111100',
              '11111000']

    # Letter 'E'
    _RAW_E = ['11111110',
              '11111110',
              '11000000',
              '11111100',
              '11111100',
              '11000000',
              '11111110',
              '11111110']

    # Letter 'F'
    _RAW_F = ['11111110',
              '11111110',
              '11000000',
              '11111100',
              '11111100',
              '11000000',
              '11000000',
              '11000000']

    # Letter 'G'
    _RAW_G = ['01111100',
              '01111110',
              '11100000',
              '11001110',
              '11001110',
              '11100110',
              '01111110',
              '01111100',]

    # Letter 'H'
    _RAW_H = ['11000110',
              '11000110',
              '11000110',
              '11111110',
              '11111110',
              '11000110',
              '11000110',
              '11000110']

    # Letter 'I'
    _RAW_I = ['00111100',
              '00111100',
              '00011000',
              '00011000',
              '00011000',
              '00011000',
              '00111100',
              '00111100']

    # Letter 'J'
    _RAW_J = ['00011110',
              '00011110',
              '00001100',
              '00001100',
              '00001100',
              '11001100',
              '11111100',
              '00111100']

    # Letter 'K'
    _RAW_K = ['11000110',
              '11001100',
              '11011000',
              '11110000',
              '11110000',
              '11011000',
              '11001100',
              '11000110']

    # Letter 'L'
    _RAW_L = ['11000000',
              '11000000',
              '11000000',
              '11000000',
              '11000000',
              '11000000',
              '11111110',
              '11111110']

    # Letter 'M'
    _RAW_M = ['11000110',
              '11001110',
              '11101110',
              '11111110',
              '11010110',
              '11000110',
              '11000110',
              '11000110']

    # Letter 'N'
    _RAW_N = ['11000110',
              '11100110',
              '11110110',
              '11110110',
              '11011110',
              '11011110',
              '11001110',
              '11000110']

    # Letter 'O'
    _RAW_O = ['00111000',
              '01111100',
              '11101110',
              '11000110',
              '11000110',
              '11101110',
              '01111100',
              '00111000']

    # Letter 'P'
    _RAW_P = ['11111000',
              '11111100',
              '11000110',
              '11000110',
              '11111100',
              '11111000',
              '11000000',
              '11000000']

    # Letter 'Q'
    _RAW_Q = ['00111000',
              '01111100',
              '11101110',
              '11000110',
              '11000110',
              '11101110',
              '01111100',
              '00110110']

    # Letter 'R'
    _RAW_R = ['11111000',
              '11111100',
              '11000110',
              '11000110',
              '11111100',
              '11111000',
              '11001100',
              '11000110']

    # Letter 'S'
    _RAW_S = ['01111100',
              '11111110',
              '11100010',
              '01110000',
              '00011100',
              '10001110',
              '11111110',
              '01111100']

    # Letter 'T'
    _RAW_T = ['11111100',
              '11111100',
              '00110000',
              '00110000',
              '00110000',
              '00110000',
              '01111000',
              '01111000']

    # Letter 'U'
    _RAW_U = ['11000110',
              '11000110',
              '11000110',
              '11000110',
              '11000110',
              '11000110',
              '01111100',
              '00111000']

    # Letter 'V'
    _RAW_V = ['11000110',
              '11000110',
              '11000110',
              '01101100',
              '01101100',
              '01101100',
              '00111000',
              '00010000']

    # Letter 'W'
    _RAW_W = ['11000110',
              '11000110',
              '11000110',
              '11010110',
              '11111110',
              '11101110',
              '11000110',
              '01000100']

    # Letter 'X'
    _RAW_X = ['11000110',
              '11000110',
              '01101100',
              '00111000',
              '00111000',
              '01101100',
              '11000110',
              '11000110']

    # Letter 'Y'
    _RAW_Y = ['11000110',
              '11000110',
              '01101100',
              '00111100',
              '00011000',
              '00011000',
              '00011000',
              '00011000']

    # Letter 'Z'
    _RAW_Z = ['11111110',
              '11111110',
              '00001100',
              '00011000',
              '00110000',
              '01100000',
              '11111110',
              '11111110']


    ## German Umlauts

    # Letter 'Ä'
    _RAW_AE = ['10010010',
               '00111000',
               '00111000',
               '01101100',
               '01101100',
               '11111110',
               '11111110',
               '11000110',]

    # Letter 'Ö'
    _RAW_OE = ['10111010',
               '01111100',
               '11101110',
               '11000110',
               '11000110',
               '11101110',
               '01111100',
               '00111000']

    # Letter 'Ü'
    _RAW_UE = ['11000110',
               '00000000',
               '11000110',
               '11000110',
               '11000110',
               '11000110',
               '01111100',
               '00111000']

    # Letter 'ß'
    _RAW_SZ = ['01111100',
               '11000110',
               '11000110',
               '11011100',
               '11000110',
               '11000110',
               '11011100',
               '11000000',]


    ## SYMBOLS

    # Symbol '@'
    _RAW_AT = ['00111000',
               '01000100',
               '01010100',
               '10101010',
               '10101010',
               '01011100',
               '01000100',
               '00111000']

    # Symbol ':'
    _RAW_COLON = ['00000000',
                  '00000000',
                  '00110000',
                  '00110000',
                  '00000000',
                  '00110000',
                  '00110000',
                  '00000000']

    # Symbol ','
    _RAW_COMMA = ['00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00110000',
                  '00110000',
                  '00100000']

    # Symbol '!'
    _RAW_EXCLAIM = ['00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '11111011',
                    '11111011',
                    '00000000']
    _RAW_EXCLAIM = ['00110000',
                    '00110000',
                    '00110000',
                    '00110000',
                    '00110000',
                    '00000000',
                    '00110000',
                    '00110000']

    # Symbol '.'
    _RAW_PERIOD = ['00000000',
                   '00000000',
                   '00000000',
                   '00000000',
                   '00000000',
                   '00000000',
                   '00110000',
                   '00110000']

    # Symbol '?'
    _RAW_QUESTION = ['01111000',
                     '00001100',
                     '00111000',
                     '01100000',
                     '00111100',
                     '00000000',
                     '00110000',
                     '00110000']

    # Symbol ';'
    _RAW_SEMICOL = ['00000000',
                    '00000000',
                    '00110000',
                    '00110000',
                    '00000000',
                    '00110000',
                    '00110000',
                    '00100000']

    # Symbol ' '
    _RAW_SPACE = ['00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000']

    # Symbol 'Neutral'
    _RAW_NEUTRAL = ['00111100',
                    '01000010',
                    '10100101',
                    '10000001',
                    '10000001',
                    '10111101',
                    '01000010',
                    '00111100']

    # Symbol 'Smiley'
    _RAW_SMILE = ['00111100',
                  '01000010',
                  '10100101',
                  '10000001',
                  '10100101',
                  '10011001',
                  '01000010',
                  '00111100']

    # Symbol 'Sad'
    _RAW_SAD = ['00111100',
                '01000010',
                '10100101',
                '10000001',
                '10011001',
                '10100101',
                '01000010',
                '00111100']


    # Regular expression pattern to find all defined numbers, letters,
    # and symbols in a given string.
    FINDALL = re.compile(
        r'\xc3.|:[\(\)\|\/]|:(?![\(\)\|\/])|[@,\!\.\?; a-zA-Z0-9]')


    def __init__(self, backwards = True):
        """ Init some parameters. """
        self.BACKWARDS = backwards
        self._transform_matrices()
        self._build_translation_dict()

    def _transform_matrices(self):
        """ Transform all raw binary 'matrices' to input 'characters'
            for the Adafruit I2C 8x8 LED backpack.
        """
        # Take each _RAW_xxx string input matrix and assign the
        # corresponding numerical LED backpack matrix to the variable _xxx.
        for varName in vars(MatrixChars).keys():
            if varName.startswith('_RAW_') and (varName != '_RAW__'):
                vars(MatrixChars)[varName[4:]] = self.matrix2led(
                    eval('self.%s' % varName))

    def _build_translation_dict(self):
        """ Builds the translation dictionary
            letter/symbol -> MatrixChars.
        """
        self.TRANSLATION = {
            # Symbols
            u'@': self._AT,
            u':': self._COLON,
            u',': self._COMMA,
            u'!': self._EXCLAIM,
            u'.': self._PERIOD,
            u'?': self._QUESTION,
            u';': self._SEMICOL,
            u' ': self._SPACE,
            u':|': self._NEUTRAL,
            u':)': self._SMILE,
            u':(': self._SAD,
            # Umlauts
            u'Ä': self._AE,
            u'ä': self._AE,
            u'Ö': self._OE,
            u'ö': self._OE,
            u'Ü': self._UE,
            u'ü': self._UE,
            u'ß': self._SZ,
        }

        for i in range(65, 91):
            self.TRANSLATION[chr(i)] = eval('self._%s' % chr(i))

    def row2led(self, _bin = None):
        """ Transforms a given binary string into an input row for the
            Adafruit I2C 8x8 LED backpack.
        """
        if _bin is None:
            return
        return int(_bin, 2)

    def matrix2led(self, _bin = None):
        """ Transform a raw binary 'matrix' to input for the Adafruit I2C
            8x8 LED backpack.
        """
        if _bin is None:
            return
        matrix = []
        for index in range(8):
            matrix_row = u''
            for _row in _bin:
                if self.BACKWARDS:
                    # For backwards display rotate 90° CW.
                    matrix_row = u'%s%s' % (matrix_row, _row[index])
                else:
                    # Otherwise, rotate the input matrix 90° CCW.
                    matrix_row = u'%s%s' % (_row[7-index], matrix_row)
            matrix.append(matrix_row)

        matrixList = []
        for row in matrix:
            matrixList.append(self.row2led(row))
        return matrixList

    def message2matrix(self, message):
        """ Convert a string message to an input stream for the LED
            backpack.
        """
        matrixOutput = []
        for character in message:
            matrixOutput.extend(self.TRANSLATION[character.upper()])
        return matrixOutput
