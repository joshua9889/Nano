#!/bin/bash
git clone https://github.com/hhernandez92/Nano.git /home/pi/Desktop/Nano
cd /home/pi/Desktop/Nano/FusionServer/Src
sudo npm i --production --unsafe-perm
cd ..
mv Src Build
cd ..
cd ..
sudo rm -R /usr/Fusion
sudo mv /home/pi/Desktop/Nano /usr/Fusion
sudo forever restart