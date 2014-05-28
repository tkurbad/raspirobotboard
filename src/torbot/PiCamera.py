#!/usr/bin/python2
# -*- coding: latin-1 -*-

from __future__ import print_function

import picamera


class PiCamera(picamera.PiCamera):
    """ Main Raspberry PI Camera control class that extends the original
        PiCamera class.
    """

    def __init__(self):
        """ Initialize some parameters. """
        # Check, if camera is connected
        self.camPresent = False
        try:
            super(PiCamera, self).__init__()
            self.camPresent = True
        except picamera.exc.PiCameraMMALError:
            print('ERROR: Camera could not be initialized. Please, check the cable.',
                file = sys.stderr)
