from distutils.core import setup
from Cython.Build import cythonize

modules=[
    "analog.py",
    "color.py",
    "colorBeacon.py",
    "compass.py",
    "digital.py",
    "driver.py",
    "intGyro.py",
    "locator360.py",
    "range.py",
    "seekerV3.py",
    "sound.py",
    "usbGamepad.py"
    ]

setup(
    ext_modules = cythonize(modules)
    )
