# **Generic Analog and Digital Sensors**
-----
The Analog and Digital Sensors toolbox includes blocks for analog read and digital read/write control.

* Connect analog sensors via analog port **A0** - **A7**.
* Connect digital sensors via digital port **D0** - **D7**.  

>[Fusion Driver Python Library Information](Py_Driver.md#analogread-port)

**List of available blocks:**  

* [**Analog Read**](Blk_Analog_Digital.md#analog-read)
* [**Digital Read**](Blk_Analog_Digital.md#digital-read)
* [**Digital Write**](Blk_Analog_Digital.md#digital-write)

## **Analog - Read**
>Read from the sensor connected to the corresponding analog port.
>
>* The returned reading ranges from **0** and **1023**.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Analog_Digital/ReadAnalog.PNG" width="300">
>
>### Code Produced:
>
>>Setup:
>>>
    analog_A0 = Fusion.analog(f, f.A0)
    
>>Code:
>>>
    analog_A0.read()
    
>### Example:
>
><img src="../img/Intermediate_Blocks/Analog_Digital/ReadAnalog_Example.PNG" width="550">
>    
>>Code:
>>>
    import Fusion
    f = Fusion.driver()
    my_analog_value = None
    analog_A0 = Fusion.analog(f, f.A0)
    my_analog_value = analog_A0.read()
   
## **Digital - Read**
>Read from the sensor connected to the corresponding digital port.
> 
>* The returned reading is either a **0** or **1**.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Analog_Digital/ReadDigital.PNG" width="300">
>
>### Code Produced:
>
>>Setup:
>>>
    digital_D0 = Fusion.digital(f, f.D7)

>>Code:
>>>
    digital_D0.read()

## **Digital - Write**
>Write to the device connected to the corresponding digital port.
> 
>* The value written can be either a **0** or **1**.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Analog_Digital/WriteDigital.PNG" width="450">
>
>### Code Produced:
>
>>Setup:
>>>
    digital_D0 = Fusion.digital(f, f.D0)
    
>>Code:
>>>
    digital_D0.write(0)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Analog/Digital