#===============================================================================
# setup.py - Library Project control/collection File
#===============================================================================
# Revision History
#   08-Oct-19 <jwa> - Added comments and updated revision information
#
#===============================================================================   
#
from distutils.core import setup

fusion_files = ["*.so",
        "examples/ColorBeacon/*",
        "examples/ColorSensor/*",
        "examples/Compass/*",
        "examples/FusionController/*",
        "examples/IRLocator360/*",
        "examples/IRSeekerV3/*",
        "examples/LightSensor/*",
        "examples/MagneticSensor/*",
        "examples/OpticalDistanceSensor/*",
        "examples/RangeSensor/*",
        "examples/RateGyro/*",
        "examples/SoundGenerator/*",
        "examples/TouchSensor/*",
        "examples/UsbGamepad/*"]
         
core_files = ["*.so",
        "examples/CoreDeviceInterface/*",
        "examples/CoreLegacyModule/*",
        "examples/CoreMotorController/*",
        "examples/CoreServoController/*",
        "examples/detectDevices.py"]
         
virtual_files = ["*.so",
        "*.html",
        "examples/*",
        "css/*",
        "misc/*",
        "js/*",
        "mjpg_streamer/*"]

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'Fusion',
      version           = '2.5.0',
      author            = 'MyBot Engineering',
      author_email      = 'support@modernroboticsinc.com',
      description       = 'Library for MRI Fusion robot controller',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://modernroboticsinc.com',
      packages          = ['Fusion', 'CoreControl', 'VirtualGamepad'],
      package_data      = {'Fusion':fusion_files, 'CoreControl':core_files, 'VirtualGamepad':virtual_files},
)
