#!/usr/bin/python2
# -*- coding: latin-1 -*-

from __future__ import print_function

import sys
from io import BytesIO

import picamera


class PiCamera(picamera.PiCamera):
    """ Main Raspberry PI Camera control class that extends the original
        PiCamera class.
    """

    def __init__(self):
        """ Initialize the camera. """
        # Check, if camera is connected
        self.camPresent = False
        try:
            super(PiCamera, self).__init__()
            self.camPresent = True
        except picamera.exc.PiCameraMMALError:
            print('ERROR: Camera could not be initialized. Please, check the cable.',
                file = sys.stderr)

    def set_parameters(self,
                       crop = None,
                       resolution = None,
                       framerate = None,
                       brightness = None,
                       contrast = None,
                       saturation = None,
                       awb_mode = None,
                       exposure_compensation = None,
                       exposure_mode = None,
                       iso = None,
                       meter_mode = None,
                       image_effect = None,
                       color_effects = None,
                       rotation = None,
                       hflip = None,
                       vflip = None):
        """ Set various camera parameters. """
        for parameter in [crop, resolution, framerate, brightness,
                            contrast, saturation, awb_mode,
                            exposure_compensation, exposure_mode, iso,
                            meter_mode, image_effect, color_effects,
                            rotation, hflip, vflip]:
            if parameter is not None:
                eval('self.%s = %s' % (parameter, parameter))

    def capture_stream(self, outFormat = 'jpeg'):
        """ Capture a still in the given output format.
            Return a stream of the capture.
        """
        stream = BytesIO
        if output not in ['jpeg', 'png', 'gif', 'bmp', 'yuv', 'rgb',
                            'rgba', 'bgr', 'bgra', 'raw']:
            print('WARNING: Unknown picture format specified. Defaulting to jpeg.',
                file = sys.stderr)
        self.capture(stream, outputFormat)
        return stream
