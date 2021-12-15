#!/bin/bash
sudo apt-get update 
sudo apt-get install --fix-missing
sudo apt-get install libjpeg8-dev imagemagick libv4l-dev -y
sudo ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h