from distutils.core import setup
from Cython.Build import cythonize

modules=[
    "coreDeviceInterface.py",
    "coreLegacyModule.py",
    "coreMotorController.py",
    "coreServoController.py",
    "driver.py",
    "ht_Accelerometer.py",
    "ht_Angle.py",
    "ht_Barometric.py",
    "ht_Color.py",
    "ht_Compass.py",
    "ht_EOPD.py",
    "ht_ForceSensor.py",
    "ht_IRreciever.py",
    "ht_IRseekerV2.py",
    "ht_Magnetic.py",
    "nxt_Light.py",
    "nxt_Sound.py",
    "nxt_Touch.py",
    "nxt_Ultrasonic.py"
    ]

setup(
    ext_modules = cythonize(modules)
    )
