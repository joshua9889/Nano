# **Rate Gyro (45-2004)**
-----
The Rate Gyro is used to detect the rate of rotation. When the Rate Gyro is completely still, the returned reading is 1.4V which produces a reading of 280° ±2°. With the sensor idle at 280° a Counter Clockwise (CCW) rotation will increase the value of the reading and then return to 280° once movement is stopped. A Clockwise (CW) rotation of the gyro will cause a decrease in the return value and return to 280° once the sensor is no longer moving. The readings are accurate to the degree.

* Connect via analog port **A0** - **A7**.

>[Rate Gyro Python Library Information](Py_Rate_Gyro.md)

**List of available blocks:**  

* [**Read**](Blk_Rate_Gyro.md#read)

![](img/Sensor_Diagrams/RateGyro.png)

## **Read**
>Returns the current rate of rotation detected by the sensor.
>
>* Idle reading is **280°**.
>* **CW** rotation results in an increase (**+**) in reading.
>* **CCW** rotation results in a decrease (**-**) in reading.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Rate_Gyro/ReadRateGyro.PNG" width="300">
>
>### Code Produced:
>
>>Sensor Declaration:
>>>
    rate_gyro_A0 = Fusion.analog(f, f.A0)
    
>>Sensor Code:
>>>
    rate_gyro_A0.read()    

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Rate Gyro