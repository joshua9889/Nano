# **IR Locator 360° (45-2009)**
-----
The IR Locator 360° utilizes an array of 4 photodiodes to detect the direction and distance from a 1200Hz or 600Hz pulsed infrared source with a  5°resolution. Both the 600Hz and 1200Hz frequencies can be read at the same time allowing up to two directional sources to be used. This device is compatible with all legacy IR sources such as the HiTechnic IR Ball, Beacon, and Beacon V2. Overall detection range is based on the intensity of the IR source being used. 

* Connect via **I2C** port.

>[IR Locator 360° Python Library Information](Py_IR_Locator_360.md)  

**List of available blocks:**  

* [**Heading**](Blk_IR_Locator_360.md#heading)
* [**Intensity**](Blk_IR_Locator_360.md#intensity)

![](img/Sensor_Diagrams/IRLocator360.png)

## **Heading**
>Reads incoming infrared light in a 360° field around the sensor. The returned reading is in 5° increments.
>
>* Read incoming infrared light at a frequency of **600Hz** or **1200Hz**.
>* The returned heading reading ranges from **0** - **71**.
>* **CW** rotation results in an increase (**+**) in reading from **0**.
>* **CCW** rotation results in a decrease (**-**) in reading from **71**.
>    
>***Degrees*** **=** Heading Reading **x** 5°
>
>### Block:
>
><img src="../img/Intermediate_Blocks/IR_Locator_360/GetIRLocatorHeading.PNG" width="400">
>
>### Code Produced:
>
>>Setup:
>>>
    locator = Fusion.locator360(f)

>>Code:
>>>
    locator.getHeading(1200)

## **Intensity**
>Measures the amount of infrared light being detected which corresponds to the distance between the sensor and source.
>
>* Read incoming infrared light at a frequency of **600Hz** or **1200Hz**.
>* The returned intensity value increases as the source approaches the sensor.
>* Value is **0** if no infrared light is detected.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/IR_Locator_360/GetIRLocatorIntensity.PNG" width="400">

>
>### Code Produced:
>
>>Setup:
>>>
    locator = Fusion.locator360(f)

>>Code:
>>>
    locator.getIntensity(1200)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly IR Locator 360