# **Optical Distance Sensor (45-2006)**
-----
The Optical Distance Sensor (ODS) is an analog sensor that uses electro optical proximity detection to calculate distance from an object based on the intensity of the light. This sensor can calculate distances between 1cm to 15cm. Lighter colored objects will return a more accurate and consistent reading, the material also plays a part on the returned value. Try different colors and material to see what works best for you. The ODS can be used for object detection, line detection and the difference between light and dark.

>**Sensor Type** : Three Wire Analog  
>**Dimensions** : 32mm x 32mm x 12mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Analog 0V - 5V  
>[Optical Distance Sensor Visual Programming Blocks](Blk_Optical_Distance_Sensor.md)

**List of available functions:**  

* [**Fusion.analog(*driver*, *port*)**](Py_Optical_Distance_Sensor.md#fusionanalogdriver-port)
* [**read()**](Py_Optical_Distance_Sensor.md#read)

![](img/Sensor_Diagrams/ODS.png)

## **Fusion.analog(*driver*, *port*)**
>### Definition
>>The following class provides a wrapper for the analog function to tie sensor names directly to the port and read all in one simple motion. 
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**f**)  
>>***port*** : Analog port the sensor is connected to A0 - A7
>
>### Returns
>>**Analog Object**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    ods_A0 = Fusion.analog(f, f.A0)
    
## **read()**
>### Definition
>>The optical element works by emitting pulsed visible light from on LED and receiving pulsed visible light to the photodiode. The optical value can detect objects within 15cm. As an object approaches the optical element the returned value will increase at an exponential rate.
>
>### Parameters
>>**None**
>
>### Returns
>>***Proximity*** : int (0 - 1023)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    ods_A0 = Fusion.analog(f, f.A0)
    print ods_A0.read()

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Optical Distance Sensor