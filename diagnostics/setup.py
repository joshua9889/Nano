from distutils.core import setup
from Cython.Build import cythonize

modules=[
    "src.py"
    ]

setup(
    ext_modules = cythonize(modules)
    )
