###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
import numpy as np  # type: ignore
# import platform
from .wrappers import printf
from .Base import Base


class BGR(object):
    """Fake class"""

    @printf
    def __init__(self, sz):
        # constructor
        self.array = np.random.rand(*sz)

    @printf
    def truncate(self, num):
        # refreshes the fake image
        self.array = np.random.rand(*self.array.shape)


class PiCamera(Base):
    """Fake class"""
    resolution = (0, 0)
    AWB_MODES = {
        'off': 0,
        'auto': 1,
        'sunlight': 2,
        'cloudy': 3,
        'shade': 4,
        'tungsten': 5,
        'fluorescent': 6,
        'incandescent': 7,
        'flash': 8,
        'horizon': 9,
    }

    METER_MODES = {
        'average': 0,
        'spot': 1,
        'backlit': 2,
        'matrix': 3,
    }

    EXPOSURE_MODES = {
        'off': 0,
        'auto': 1,
        'night': 2,
        'nightpreview': 3,
        'backlight': 4,
        'spotlight': 5,
        'sports': 6,
        'snow': 7,
        'beach': 8,
        'verylong': 9,
        'fixedfps': 10,
        'antishake': 11,
        'fireworks': 12,
    }

    def __init__(self, resolution=None):
        Base.__init__(self, self.__class__)

        self.closed = False
        self.awb_mode = 'auto'
        self.exposure_mode = 'auto'
        self.meter_mode = 'average'
        self.preview = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.closed = True

    @printf
    def capture(self, output, format=None, use_video_port=False, resize=None, splitter_port=0, **options):
        # this does nothing
        pass

    @printf
    def start_preview(self, **options):
        # this does nothing
        self.preview = PiRenderer()

    @printf
    def stop_preview(self, **options):
        # this does nothing
        self.preview = None


class PiRenderer(object):
    """Fake class"""
    pass


class array(object):
    """Fake class"""

    @staticmethod
    def PiRGBArray(cam, size):
        return BGR(size)
