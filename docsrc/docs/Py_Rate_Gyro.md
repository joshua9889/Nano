# **Rate Gyro (45-2004)**
-----
The Rate Gyro is used to detect the rate of rotation. When the Rate Gyro is completely still, the returned reading is 1.4V which produces a reading of 280° ±2°. With the sensor idle at 280° a Counter Clockwise (CCW) rotation will increase the value of the reading and then return to 280° once movement is stopped. A Clockwise (CW) rotation of the gyro will cause a decrease in the return value and return to 280° once the sensor is no longer moving. The readings are accurate to the degree.

>**Sensor Type** : Three Wire Analog  
>**Dimensions** : 32mm x 32mm x 12mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Analog 0V - 5V  
>[Rate Gyro Visual Programming Blocks](Blk_Rate_Gyro.md)

**List of available functions:**  

* [**Fusion.analog(*driver*, *port*)**](Py_Rate_Gyro.md#fusionanalogdriver-port)
* [**read()**](Py_Rate_Gyro.md#read)

![](img/Sensor_Diagrams/RateGyro.png)

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
    rate_gyro_A0 = Fusion.analog(f, f.A0)
    
## **read()**
>### Definition
>>Returns the rate of rotation of the sensor. When the sensor stops moving the value will go back to 280.
>>
>>* Value of 280 indicates no rotation detected in either direction.
>
>### Parameters
>>**None**
>
>### Returns
>>***Rate of Rotation*** : int (0 - 1023)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    rate_gyro_A0 = Fusion.analog(f, f.A0)
    print rate_gyro_A0.read()

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Rate Gyro