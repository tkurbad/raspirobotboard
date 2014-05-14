#!/usr/bin/python2

import RPi.GPIO as GPIO

from time import sleep

from EightByEight import EightByEight
from ESpeak import ESpeak
from Ranger import Ranger

## Define some standard variables

# Serial port setup
SER_DEVICE          = '/dev/ttyAMA0'
SER_BAUD            = 9600

# SRF02 range finder addresses
FRONT_RANGER_ADDR   = 3
BACK_RANGER_ADDR    = None
LEFT_RANGER_ADDR    = 2
RIGHT_RANGER_ADDR   = 1

# GPIO setup - motors
LEFT_GO_PIN         = 17
LEFT_DIR_PIN        = 4
RIGHT_GO_PIN        = 10
RIGHT_DIR_PIN       = 25

# GPIO setup - LEDs
LED1_PIN            = 7
LED2_PIN            = 8

# GPIO setup - odometers / open collectors / switches
#               * open collector outputs provide power
#               * switches act as inputs
#               * right side odometer uses OC1/SW1, left is OC2/SW2
#  !!! IMPORTANT! See schematics/RaspiRobotBoard_Modifications.txt !!!
USE_ODOMETERS       = True
RIGHT_POWER_PIN     = OC1_PIN = 22
RIGHT_DETECT_PIN    = SW1_PIN = 11
LEFT_POWER_PIN      = OC2_PIN = 27
LEFT_DETECT_PIN     = SW2_PIN = 9

# espeak setup - speech output
USE_ESPEAK          = True
ESPEAK_VOICE        = 'default'
ESPEAK_CAPITALS     = None
ESPEAK_PITCH        = None
ESPEAK_PUNCTUATION  = None
ESPEAK_RATE         = 170
ESPEAK_VOLUME       = 200
ESPEAK_WORDGAP      = 1

# Adafruit LED matrix
USE_ADAFRUIT_8x8    = True
ADAFRUIT_ADDRESS    = 0x70


class TorBot:
    """ Control the TorBot robot platform using Python on a
        Raspberry PI. """

    def __init__(self):
        """ Initialize some parameters. """
        
        # Silence GPIO warnings
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(LEFT_GO_PIN, GPIO.OUT)
        GPIO.setup(LEFT_DIR_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_GO_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_DIR_PIN, GPIO.OUT)

        GPIO.setup(LED1_PIN, GPIO.OUT)
        GPIO.setup(LED2_PIN, GPIO.OUT)
        GPIO.setup(OC1_PIN, GPIO.OUT)
        GPIO.setup(OC2_PIN, GPIO.OUT)

        pud = GPIO.PUD_OFF
        if USE_ODOMETERS:
            pud = GPIO.PUD_DOWN
        GPIO.setup(SW1_PIN, GPIO.IN, pull_up_down = pud)
        GPIO.setup(SW2_PIN, GPIO.IN, pull_up_down = pud)

        self.fRanger = None
        self.bRanger = None
        self.lRanger = None
        self.rRanger = None

        if FRONT_RANGER_ADDR is not None:
            self.fRanger = Ranger(rangerAddress = FRONT_RANGER_ADDR,
                                serDevice = SER_DEVICE,
                                baud = SER_BAUD)
        if BACK_RANGER_ADDR is not None:
            self.bRanger = Ranger(rangerAddress = BACK_RANGER_ADDR,
                                serDevice = SER_DEVICE,
                                baud = SER_BAUD)
        if LEFT_RANGER_ADDR is not None:
            self.lRanger = Ranger(rangerAddress = LEFT_RANGER_ADDR,
                                serDevice = SER_DEVICE,
                                baud = SER_BAUD)
        if RIGHT_RANGER_ADDR is not None:
            self.rRanger = Ranger(rangerAddress = RIGHT_RANGER_ADDR,
                                serDevice = SER_DEVICE,
                                baud = SER_BAUD)
                                
        if USE_ESPEAK:
            self.speech = ESpeak(voice = ESPEAK_VOICE,
                                capitals = ESPEAK_CAPITALS,
                                pitch = ESPEAK_PITCH,
                                punctuation = ESPEAK_PUNCTUATION,
                                rate = ESPEAK_RATE,
                                volume = ESPEAK_VOLUME,
                                wordgap = ESPEAK_WORDGAP)

        if USE_ADAFRUIT_8x8:
            self.ledMatrix = EightByEight(address=ADAFRUIT_ADDRESS)
            self.ledMatrix.clear()

    ## motor control ###################################################

    def set_motors(self, leftGo = 0, leftDir = 0,
                rightGo = 0, rightDir = 0):
        """ Set the motors in motion. """
        GPIO.output(LEFT_GO_PIN, leftGo)
        GPIO.output(LEFT_DIR_PIN, leftDir)
        GPIO.output(RIGHT_GO_PIN, rightGo)
        GPIO.output(RIGHT_DIR_PIN, rightDir)

    def stop(self):
        """ Stop all motors. """
        self.set_motors()

    def forward(self, seconds = 0):
        """ Move forward [for seconds]. """
        self.set_motors(1, 0, 1, 0)
        if seconds > 0:
            sleep(seconds)
            self.stop()
 
    def reverse(self, seconds = 0):
        """ Move backward [for seconds]. """
        self.set_motors(1, 1, 1, 1)
        if seconds > 0:
            sleep(seconds)
            self.stop()
    
    def left(self, seconds = 0):
        """ Turn to the left [for seconds].
            Left motor: stop
            Right motor: forward
        """
        self.set_motors(0, 0, 1, 0)
        if seconds > 0:
            sleep(seconds)
            self.stop()

    def right(self, seconds = 0):
        """ Turn to the right [for seconds].
            Left motor: forward
            Right motor: stop
        """
        self.set_motors(1, 0, 0, 0)
        if seconds > 0:
            sleep(seconds)
            self.stop()

    def hard_left(self, seconds = 0):
        """ Turn inplace to the left [for seconds].
            Left motor: reverse
            Right motor: forward
        """
        self.set_motors(1, 1, 1, 0)
        if seconds > 0:
            sleep(seconds)
            self.stop()

    def hard_right(self, seconds = 0):
        """ Turn inplace to the right [for seconds].
            Left motor: forward
            Right motor: reverse
        """
        self.set_motors(1, 0, 1, 1)
        if seconds > 0:
            sleep(seconds)
            self.stop()

    ## LEDs ############################################################

    def set_leds(self, led1State = False, led2State = False):
        """ Switch on or off both onboard LEDs. """
        GPIO.output(LED1_PIN, led1State)
        GPIO.output(LED2_PIN, led2State)

    def set_led1(self, state = False):
        """ Switch onboard LED 1. """
        GPIO.output(LED1_PIN, state)

    def set_led2(self, state = False):
        """ Switch onboard LED 2. """
        GPIO.output(LED2_PIN, state)

    ## SW / OC #########################################################

    def sw_states(self):
        """ Return the state of both switches as a tuple.
            Possible values are
            1: Open
            0: Closed

            Returns None when odometers are enabled.
        """
        if not USE_ODOMETERS:
            return (GPIO.input(SW1_PIN), GPIO.input(SW2_PIN))

    def sw1_closed(self):
        """ Is switch 1 closed?
        
            Returns None when odometers are enabled.        
        """
        if not USE_ODOMETERS:
            return not GPIO.input(SW1_PIN)

    def sw2_closed(self):
        """ Is switch 2 closed?
        
            Returns None when odometers are enabled.        
        """
        if not USE_ODOMETERS:
            return not GPIO.input(SW2_PIN)

    def set_ocs(self, oc1State = False, oc2State = False):
        """ Switch on or off both open collector outputs.

            Does nothing when odometers are enabled.
        """
        if not USE_ODOMETERS:
            GPIO.output(OC1_PIN, oc1State)
            GPIO.output(OC2_PIN, oc2State)

    def set_oc1(self, state = False):
        """ Switch open collector output 1.

            Does nothing when odometers are enabled.
        """
        if not USE_ODOMETERS:
            GPIO.output(OC1_PIN, state)

    def set_oc2(self, state = False):
        """ Switch open collector output 2.

            Does nothing when odometers are enabled.
        """
        if not USE_ODOMETERS:
            GPIO.output(OC2_PIN, state)

    ## odometers #######################################################

    def power_odometers(self, onoff = True):
        """ Power up odometers.
            onoff == True: Power on.
            onoff == False: Power off.
        
            Does nothing when USE_ODOMETERS is False.
        """
        if USE_ODOMETERS:
            GPIO.output(LEFT_POWER_PIN, onoff)
            GPIO.output(RIGHT_POWER_PIN, onoff)

    def get_odo_left(self):
        """ Get state of left odometer. Return values.

                1 : High. Phototransistor dark.
                0 : Low.  Phototransistor illuminated.

            Returns None when odometers are disabled.
        """
        if USE_ODOMETERS:
            return GPIO.input(LEFT_DETECT_PIN)

    def get_odo_right(self):
        """ Get state of right odometer. Return values.

                1 : High. Phototransistor dark.
                0 : Low.  Phototransistor illuminated.

            Returns None when odometers are disabled.
        """
        if USE_ODOMETERS:
            return GPIO.input(RIGHT_DETECT_PIN)

    ## espeak ##########################################################

    def speak(self, message):
        """ Speak using TTS. """
        if USE_ESPEAK:
            return self.speech.speak(message)

    ## test ############################################################

    def test(self, motors = True, leds = True, rangers = True,
            switches = True, opencollectors = True, odometers = True,
            matrix = True, speech = True):
        """ Interactively test various functions of the robot board. """
        if motors:
            if odometers and USE_ODOMETERS:
                raw_input("Power up odometers")
                self.power_odometers(True)

            raw_input("Move forward")
            self.forward(1)

            raw_input("Move left")
            self.left(1)
    
            raw_input("Move right")
            self.right(1)
    
            raw_input("Move hard left")
            self.hard_left(1)
    
            raw_input("Move hard right")
            self.hard_right(1)
    
            raw_input("Move backwards")
            self.reverse()
    
            raw_input("Stop")
            self.stop()
    
            if odometers and USE_ODOMETERS:
                raw_input("Power down odometers")
                self.power_odometers(False)

        if leds:
            raw_input("Turn on LEDs")
            self.set_leds(True, True)

            raw_input("Turn off LED1")
            self.set_led1(False)
    
            raw_input("Turn off LED2")
            self.set_led2(False)

        if rangers:
            if self.fRanger is not None:
                raw_input("Measure front obstacle distance")
                print self.fRanger.get_range_cm()
    
            if self.lRanger is not None:
                raw_input("Measure left obstacle distance")
                print self.lRanger.get_range_cm()
    
            if self.rRanger is not None:
                raw_input("Measure right obstacle distance")
                print self.rRanger.get_range_cm()

        if opencollectors:
            if not USE_ODOMETERS:
                raw_input("Turn on collector output 1")
                self.set_oc1(True)
                raw_input("Turn on collector output 2")
                self.set_oc2(True)
                raw_input("Turn off collector outputs")
                self.set_ocs(False, False)
            else:
                print "Odometers are enabled, not testing open collectors."

        if switches:
            if not USE_ODOMETERS:
                raw_input("Test switch 1")
                print self.sw1_closed()
                raw_input("Test switch 1 again")
                print self.sw1_closed()
                raw_input("Test switch 2")
                print self.sw2_closed()
                raw_input("Test switch 2 again")
                print self.sw2_closed()
            else:
                print "Odometers are enabled, not testing switches."

        # Temporary
        if odometers and USE_ODOMETERS:
            raw_input("Power up odometers")
            self.power_odometers(True)
            raw_input("Get left odometer")
            print self.get_odo_left()
            raw_input("Get left odometer again")
            print self.get_odo_left()
            raw_input("Get right odometer")
            print self.get_odo_right()
            raw_input("Get right odometer again")
            print self.get_odo_right()
            raw_input("Shut down odometers")
            self.power_odometers(False)

        if matrix:
            raw_input("Test LED Matrix output")
            for x in range(0, 8):
                for y in range(0, 8):
                    self.ledMatrix.setPixel(x, y)
                    sleep(0.05)
                sleep(0.5)
            raw_input("Clear LED matrix")
            self.ledMatrix.clear()

        if speech:
            raw_input("Test speech")
            self.speak("Hello, my name is Torbot. I am an autonomous robot.")

        raw_input("End of test")
