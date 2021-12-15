# **Color Beacon (45-2019)**
-----
The Color Beacon is used to display one of seven colors or any set custom color based on RGB values.  
The beacon can also indicate **Red**/**Blue** team colors with the use of a magnet. There is no code or setup needed to operate as a team indicator. There is a Hall Effect sensor located on the left side of the sensors (wire pointed toward you). By holding a magnet over the top of the sensor it will blink green. After the green blink the beacon will be set to **Red**, **Blue** or **Off**. This can be done at any time and will overwrite any custom color or color number. When the beacon is **Red** or **Blue** from the Hall Effect sensor, it will be locked in that mode until turned **Off** using a magnet or disconnecting the sensor.

>**Sensor Type** : Four Wire I2C  
>**Default I2C Address** : 0x4C  
>**Sensor ID Code** : 0x75  
>**Dimensions** : 56mm x 32mm x 17mm  
>**Mounting Holes** : 48mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Logic 0 - 0V, Logic 1 - 5V  
>**I2C Bus Speed** : 100kHz max  
>**I2C Address Change Option** : Yes (Even Number 0x10 - 0xEE)  
>**LED Brightness** : 840 Red, 1680 Green, 420 Blue mcd (millicandela)  
>[Color Beacon Visual Programming Blocks](Blk_Color_Beacon.md)

**List of available functions:**  

* [**Fusion.ColorBeacon(*driver*, *addr*)**](Py_Color_Beacon.md#fusioncolorbeacondriver-addr)
* [**setColor(*color*)**](Py_Color_Beacon.md#setcolorcolor)
* [**setCustomColor(*red*, *green*, *blue*)**](Py_Color_Beacon.md#setcustomcolorred-green-blue)

![](img/Sensor_Diagrams/ColorBeacon.png)

## **Fusion.colorBeacon(*driver*, *addr*)**    
>### Definition
>>This class contains the necessary drivers for our Color Beacon and must be called at the beginning of the program before using any other class functions. 
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**f**)  
>>***addr*** : Enter an I2C address in hexadecimal if different from default 
>
>### Returns
>>**Color Beacon Object**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    beacon1 = Fusion.colorBeacon(f)
    beacon2 = Fusion.colorBeacon(f, 0x40)

## **setColor(*color*)**
>### Definition
>>Set the color of the LED using the number of the color.

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

>### Parameters  
>>***color*** : int (0 - 7)  
>
>### Returns  
>>**None**  
>
>### Example
>>
    import Fusion  
    import time  
    f = Fusion.driver()  
    beacon = Fusion.colorBeacon(f)  
    
    beacon.setColor(1)  
    time.sleep(1)  
    beacon.setColor(2)  
    time.sleep(1)  
    beacon.setColor(4)  
    time.sleep(1)  
    
## **setCustomColor(*red*, *green*, *blue*)**  
>### Definition
>>Set the color of the LED using a value 0-255 for **Red**, **Green** and **Blue**.
>
>### Parameters
>>***red*** : int (0 - 255)  
>>***green*** : int (0 - 255)  
>>***blue*** : int (0 - 255)
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    import time
    f = Fusion.driver()
    beacon = Fusion.colorBeacon(f)
    
    beacon.setCustomColor(255, 0, 0)
    time.sleep(1)
    beacon.setCustomColor(0, 255, 0)
    time.sleep(1)
    beacon.setCustomColor(0, 0, 255)
    time.sleep(1)

##  Questions?
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Color Beacon