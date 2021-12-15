# **Range Sensor (45-2008)**
-----
The Range Sensor combines ultrasonic and optical measuring elements to obtain a reading between 1cm and 255cm. The ultrasonic accurately measures distance to a target up to 255cm away, but it losses accuracy if the object is closer than 5cm. This is where the optical sensor comes into play as it can measure from 1cm out to about 7cm. The target shape and surface material will influence the detectable range.

* Connect via **I2C** port.

>[Range Sensor Python Library Information](Py_Range_Sensor.md)

**List of available blocks:**  

* [**Ultrasonic**](Blk_Range_Sensor.md#ultrasonic)
* [**Optical**](Blk_Range_Sensor.md#optical)

![](img/Sensor_Diagrams/Range.png)

## **Ultrasonic**
>Read the distance of an object using ultrasonic sound.
>
>* Returns reading in centimeters (cm).
>* Detectable distance ranges from **1** cm to **255** cm.
>* Returned reading is linear.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Range_Sensor/GetRangeUltrasonic.PNG" width="350">
>
>### Code Produced:
>
>>Setup:
>>>
    range = Fusion.range(f)

>>Code:
>>>
    range.ultrasonic()
    
>### Example:
>
><img src="../img/Intermediate_Blocks/Range_Sensor/GetRangeUltrasonic_Example.PNG" width="600">
>
>>Code:
>>>    
    import Fusion
    f = Fusion.driver()
    my_range_ultrasonic = None
    range = Fusion.range(f)
    my_range_ultrasonic = range.ultrasonic()
    
## **Optical**
>Read the proximity of an object using infrared light.
>
>* The returned reading ranges from **0** - **1023**.
>* Detectable proximity ranges from **1** cm to **15** cm.
>* Returned reading is an exponential decay.
    * Value increases as the object approached the sensor.
    
>### Block:
>
><img src="../img/Intermediate_Blocks/Range_Sensor/GetRangeOptical.PNG" width="280">
>
>### Code Produced:
>
>>Setup:
>>>
    range = Fusion.range(f)

>>Code:
>>>
    range.optical()
    
>### Example:
>
><img src="../img/Intermediate_Blocks/Range_Sensor/GetRangeOptical_Example.PNG" width="550">
>
>>Code:
>>>
    import Fusion
    f = Fusion.driver()
    my_range_optical = None
    range = Fusion.range(f)
    my_range_optical = range.optical()

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Range Sensor