# **Servo Control**
-----
The Servo toolbox contains blocks for controlling the four servo ports.

* Connect via servo port **S0** to **S3**.
* Servo Target ranges from **0** to **255**.
* Value of **128** is the center of rotation and the starting position of a servo.

[Servo Python Library Information](Py_Servos.md)

**List of available blocks:**  

* [**Servo Target**](Int_Servos.md#servo-target)

## **Servo Target**
>Set the servo to a set target position from **0** to **255**. Be careful as Boxlight Robotics is not responsible for damaged servos due to exceeding mechanical limits.
>
>### Block:
>
><img src="../img/Intermediate_Blocks/Servos/SetServo.PNG" width="300">
>
>### Code Produced:
>
>>Setup:
>>>
    f.servoEnable(f.S0, 1)
    
>>Code:
>>>
    f.servoTarget(f.S0, 128)

>### Example:
>
><img src="../img/Intermediate_Blocks/Servos/SetServo_Example.PNG" width="300">
>
>>Code:
>>>
    import Fusion
    import time
	
    f = Fusion.driver()
    f.servoEnable(f.S0, 1)
    f.servoEnable(f.S2, 1)
    f.servoTarget(f.S0, 10)
    f.servoTarget(f.S2, 245)
    time.sleep(1)
    
    f.servoTarget(f.S0, 245)
    f.servoTarget(f.S2, 10)
    time.sleep(1)
    
    f.servoTarget(f.S0, 128)
    f.servoTarget(f.S2, 128)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Intermediate Servo Control