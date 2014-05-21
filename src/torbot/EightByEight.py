#!/usr/bin/python2
# -*- coding: latin-1 -*-

from __future__ import print_function

import sys
from time import sleep

import Adafruit_8x8

from LEDMatrixChars import MatrixChars


class EightByEight(Adafruit_8x8.EightByEight):
    """ Extend Adafruit's original EightByEight class to allow for easy
        displaying of string messages, characters and symbols.
    """

    def __init__(self, address = 0x70, debug = False, backwards = True):
        """ Initialize the LED matrix. """
        super(EightByEight, self).__init__(address = address, debug = debug)
        self.matrixChars = MatrixChars(backwards = backwards)

    def write_matrix_raw(self, matrixCharacter):
        """ Display a whole set of encoded matrix data, i.e. one symbol,
            character, etc. """
        lineNum = 0
        for line in matrixCharacter:
            self.writeRowRaw(lineNum, line)
            lineNum += 1
            # For testing
            if self.disp.i2c.bus.__class__.__name__ == 'FakeSMBus':
                print ('Line number %d: %d' % (lineNum, line))

    def translate_char(self, character):
        """ Translate a single (ASCII) character to matrix output
            format.
        """
        matrixCharacter = self.matrixChars._SPACE
        if character in self.matrixChars.TRANSLATION.keys():
            matrixCharacter = self.matrixChars.TRANSLATION[character]
        elif character.upper() in self.matrixChars.TRANSLATION.keys():
            matrixCharacter = self.matrixChars.TRANSLATION[
                                    character.upper()]
        return matrixCharacter

    def translate_string(self, message):
        """ Translate a string of characters to matrix output format.
        """
        if not message:
            print('ERROR: Message is empty. Not displaying anything.',
                file = sys.stderr)
            return []

        charList = self.matrixChars.FINDALL.findall(message)
        matrixList = []

        for character in charList:
            if character:
                matrixList.append(self.translate_char(character))
        if not self.matrixChars.BACKWARDS:
            matrixList.reverse()
        return matrixList
        
    def display_char(self, character):
        """ Display a single character. """
        if not character:
            return
        matrixCharacter = self.translate_char(character)
        self.write_matrix_raw(matrixCharacter)

    def display_string_one_by_one(self, message, timeout = 1, clear = True):
        """ Displays the given message, one character at a time.
            
            'timeout' defines the time for which each character is
            displayed. If set to 0, the first character will be displayed
            forever.
            If clear is True, the matrix is cleared after
            displaying all of message.
        """
        if timeout < 0:
            timeout = 1
            print('WARNING: Parameter timeout has to be non-negative. Setting it to 1.',
                file = sys.stderr)

        matrixList = self.translate_string(message)
        if timeout == 0 and matrixList != []:
            self.write_matrix_raw(matrixList[0])
        else:
            matrixList = self.translate_string(message)
            for matrixCharacter in matrixList:
                self.write_matrix_raw(matrixCharacter)
                sleep(timeout)
        if clear:
            self.clear()

    def _scroll_by_one(self, outputList, timeout):
        """ Helper method to scroll a list of matrix characters by one
            column.
        """
        if self.matrixChars.BACKWARDS:
            self.write_matrix_raw(outputList[0:8])
            outputList.append(outputList[0])
            del(outputList[0])
        else:
            outputList.reverse()
            outputList.append(outputList[0])
            outputList.reverse()
            self.write_matrix_raw(outputList[-8:])
            del(outputList[-1])
        sleep(timeout)
        return outputList

    def display_string_scrolling(self, message, timeout = 0.1,
        turnaround = True, backwards = False, clear = True):
        """ Displays the given message, scrolling it column by column.

            'timeout' defines the time between switching from one column
            to the next and has to be a positive (floating point) number.
            If turnaround is True, the message is repeated over and over.
            XXX: How to stop it then???
            Otherwise, the display is cleared after displaying all of
            'message'.
        """

        if timeout <= 0:
            timeout = 0.1
            print('WARNING: Parameter timeout has to be non-negative. Setting it to 0.1.',
                file = sys.stderr)

        matrixList = self.translate_string(message)
        if matrixList == []:
            return

        outputList = []
        for matrixCharacter in matrixList:
            outputList.extend(matrixCharacter)

        if turnaround:
            # XXX: Think of proper condition to end this loop.
            while True:
                outputList = self._scroll_by_one(outputList,
                                                 timeout)
        else:
            numColumns = len(outputList)
            column = numColumns - 8
            while column > 0:
                outputList = self._scroll_by_one(outputList,
                                                 timeout)
                column -= 1

        if clear:
            sleep(timeout)
            self.clear()
