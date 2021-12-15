# **Color Sensor (45-2018)**
-----
The Color Sensor is used to detect the color of an object or a visible light source. Along with raw and adjusted RGB values, the device can also return a color number corresponding to a the colors listed below in the documentation. Calibration steps must be taken as needed based on the environment and ambient lighting for the most accurate readings. Maximum detection distance of the color sensor is approximately 7cm and it is recommended that during active mode the device is placed at a slight angle to avoid white light reflecting from the LED. 

>**Sensor Type** : Four Wire I2C  
>**Default I2C Address** : 0x3C  
>**Sensor ID Code** : 0x67  
>**Dimensions** : 32mm x 32mm x 11mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Logic 0 - 0V, Logic 1 - 5V  
>**I2C Bus Speed** : 100kHz max  
>**I2C Address Change Option** : Yes (Even Number 0x10 - 0xEE) 

>[Color Sensor Visual Programming Blocks](Blk_Color_Sensor.md)  
>[Color Sensor Python Library Information](Py_Color_Sensor.md)  

![](img/Sensor_Diagrams/ColorSensor.png)

<table style="width:50%" align="center" border="2">
    <tr><th><p align="center">Register</p></th><th><p align="center">Function</p></th></tr>
    <tr><td><p align="center">0x00</p></td><td><p align="left">Sensor Firmware Revision</p></td></tr>
    <tr><td><p align="center">0x01</p></td><td><p align="left">Manufacturer Code</p></td></tr>
    <tr><td><p align="center">0x02</p></td><td><p align="left">Sensor ID Code</p></td></tr>
    <tr><td><p align="center">0x03</p></td><td><p align="left">Command</p></td></tr>
    <tr><td><p align="center">0x04</p></td><td><p align="left">Color Number</p></td></tr>
    <tr><td><p align="center">0x05</p></td><td><p align="left">Red Value</p></td></tr>
    <tr><td><p align="center">0x06</p></td><td><p align="left">Green Value</p></td></tr>
    <tr><td><p align="center">0x07</p></td><td><p align="left">Blue Value</p></td></tr>
    <tr><td><p align="center">0x08</p></td><td><p align="left">White Value</p></td></tr>
    <tr><td><p align="center">0x09</p></td><td><p align="left">Color Index Number</p></td></tr>
    <tr><td><p align="center">0x0A</p></td><td><p align="left">Red Index</p></td></tr>
    <tr><td><p align="center">0x0B</p></td><td><p align="left">Green Index</p></td></tr>
    <tr><td><p align="center">0x0C</p></td><td><p align="left">Blue Index</p></td></tr>
    <tr><td><p align="center">0x0D</p></td><td><p align="left">Undefined</p></td></tr>
    <tr><td><p align="center">0x0E/0x0F</p></td><td><p align="left">Red Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x10/0x11</p></td><td><p align="left">Green Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x12/0x13</p></td><td><p align="left">Blue Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x14/0x15</p></td><td><p align="left">White Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x16/0x17</p></td><td><p align="left">Normalized Red Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x18/0x19</p></td><td><p align="left">Normalized Green Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x1A/0x1B</p></td><td><p align="left">Normalized Blue Reading (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x1C/0x1D</p></td><td><p align="left">Normalized White Reading (lsb/msb)</p></td></tr>
</table>

<table style="width:70%" align="center" border="2">
    <tr><th><p align="center">Command</p></th><th><p align="center">Operation</p></th><th><p align="center">EEPROM Auto-Update</p></th></tr>
    <tr><td><p align="center">0x00</p></td><td><p align="left">Active Mode (LED On)</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x01</p></td><td><p align="left">Passive Mode (LED Off)</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x35</p></td><td><p align="left">50 Hz Operating Frequency</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x36</p></td><td><p align="left">60 Hz Operating Frequency</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x42</p></td><td><p align="left">Black Level Calibration</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x43</p></td><td><p align="left">White Balance Calibration</p></td><td><p align="center">X</p></td></tr>
</table>

## **Commands**
>The command register may be set to any of the values from the command table. Once a command value is entered into the command register the value will be saved in the EEPROM.

>>**Active Measurement Mode**  
*Command = 0x00*  
In active measurement mode, the sensor takes a reading by illuminating a surface with a white LED and measuring the reflected light. Active mode is useful in identifying the color of a surface.

>>**Passive Measurement Mode**  
*Command = 0x01*  
In passive measurement mode, the sensor takes a reading without the white LED on. Therefore passive measurement mode is most useful in determining the color of a light source like an LED.

>>**Operating Frequency**  
*Command = 0x35(50Hz) or 0x36(60Hz)*  
The operating frequency is provided to enable the sampling to coincide with the normal flickering associated with artificial lighting. This helps to reduce signal noise and other issues. The operating frequency can be set to 50Hz or 60Hz.

>>**Black Level Calibration**  
*Command = 0x42*  
Black level calibration will run 64 measurement cycles to obtain an average value for each of the 3 color channels.  
During black level calibration, the sensor should be placed such that no surface is within 1.5m forward of the sensor elements. The calibration process last about 1.5 seconds and when calibration is complete, the LED will blink briefly and then the command register will be reset to 0x00 or 0x01 depending on the mode save in EEPROM.  
Black level calibration must be completed before white balance calibration.

>>**White Balance Calibration**  
*Command = 0x43*  
White balance calibration will run 64 measurement cycles to obtain and average value for each of the 3 color channels and are adjusted according to the black level calibration values.  
During white balance calibration, the sensor must be placed approximately 5cm (2in) from a white target. The target must be very white and not allow light to pass through the material. At least 3 sheets of high quality copy paper will make a satisfactory white surface for calibration. The calibration process last about 1.5 seconds and when calibration is complete, the LED will blink briefly and then the command register will be reset to 0x00 or 0x01 depending on the mode save in EEPROM.

## **Color Number**
>The color number register returns a single number representing the color estimate. The number corresponds to the following figure.  
>![](img/Sensor_Diagrams/ColorChart.png)

## **Color Values**
>The color values are returned separately as red, green, blue and white. The color value is a measure of the current detection levels for each primary color.

## **Color Index Number**
>The color index number is a single 6 bit number. Bits (5:4) encode the red signal level, bits (3:2) encode the green signal level and bits (1:0) encode the blue signal levels.

<table style="width:70%" align="center" border="2">
    <tr><th width="12%"><p align="center">D7</p></th><th width="12%"><p align="center">D6</p></th><th width="12%"><p align="center">D5</p></th><th width="12%"><p align="center">D4</p></th><th width="12%"><p align="center">D3</p></th width="12%"><th width="12%"><p align="center">D2</p></th><th width="12%"><p align="center">D1</p></th><th width="12%"><p align="center">D0</p></th></tr>
    <tr><td><p align="center">0</p></td><td><p align="center">0</p></td><td><p align="center">Red 1</p></td><td><p align="center">Red 0</p></td><td><p align="center">Green 1</p></td><td><p align="center">Green 0</p></td><td><p align="center">Blue 1</p></td><td><p align="center">Blue 0</p></td></tr>
</table>

## **Color Indexes**
>The color index will return the current analog signal levels for red, green and blue separately. The color with the greatest intensity is set as 0xFF while the other two colors indexes are set as a proportion of 0xFF.

## **Color Readings**
>The color reading registers return the current analog signal levels as 16 bits values forred, green, blue and white.

## **Color Normalized Readings**
>The color normalized readings will return the current levels for the color components and white channel that are adjusted for gain and offset.


