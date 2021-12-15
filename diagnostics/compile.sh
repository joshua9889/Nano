#!/bin/bash

sudo apt-get install python-dev --fix-missing
sudo apt-get install cython
sudo python setup.py build_ext --inplace 
sudo rm -r build 
sudo rm *.c 