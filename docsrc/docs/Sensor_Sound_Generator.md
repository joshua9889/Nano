# **Sound Generator (45-2016)**
-----
The Sound Generator can generate a sound based on volume, pitch and duration. This sensor also can overwrite settings during a tone to change the pitch, volume, or extend the duration of the tone.

>**Sensor Type** : Four Wire I2C  
>**Default I2C Address** : 0x34  
>**Sensor ID Code** : 0x53  
>**Dimensions** : 32mm x 32mm x 19mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Logic 0 - 0V, Logic 1 - 5V  
>**I2C Bus Speed** : 100kHz max  
>**I2C Address Change Option** : Yes (Even Number 0x10 - 0xEE)  

>[Sound Generator Visual Programming Blocks](Blk_Sound_Generator.md)  
>[Sound Generator Python Library Information](Py_Sound_Generator.md)  

![](img/Sensor_Diagrams/Sound.png)

<table style="width:50%" align="center" border="2">
    <tr><th><p align="center">Register</p></th><th><p align="center">Function</p></th></tr>
    <tr><td><p align="center">0x00</p></td><td><p align="left">Sensor Firmware Revision</p></td></tr>
    <tr><td><p align="center">0x01</p></td><td><p align="left">Manufacturer Code</p></td></tr>
    <tr><td><p align="center">0x02</p></td><td><p align="left">Sensor ID Code</p></td></tr>
    <tr><td><p align="center">0x03</p></td><td><p align="left">Not Used</p></td></tr>
    <tr><td><p align="center">0x04</p></td><td><p align="left">Sound level</p></td></tr>
    <tr><td><p align="center">0x05/0x06</p></td><td><p align="left">Pitch (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x07</p></td><td><p align="left">Duration</p></td></tr>
</table>

The order if the 4 control bytes, Sound Level, Pitch (lsb), Pitch (msb) and Duration are arranged such that a signal 4 byte write can be used to initiate a tone.

## **Sound Level**
>Controls the amplitude of the output signal from 0 to 3 where 0 is the quietest and 3 is the loudest.

## **Pitch**
>Consisting of 2 bytes to make a word, the Pitch controls the frequency of the output in increments of 1Hz. The frequencies range from 1Hz to 65kHz, although operation over 5kHz is not recommended and may damage the device. The speaker resonates at about 2kHz, so the speaker will sound much louder at this frequency.

## **Duration**
>This controls the duration of the tone in increments of 10 msec. The duration of the tone can range from 10 msec – 2.55 sec. The duration of the tone begins a countdown and will stop when the counter reaches 0. The duration may be updated at anytime to extend the length of a tone past 2.55 sec.