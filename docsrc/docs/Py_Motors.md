# **Fusion Motors**
-----
Using the [Fusion Driver Class](Py_Driver.md), this section outlines the available functions for the motor ports. 

[Motor Visual Programming Blocks](Int_Motors.md)  

**List of available functions:**  

* [**motorMode(*motor*, *mode*)**](Py_Motors.md#motormodemotor-mode)
* [**motorSpeed(*motor*, *speed*)**](Py_Motors.md#motorspeedmotor-speed)

## **motorMode(*motor*, *mode*)**
>### Definition
>>Set the stop mode of the motor on the selected port. 
>>
>>* Default value is **FLOAT**.
>>* **FLOAT** : Motors spin freely when a value of **0** is applied.
>>* **BRAKE** : Motors are held in once place when a value of **0** is applied.
>
>### Parameters
>>***motor*** : M0 or M1  
>>***mode*** : FLOAT or BRAKE
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.motorMode(f.M0, f.FLOAT)
    
>>or
>>
    import Fusion
    f = Fusion.driver()
    f.motorMode(f.M0+f.M1, f.BRAKE)

## **motorSpeed(*motor*, *speed*)**
>### Definition
>>Set the speed of the motor on the selected port.
>
>### Parameters
>>***motor*** : M0 or M1  
>>***speed*** : int (±100)
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.motorSpeed(f.M0, 100)
    f.motorSpeed(f.M1, -100)
    
>>or
>>    
    import Fusion
    f = Fusion.driver()
    f.motorSpeed(f.M0+f.M1, 100)
    
## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Motors