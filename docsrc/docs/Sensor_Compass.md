# **Compass (45-2003)**
-----
The Compass uses a magnetometer and an accelerometer to calculate heading data based on Earth’s magnetic field. The compass can return the heading data, accelerometer data and magnetometer data to the user. Anything that generates a magnetic field must be moved away from the sensor like power cables, motor or magnetic material. This must happen because during calibration the sensor will add an offset to account for other magnetic sources in the area.

>**Sensor Type** : Four Wire I2C  
>**Default I2C Address** : 0x24  
>**Sensor ID Code** : 0x63  
>**Dimensions** : 32mm x 32mm x 12mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Logic 0 - 0V, Logic 1 - 5V  
>**I2C Bus Speed** : 100kHz max  
>**I2C Address Change Option** : Yes (Even Number 0x10 - 0xEE) 

>[Compass Visual Programming Blocks](Blk_Compass.md)  
>[Compass Python Library Information](Py_Compass.md)

![](img/Sensor_Diagrams/Compass.png)

<table style="width:50%" align="center" border="2">
    <tr><th><p align="center">Register</p></th><th><p align="center">Function</p></th></tr>
    <tr><td><p align="center">0x00</p></td><td><p align="left">Sensor Firmware Revision</p></td></tr>
    <tr><td><p align="center">0x01</p></td><td><p align="left">Manufacturer Code</p></td></tr>
    <tr><td><p align="center">0x02</p></td><td><p align="left">Sensor ID Code</p></td></tr>
    <tr><td><p align="center">0x03</p></td><td><p align="left">Command</p></td></tr>
    <tr><td><p align="center">0x04/0x05</p></td><td><p align="left">Heading Data (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x06/0x07</p></td><td><p align="left">Accelerometer X Value (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x08/0x09</p></td><td><p align="left">Accelerometer Y Value (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x0A/0x0B</p></td><td><p align="left">Accelerometer Z Value (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x0C/0x0D</p></td><td><p align="left">Magnetometer X Value (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x0E/0x0F</p></td><td><p align="left">Magnetometer Y Value (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x10/0x11</p></td><td><p align="left">Magnetometer Z Value (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x12/0x13</p></td><td><p align="left">Accelerometer X Offset (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x14/0x15</p></td><td><p align="left">Accelerometer Y Offset (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x16/0x17</p></td><td><p align="left">Accelerometer Z Offset (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x18/0x19</p></td><td><p align="left">Magnetometer X Offset (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x1A/0x1B</p></td><td><p align="left">Magnetometer Y Offset (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x1C/0x1D</p></td><td><p align="left">Magnetometer Z Offset (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x1E/0x1F</p></td><td><p align="left">Magnetometer Tilt Coefficient (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x20/0x21</p></td><td><p align="left">Accelerometer Scale Coefficient (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x22/0x23</p></td><td><p align="left">Magnetometer X Scale Coefficient (lsb/msb)</p></td></tr>
    <tr><td><p align="center">0x24/0x25</p></td><td><p align="left">Magnetometer Y Scale Coefficient (lsb/msb)</p></td></tr>
</table>

<table style="width:70%" align="center" border="2">
    <tr><th><p align="center">Command</p></th><th><p align="center">Operation</p></th><th><p align="center">EEPROM Auto-Update</p></th></tr>
    <tr><td><p align="center">0x00</p></td><td><p align="left">Normal measurement mode</p></td><td><p align="center"></p></td></tr>
    <tr><td><p align="center">0x43</p></td><td><p align="left">Hard Iron Calibration mode</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x58</p></td><td><p align="left">Accelerometer X axis null</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x59</p></td><td><p align="left">Accelerometer Y axis null</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x5A</p></td><td><p align="left">Accelerometer Z axis null</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x47</p></td><td><p align="left">Accelerometer sensitivity/gain adjust</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x55</p></td><td><p align="left">Measure tilted up accelerometer value</p></td><td><p align="center"></p></td></tr>
    <tr><td><p align="center">0x44</p></td><td><p align="left">Measure tilted down accelerometer value</p></td><td><p align="center">X</p></td></tr>
    <tr><td><p align="center">0x57</p></td><td><p align="left">Write EEPROM Data</p></td><td><p align="center">X</p></td></tr>
</table>

During normal operation, the LED will blink briefly at 1Hz. During Hard Iron Calibration,the LED will blink at ½Hz. During tilt up and tilt down calibration the LED will be onduring a period of calibration measurement.

## **Hard Iron Calibration**
>Hard Iron Calibration is entered by setting the command location to 0x43. Once Hard Iron Calibration is active rotate the Compass 360°, making sure it does not tilt, for a period of 5 seconds. Once the rotation procedure is complete, the command location must be set to 0x00 to signal that calibration is complete. If the data collected during the rotation was good, the Compass will enter Normal Measurement Mode using the new calibration data. If the data collected during the rotation was not good, the command value will change to 0x46 and the Compass will enter Normal Measurement Mode using the previous calibration data.

## **Tilt Compensation**
>Tilt compensation is performed in two steps, tilt up and tilt down in that order. The first step is tilt up. To set the Compass up for tilt up measurement, the Compass should be pointed due North and set with the front of the device tiled up by approximately 20°. Then the command location should be set to 0x55 while the Compass is held perfectly still. Once the LED extinguishes itself, the command location will return to 0x00, indicating that tilt up data has been captured.  
>The second step is tilt down. To set the Compass up for tilt down measurement, the Compass should be pointed due North and set with the front of the device tilted down by approximately 20°. Then the command location should be set to 0x44 while the compass is held perfectly still. Once the LED extinguishes itself, the command location will return 0x00, indicating that tilt down data has been captured and the tilt compensation coefficient has been acquired.  
>If the two tilt steps are not performed in the correct order, or some other error is detected, the command location will be set to 0x46 and the Compass will enter Normal Measurement Mode using the previous tilt compensation coefficient.

## **Accelerometer Nulling**
>Accelerometer axis nulling is performed using the three axis null commands. For both the x and y axis nulling should be performed with the device set perfectly level. Setting the command location to 0x58 will update the accelerometer X axis offset. Setting the command location to 0x59 will update the accelerometer Y axis offset. For the Z axis nulling, the device should be set to be perfectly vertical. Setting the command location to 0x5A will update the accelerometer Z axis offset

## **Accelerometer Scale Coefficient**
>The Accelerometer Scale Coefficient is adjusted to be approximately 1mg/count. If greater measurement accuracy is required, the Accelerometer Scale Coefficient (fsb/lsb) may be set by the user. This can be simply done by setting the device perfectly vertical
and obtaining the accelerometer X value via registers 0x06 and 0x07.  
Once the Accelerometer Scale Coefficient has been adjusted, the 0x57 command should be issued to ensure the new value is recorded in EEPROM.

>>Example:  

>>**Step 1: Sensor Position**  
>>Set the sensor vertical so that the wires are pointing up in the air.

>>**Step 2: Find the X Value**  
>>Find the Accelerometer X Value - Register 0x06(lsb)/0x07(msb)  

>>Register 0x06 (lsb) = **0xE2**  
>>Register 0x07 (msb) = **0x04**  

>>X Value = msb:lsb = 0x04:0xE2 = **0x04E2** = **1250**

>>**Step 3: Calculating Scaling Value**  
>>Scaling Value = 1000/X Value = 1000/1250 = **.8**

>>**Step 4: Calculate Register Values**  
>>Register Values (lsb:fsb) = .8*256 = 204.8 = 204 = **0xCC** = **0x00CC**

>>**Step 5: Enter Values into Accelerometer Scale Coefficient Register**  
>>Accelerometer Scale Coefficient = 0x20(fsb)/0x21(lsb)

>>Register 0x20 (fsb) = **0xCC**  
>>Register 0x21 (lsb) = **0x00**

>>**Step 6: Saving the value to EEPROM**  
>>Enter a value of **0x57** (Write EEPROM Data) to the Command Register (0x03) to save the scaled value into EEPROM.






