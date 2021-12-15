# **Range Sensor (45-2008)**
-----
The Range Sensor combines ultrasonic and optical measuring elements to obtain a reading between 1cm and 255cm. The ultrasonic accurately measures distance to a target up to 255cm away, but it losses accuracy if the object is closer than 5cm. This is where the optical sensor comes into play as it can measure from 1cm out to about 7cm. The target shape and surface material will influence the detectable range.

>**Sensor Type** : Four Wire I2C  
>**Default I2C Address** : 0x28  
>**Sensor ID Code** : 0x55  
>**Dimensions** : 56mm x 32mm x 17mm  
>**Mounting Holes** : 48mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Logic 0 - 0V, Logic 1 - 5V  
>**I2C Bus Speed** : 100kHz max  
>**I2C Address Change Option** : Yes (Even Number 0x10 - 0xEE)

>[Range Sensor Visual Programming Blocks](Blk_Range_Sensor.md)  
>[Range Sensor Python Library Information](Py_Range_Sensor.md)  

![](img/Sensor_Diagrams/Range.png)

<table style="width:50%" align="center" border="2">
    <tr><th><p align="center">Register</p></th><th><p align="center">Function</p></th></tr>
    <tr><td><p align="center">0x00</p></td><td><p align="left">Sensor Firmware Revision</p></td></tr>
    <tr><td><p align="center">0x01</p></td><td><p align="left">Manufacturer Code</p></td></tr>
    <tr><td><p align="center">0x02</p></td><td><p align="left">Sensor ID Code</p></td></tr>
    <tr><td><p align="center">0x03</p></td><td><p align="left">Not Used</p></td></tr>
    <tr><td><p align="center">0x04</p></td><td><p align="left">Ultrasonic reading (cm)</p></td></tr>
    <tr><td><p align="center">0x05</p></td><td><p align="left">Optical Reading</p></td></tr>
</table>

## **Ultrasonic**
>The ultrasonic element works by one of the transducers emitting a sound wave and the other receiving the sound wave. This reading is accurate between 5cm and approximately 255cm. Since the value returned is in units of centimeters, the return is linear.

## **Optical**
>The optical element works by emitting infrared light from on LED and receiving infrared light to the other LED. The optical value can detect objects within 15cm. As an object approaches the optical element the returned value will increase at an exponential rate.