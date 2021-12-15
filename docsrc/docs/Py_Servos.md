# **Fusion Servos**
-----
Using the [Fusion Driver Class](Py_Driver.md), this section outlines the Fusion servos and their functions. 

[Servo Visual Programming Blocks](Int_Servos.md)

**List of available functions:**  

* [**servoEnable(*servo*, *state*, *extended*)**](Py_Servos.md#servoenableservo-state-extended)
* [**servoTarget(*servo*, *target*)**](Py_Servos.md#servotargetservo-target)

## **servoEnable(*servo*, *state*, *extended*)**
>### Definition
>>Enable or disable the Pulse Width Modulation (PWM) of the selected port. 
>
>### Parameters
>>***servo*** : S0 - S3  
>>***state*** : int (0 or 1)  
>>***extended*** : bool (True / Flase)  
>>
>>* Extends the servo range by modifying the limits of the PWM signal.  
>>* **False** = 750µs - 2250µs (**Default**)  
>>* **True** = 500µs - 2500µs
>>* Be careful as Boxlight Robotics is not responsible for damaged servos due to exceeding mechanical limits.
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.servoEnable(f.S0, 1)
    f.servoEnable(f.S1, 1, True)
    f.servoEnable(f.S2+f.S3, 1)

## **servoTarget(*servo*, *target*)**
>### Definition
>>Sets the target position of the servo on the selected port.
>
>### Parameters
>>***servo*** : S0 - S3  
>>***target*** : int (0 - 255) (**Default** 128 when enabled) 
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.servoTarget(f.S0, 10)
    f.servoTarget(f.S1, 245)
    f.servoTarget(f.S2+f.S3, 128)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Servos