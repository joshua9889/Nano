# **Color Beacon (45-2019)**
-----
The Color Beacon is used to display one of seven colors or any set custom color based on RGB values.  
The beacon can also indicate **Red**/**Blue** team colors with the use of a magnet. There is no code or setup needed to operate as a team indicator. There is a Hall Effect sensor located on the left side of the sensors (wire pointed toward you). By holding a magnet over the top of the sensor it will blink green. After the green blink the beacon will be set to **Red**, **Blue** or **Off**. This can be done at any time and will overwrite any custom color or color number. When the beacon is **Red** or **Blue** from the Hall Effect sensor, it will be locked in that mode until turned **Off** using a magnet or disconnecting the sensor.

* Connect via **I2C** port.

>[Color Beacon Python Library Information](Py_Color_Beacon.md)

**List of available blocks:**  

* [**Set Color**](Blk_Color_Beacon.md#set-color)
* [**Set Custom Color**](Blk_Color_Beacon.md#set-custom-color)

![](img/Sensor_Diagrams/ColorBeacon.png)
  
## **Set Color**
>Set the color of the Color Beacon to one of the preset colors.

<table style="width:30%" align="center" border="2">
    <tr><th><p align="center">Number</p></th><th><p align="center">Color</p></th></tr>
    <tr><td><p align="center">0</p></td><td><p align="center">Off</p></td></tr>
    <tr><td><p align="center">1</p></td><td><p align="center">Red</p></td></tr>
    <tr><td><p align="center">2</p></td><td><p align="center">Green</p></td></tr>
    <tr><td><p align="center">3</p></td><td><p align="center">Yellow</p></td></tr>
    <tr><td><p align="center">4</p></td><td><p align="center">Blue</p></td></tr>
    <tr><td><p align="center">5</p></td><td><p align="center">Purple</p></td></tr>
    <tr><td><p align="center">6</p></td><td><p align="center">Teal</p></td></tr>
    <tr><td><p align="center">7</p></td><td><p align="center">White</p></td></tr>
</table>
    
>### Block:
>
><img src="../img/Intermediate_Blocks/Color_Beacon/SetColor.PNG" width="350">
>
>### Code Produced:
>
>>Setup:
>>>
    beacon = Fusion.colorBeacon(f)

>>Code:
>>>
    beacon.setColor(1)

>### Example:
>
><img src="../img/Intermediate_Blocks/Color_Beacon/SetColor_Example.PNG" width="240">
>
>>Code:
>>>
    import Fusion
    import time
    f = Fusion.driver()
    beacon = Fusion.colorBeacon(f)
    beacon.setColor(1)
    time.sleep(1)
    beacon.setColor(4)
    time.sleep(1)
    beacon.setColor(3)
    time.sleep(1)
    beacon.setColor(0)

## **Set Custom Color**
>Set a custom color using Red, Green and Blue (RGB) values.
>
>* RGB value ranges from **0** - **255**.
>* Some online sources may represent the color in hexadecimal (**0x00** - **0xFF**). Use a hexadecimal to decimal converter to get the appropriate value to enter. You can also use built-in Windows calculator, just change to programmer mode.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Color_Beacon/SetCustomColor.PNG" width="350">
>
>### Code Produced:
>
>>Setup:
>>>
    beacon = Fusion.colorBeacon(f)

>>Code:
>>>
    beacon.setCustomColor(100,0,255)
    
>### Example:
>
><img src="../img/Intermediate_Blocks/Color_Beacon/SetCustomColor_Example.PNG" width="480">
>
>>Setup:
>>>
    beacon = Fusion.colorBeacon(f)
    colour = Fusion.color(f)

>>Code:
>>>
    beacon.setCustomColor(colour.getRGBIndex()[0],colour.getRGBIndex()[1],colour.getRGBIndex()[2])

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Color Beacon