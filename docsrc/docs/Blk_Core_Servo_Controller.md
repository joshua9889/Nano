# **Core Servo Controller (45-2204)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Servo Controller Python Library Information](Py_Core_Servo_Controller.md)  

**List of available blocks:**  

* [**Setup**](Blk_Core_Servo_Controller.md#setup)
* [**Servo Target**](Blk_Core_Servo_Controller.md#servo-target)

## **Setup**
>This block contains the necessary drivers for our Core Servo Controller and must be called at the beginning of the program. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Block:
>
><img src="../img/Core_Control/csc_setup.PNG" width="450">
>
>### Code:
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
>>
    csc1 = CoreControl.coreServoController(c, 'A0000000')
    
## **Servo Target**
>Set the target position of a servo on the selected port. Be careful as Boxlight Robotics is not responsible for damaged servos due to exceeding mechanical limits.  
Must have the [Setup](Blk_Core_Servo_Controller.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/csc_servoTarget.PNG" width="350">
>
>### Code:
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
    csc1 = CoreControl.coreServoController(c, 'A0000000')
>>
    csc1.servoTarget(csc1.S1, 128)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Core Servo Controller