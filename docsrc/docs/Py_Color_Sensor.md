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

**List of available functions:**  

* [**Fusion.color(*driver*, *addr*)**](Py_Color_Sensor.md#fusioncolordriver-addr)
* [**colorSetup(*mode*, *rate*)**](Py_Color_Sensor.md#colorsetupmode-rate)
* [**getColorNumber()**](Py_Color_Sensor.md#getcolornumber)
* [**getRGBIndex()**](Py_Color_Sensor.md#getrgbindex)
* [**getColorValue())**](Py_Color_Sensor.md#getcolorvalue)
* [**getColorIndex())**](Py_Color_Sensor.md#getcolorindex)
* [**getColorReading()**](Py_Color_Sensor.md#getcolorreading)
* [**getColorNormalized()**](Py_Color_Sensor.md#getcolornormalized)
* [**blackBalance()**](Py_Color_Sensor.md#blackbalance)
* [**whiteBalance()**](Py_Color_Sensor.md#whitebalance)

![](img/Sensor_Diagrams/ColorSensor.png)

## **Fusion.color(*driver*, *addr*)**
>### Definition
>>This class contains the necessary drivers for our Color Sensor and must be called at the beginning of the program before using any other class functions. 
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**f**)  
>>***addr*** : Enter an I2C address in hexadecimal if different from default 
>
>### Returns
>>**Color Sensor Object**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    color1 = Fusion.color(f)
    color2 = Fusion.color(f, 0x40)

## **colorSetup(*mode*, *rate*)**
>### Definition
>>This function sets the mode and rate at which the readings are taken. The mode can be either **Active** or **Passive**.  
>>In **Active** mode, the white LED on the sensor is used to illuminate the surface that it is trying to detect. **Active** mode works best when the sensor is looking at an object at a slight angle so that the white light is not picked up by the sensor thus distorting the readings.  
>>In **Passive** mode, the sensor takes readings without the use of the white LED. **Passive** mode works best for detecting colored light much like that produced by the [Color Beacon](Py_Color_Beacon.md). The rate sets the operational frequency of the sensor that can be either 50Hz or 60Hz. The purpose of this is to eliminate any flickering from ambient light.
>>
>>* [Constants](Py_Constants.md)
>
>### Parameters
>>***mode*** : ACTIVE or PASSIVE   
>>***rate*** : FIFTY_HZ or SIXTY_HZ
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    color.colorSetup(color.ACTIVE, color.FIFTY_HZ)
    
## **getColorNumber()**  
>### Definition
>>This function returns the color number that was read by the sensor. The color number corresponds to the color line below. Some materials or the angle of incidence may affect the results. Test the sensor in your environment thoroughly before applying it to a design.
>>
>>![](img/Sensor_Diagrams/ColorChart.png)
>
>### Parameters
>>**None**
>
>### Returns
>>***Color Number*** : int (0 - 16)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    print color.getColorNumber()
    
## **getRGBIndex()**  
>### Definition
>>This function gets the analog values of the three primary color channels with an intensity correction whereby 0xFF is the strongest signal.
>
>### Parameters
>>**None**
>
>### Returns
>>***RGB Index*** : int [red, green, blue]
>
>### Example
>>The following example returns an array of size **3** and stores it into the variables **red**, **green** and **blue**.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    (red, green, blue) = color.getRGBIndex()
    print red
    
>>To collect a single value instead of the array, reference the index. This will print the **red** value.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    print color.getRGBIndex()[0]
    
## **getColorValue()**  
>### Definition
>>The color values are returned separately as red, green, blue and white. The color value is a measure of the current detection levels for each primary color.
>
>### Parameters
>>**None**
>
>### Returns
>>***Color Value*** : int [red, green, blue, white]
>
>### Example
>>The following example returns an array of size **3** and stores it into the variables **red**, **green**, **blue** and **white**.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    (red, green, blue, white) = color.getColorValue()
    print red
    
>>To collect a single value instead of the array, reference the index. This will print the **red** value.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    print color.getColorValue()[0]
    
## **getColorIndex()**  
>### Definition
>>The color index number is a single 6 bit number. Bits (5:4) encode the red signal level, bits (3:2) encode the green signal level and bits (1:0) encode the blue signal levels.
>>
| D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | Red 1 | Red 0 | Green 1 | Green 0 | Blue 1 | Blue 0 |
>>
>>* **Red** = 0x30
>>* **Green** = 0x0C
>>* **Blue** = 0x03
>
>### Parameters
>>**None**
>
>### Returns
>>***Color Index*** : int (0 - 63)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    print color.getColorIndex()
    
## **getColorReading()**
>### Definition
>>This function gets the analog value of the color channels in a 16-bit format. Therefore there is much more detail in the reading as compared to the index reading.
>
>### Parameters
>>**None**
>
>### Returns
>>***Color Reading*** : int (0 - 65535)
>
>### Example
>>The following example returns an array of size **3** and stores it into the variables **red**, **green**, **blue** and **white**.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    (red, green, blue, white) = color.getColorReading()
    print red
    
>>To collect a single value instead of the array, reference the index. This will print the **red** value.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    print color.getColorReading()[0]
    
## **getColorNormalized()**  
>### Definition
>>This function gets the analog value of the color channel adjusted by the calibration values.
>
>### Parameters
>>**None**
>
>### Returns
>>***Color Normalized*** : int [red, green, blue, white]
>
>### Example
>>The following example returns an array of size **3** and stores it into the variables **red**, **green**, **blue** and **white**.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    (red, green, blue, white) = color.getColorNormalized()
    print red
    
>>To collect a single value instead of the array, reference the index. This will print the **red** value.
>>
    import Fusion
    f = Fusion.driver()
    color = Fusion.color(f)
    print color.getColorNormalized()[0]
    
## **blackBalance()**
>### Definition
>>This function gathers data and calculates an average value for each of the three color channels. To calibrate the black balance, point the sensor so that there is no object within 5 feet (1.5m) forward of the sensor. Calibration takes approximately 1.5 seconds. This function must be called before the [whiteBalance()](#whitebalance) function because the white balance calculations are dependent on the black balance values.
>
>### Parameters
>>**None**
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    import time
    f = Fusion.driver()
    color = Fusion.color(f)
    color.blackBalance()
    time.sleep(2)
    
## **whiteBalance()**
>### Definition
>>This function gathers data and calculates and average value for each of the three color channels. Then the values are adjusted based on the readings from the [blackBalance()](#blackbalance) function. When calibrating, hold the sensor no more than 2 inches (5cm) away from a white target. The target must be very white, using a white board or 3 layers of high quality copy paper. Calibration takes approximately 1.5 seconds.
>
>### Parameters
>>**None**
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    import time
    f = Fusion.driver()
    color = Fusion.color(f)
    color.blackBalance()
    time.sleep(2)
    color.whiteBalance()
    time.sleep(2)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Color Sensor