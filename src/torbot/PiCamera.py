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
        if crop is not None:
            self.crop = crop
        if resolution is not None:
            self.resolution = resolution
        if framerate is not None:
            self.framerate = framerate
        if brightness is not None:
            self.brightness = brightness
        if contrast is not None:
            self.contrast = contrast
        if saturation is not None:
            self.saturation = saturation
        if awb_mode is not None:
            self.awb_mode = awb_mode
        if exposure_compensation is not None:
            self.exposure_compensation = exposure_compensation
        if exposure_mode is not None:
            self.exposure_mode = exposure_mode
        if iso is not None:
            self.iso = iso
        if meter_mode is not None:
            self.meter_mode = meter_mode
        if image_effect is not None:
            self.image_effect = image_effect
        if color_effects is not None:
            self.color_effects = color_effects
        if rotation is not None:
            self.rotation = rotation
        if hflip is not None:
            self.hflip = hflip
        if vflip is not None:
            self.vflip = vflip

    def capture_stream(self, outputFormat = 'jpeg'):
        """ Capture a still in the given output format.
            Return a stream of the capture.
        """
        stream = BytesIO()
        if outputFormat not in ['jpeg', 'png', 'gif', 'bmp', 'yuv', 'rgb',
                                'rgba', 'bgr', 'bgra', 'raw']:
            print('WARNING: Unknown picture format specified. Defaulting to jpeg.',
                file = sys.stderr)
        self.capture(stream, outputFormat)
        return stream
