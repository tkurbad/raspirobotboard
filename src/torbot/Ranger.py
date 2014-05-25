#!/usr/bin/python2

import serial

from time import sleep

class Ranger:
    """ Python class to access SRF02 ultrasonic rangers by a serial
        connection.
    """

    def __init__(self, rangerAddress = 0, serDevice = '/dev/ttyAMA0',
        baud = 9600):

        self.ser = serial.Serial(port = serDevice,
                        baudrate = baud,
                        stopbits = 2)
        self.rAddr = rangerAddress

    def _send_receive(self, command, lenResult = 2, delay = 0.1, openSer = True):
        """ Helper method to send a command to the ranger and return the
            answer of the device. """
        result = None
        if openSer:
            self.ser.open()
        self.ser.write(chr(self.rAddr) + chr(command))
        sleep(delay)
        if (lenResult is not None) and (lenResult > 0):
            result = self.ser.read(lenResult)
        self.ser.flush()
        if openSer:
            self.ser.close()
        return result

    def _distance(self, rawResult):
        """ Helper method to calculate two-byte encoded distances. """
        return ord(rawResult[0]) * 256 + ord(rawResult[1])

    def get_range_inch(self):
        """ Get the range in inches. """
        return self._distance(self._send_receive(83))

    def get_range_cm(self):
        """ Get the range in cm. """
        return self._distance(self._send_receive(84))

    def get_range_us(self):
        """ Get the range in microseconds. """
        return self._distance(self._send_receive(85))

    def get_min(self):
        """ Get the minimum range (according to auto tuning). """
        return self._distance(self._send_receive(95))

    def get_version(self):
        """ Get the software version of the ranger device. """
        result = self._send_receive(93, lenResult = 1)
        return ord(result)

    def set_address(self, newAddress):
        """ Set the ranger's I2C / serial address.
            !!! Be CAUTIOUS with this operation !!!
        """
        if (newAddress < 0) or (newAddress > 15):
            raise ValueError("New address outside range (0..15)")

        self.ser.open()
        self._send_receive(160, lenResult = 0, openSer = False)
        self._send_receive(170, lenResult = 0, openSer = False)
        self._send_receive(165, lenResult = 0, openSer = False)
        self._send_receive(newAddress, lenResult = 0, openSer = False)
        self.ser.close()
        return newAddress
