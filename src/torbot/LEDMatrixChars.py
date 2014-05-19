#!/usr/bin/python2
# -*- coding: latin-1 -*-


class MatrixChars:
    """ Class that holds all the characters and symbols to display on
        the LED matrix.
    """

    ### Binary string matrices. Note that all symbols are mirrored and 
    ### rotated 90° CCW.
    
    # Example
    _RAW__ = ['xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx',
              'xxxxxxxx']

    ## LETTERS

    # Letter 'A'
    #_RAW_A = ['00000011',
              #'00001111',
              #'00111110',
              #'11100110',
              #'00111110',
              #'00001111',
              #'00000011',
              #'00000000',]
    _RAW_A = ['00010000',
              '00111000',
              '00111000',
              '01101100',
              '01101100',
              '11111110',
              '11111110',
              '11000110',]

    ## Letter 'B'
    #_RAW_B = ['11111111',
              #'11111111',
              #'11011011',
              #'11011011',
              #'11011011',
              #'11111111',
              #'01100110',
              #'00000000',]
    _RAW_B = ['11111100',
              '11111110',
              '11000110',
              '11111100',
              '11111100',
              '11000110',
              '11111110',
              '11111100',]
    
    # Letter 'C'
    _RAW_C = ['00111100',
              '11111111',
              '11100111',
              '11000011',
              '11000011',
              '11100111',
              '01100110',
              '00000000',]

    # Letter 'D'
    _RAW_D = [
              '00000000',
              '01111110',
              '11100111',
              '11000011',
              '11000011',
              '11000011',
              '11111111',
              '11111111']

    # Letter 'E'
    _RAW_E = ['00000000',
              '11000011',
              '11011011',
              '11011011',
              '11011011',
              '11011011',
              '11111111',
              '11111111']

    # Letter 'F'
    _RAW_F = ['00000000',
              '11000000',
              '11011000',
              '11011000',
              '11011000',
              '11011000',
              '11111111',
              '11111111']

    # Letter 'G'
    _RAW_G = ['00000000',
              '01101110',
              '11001111',
              '11000011',
              '11000011',
              '11100111',
              '11111111',
              '00111100']

    # Letter 'H'
    _RAW_H = ['00000000',
              '11111111',
              '11111111',
              '00011000',
              '00011000',
              '00011000',
              '11111111',
              '11111111']

    # Letter 'I'
    _RAW_I = ['00000000',
              '00000000',
              '00000000',
              '11000011',
              '11111111',
              '11111111',
              '11000011',
              '00000000']

    # Letter 'J'
    _RAW_J = ['00000000',
              '00000000',
              '00000000',
              '11111111',
              '11111111',
              '11000011',
              '00000011',
              '00000110']

    # Letter 'K'
    _RAW_K = ['00000000',
              '11000011',
              '11000011',
              '01100110',
              '00111100',
              '00011000',
              '11111111',
              '11111111']

    # Letter 'L'
    _RAW_L = ['00000000',
              '00000111',
              '00000011',
              '00000011',
              '00000011',
              '00000011',
              '11111111',
              '11111111']

    # Letter 'M'
    _RAW_M = ['00000000',
              '11111111',
              '11111111',
              '00110000',
              '00011000',
              '00110000',
              '11111111',
              '11111111']

    # Letter 'N'
    _RAW_N = ['00000000',
              '11111111',
              '11111111',
              '00001110',
              '00111100',
              '01110000',
              '11111111',
              '11111111']

    # Letter 'O'
    _RAW_O = ['00000000',
              '00111100',
              '11111111',
              '11100111',
              '11000011',
              '11100111',
              '11111111',
              '00111100']

    # Letter 'P'
    _RAW_P = ['00000000',
              '00110000',
              '01111000',
              '11001100',
              '11001100',
              '11001100',
              '11111111',
              '11111111']

    # Letter 'Q'
    _RAW_Q = ['00000000',
              '00111011',
              '11111111',
              '11100110',
              '11000011',
              '11100111',
              '11111111',
              '00111100']

    # Letter 'R'
    _RAW_R = ['00000000',
              '00110000',
              '01111001',
              '11001111',
              '11001110',
              '11001100',
              '11111111',
              '11111111']

    # Letter 'S'
    _RAW_S = ['00000000',
              '01100110',
              '11001111',
              '11001111',
              '11011011',
              '11110011',
              '11110011',
              '01100110']

    _RAW_S = ['00000000',
              '01100110',
              '11001111',
              '11001111',
              '11011011',
              '11110011',
              '11110011',
              '01100110']
    _RAW_S = ['00000000',
              '01100110',
              '11110011',
              '11110011',
              '11011011',
              '11001111',
              '11001111',
              '01100110']

    # Letter 'T'
    _RAW_T = ['00000000',
              '00000000',
              '11000000',
              '11000011',
              '11111111',
              '11111111',
              '11000011',
              '11000000']

    # Letter 'U'
    _RAW_U = ['00000000',
              '11111100',
              '11111110',
              '00000011',
              '00000011',
              '00000011',
              '11111110',
              '11111100']

    # Letter 'V'
    _RAW_V = ['00000000',
              '11000000',
              '01111100',
              '00001110',
              '00000011',
              '00001110',
              '01111100',
              '11000000']

    # Letter 'W'
    _RAW_W = ['00000000',
              '11111110',
              '11111111',
              '00001100',
              '00011000',
              '00001100',
              '11111111',
              '11111110']

    # Letter 'X'
    _RAW_X = ['00000000',
              '11000011',
              '11100111',
              '00111100',
              '00011000',
              '00111100',
              '11100111',
              '11000011']

    # Letter 'Y'
    _RAW_Y = ['00000000',
              '11000000',
              '11110000',
              '00111111',
              '00011111',
              '00111000',
              '11100000',
              '11000000']

    # Letter 'Z'
    _RAW_Z = ['00000000',
              '11000011',
              '11100011',
              '11110011',
              '11011011',
              '11001111',
              '11000111',
              '11000011']

    ## SYMBOLS

    # Symbol '@'
    _RAW_AT = ['00000000',
               '00011000',
               '01100110',
               '10111101',
               '10100101',
               '10011001',
               '01100110',
               '00011000']

    # Symbol ','
    _RAW_COMMA = ['00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000110',
                  '00000111',
                  '00000000']

    # Symbol '.'
    _RAW_DOT = ['00000000',
                '00000000',
                '00000000',
                '00000000',
                '00000000',
                '00000011',
                '00000011',
                '00000000']

    # Symbol '!'
    _RAW_EXCLAIM = ['00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '11111011',
                    '11111011',
                    '00000000']

    # Symbol '?'
    _RAW_QUESTION = ['00000000',
                     '00000000',
                     '00000000',
                     '01001000',
                     '11101011',
                     '10101011',
                     '10111000',
                     '00000000']

    # Symbol ';'
    _RAW_SEMICOL = ['00000000'
                    '00000000',
                    '00000000',
                    '00000000',
                    '00000000',
                    '00110110',
                    '00110111',
                    '00000000']

    # Symbol ' '
    _RAW_SPACE = ['00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000',
                  '00000000']

    # Symbol 'Smiley'
    _RAW_SMILE = ['00011000',
                  '00100100',
                  '01101010',
                  '10000101',
                  '10000101',
                  '01101010',
                  '00100100',
                  '00011000']

    # Symbol 'Sad'
    _RAW_SAD = ['00011000',
                '00100100',
                '01101010',
                '10010001',
                '10010001',
                '01101010',
                '00100100',
                '00011000']


    ## German Umlauts
    _RAW_AE = ['00000000',
               '00000011',
               '10001111',
               '00111110',
               '11100110',
               '00111110',
               '10001111',
               '00000011']


    def __init__(self):
        """ Init some parameters. """
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
            u',': self._COMMA,
            u'.': self._DOT,
            u'!': self._EXCLAIM,
            u'?': self._QUESTION,
            u';': self._SEMICOL,
            u' ': self._SPACE,
            # Umlauts
            u'Ä': self._AE,
            u'ä': self._AE,
            u'Ö': self._O + self._E,
            u'ö': self._O + self._E,
            u'Ü': self._U + self._E,
            u'ü': self._U + self._E,
            u'ß': self._S + self._S,
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
        # Mirror the input matrix and turn 90° CCW.
        matrix = []
        for index in range(8):
            matrix_row = u''
            for _row in _bin:
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
