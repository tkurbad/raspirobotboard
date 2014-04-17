from raspirobotboard import *
from time import sleep

import serial

class Ranger:

    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyAMA0', baudrate=9600, stopbits=2)

    def get_range(self):
        self.ser.write(chr(3) + chr(84))
        sleep(0.07)
        msg = self.ser.read(2)
        self.ser.flush()
        reading = ord(msg[0]) * 256 + ord(msg[1])
        return reading

    def get_min(self):
        self.ser.write(chr(3) + chr(95))
        sleep(0.07)
        msg = self.ser.read(2)
        self.ser.flush()
        reading = ord(msg[0]) * 256 + ord(msg[1])
        return reading

    def get_version(self):
        self.ser.write(chr(3)+chr(93))
        sleep(0.01)
        msg = self.ser.read(1)
        reading = ord(msg)
        return reading

rr = RaspiRobot()

sleep(2)
rr.forward(1)
rr.right(0.3)
rr.left(0.3)
rr.right(2)
rr.left(0.3)
rr.reverse(0.5)


range = Ranger()
print range.get_min()
print range.get_range()
print range.get_version()
