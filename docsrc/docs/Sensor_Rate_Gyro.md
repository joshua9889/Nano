# **Rate Gyro (45-2004)**
-----
The Rate Gyro is used to detect the rate of rotation. When the Rate Gyro is completely still, the returned reading is 1.4V which produces a reading of 280° ±2°. With the sensor idle at 280° a Counter Clockwise (CCW) rotation will increase the value of the reading and then return to 280° once movement is stopped. A Clockwise (CW) rotation of the gyro will cause a decrease in the return value and return to 280° once the sensor is no longer moving. The readings are accurate to the degree.

>**Sensor Type** : Three Wire Analog  
>**Dimensions** : 32mm x 32mm x 12mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Analog 0V - 5V 

>[Rate Gyro Visual Programming Blocks](Blk_Rate_Gyro.md)  
>[Rate Gyro Python Library Information](Py_Rate_Gyro.md)

![](img/Sensor_Diagrams/RateGyro.png)