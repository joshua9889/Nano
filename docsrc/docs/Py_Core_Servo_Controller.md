# **Core Servo Controller (45-2204)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Servo Controller Visual Programming Blocks](Blk_Core_Servo_Controller.md)

**List of available functions:**  

* [**coreServoController(*driver*, *serial*)**](Py_Core_Servo_Controller.md#coreservocontrollerdriver-serial)
* [**pwmEnable(*enable*)**](Py_Core_Servo_Controller.md#pwmenableenable)
* [**servoTarget(*servo*, *target*)**](Py_Core_Servo_Controller.md#servotargetservo-target)
* [**extendedModeEnable(*servo*, *mode*)**](Py_Core_Servo_Controller.md#extendedmodeenableservo-mode)

## **coreServoController(*driver*, *serial*)**
>### Definition
>>This class contains the necessary drivers for our Core Servo Controller and must be called at the beginning of the program before using any other class functions. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**c**)  
>>***serial*** : Enter the FTDI serial number of the module. 
>
>### Returns
>>Core Servo Controller Object
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()

    csc1 = CoreControl.coreServoController(c, 'A0000000')
    
## **pwmEnable(*enable*)**
>### Definition
>>Turn all the servo ports on or off. This function must be called in order for the servos to operate.   
Must have the [Setup](Py_Core_Servo_Controller.md#coreservocontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***enable*** : True(1) or False(0)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    csc1 = CoreControl.coreServoController(c, 'A0000000')

    csc1.pwmEnable(True)
    
## **servoTarget(*servo*, *target*)**
>### Definition
>>Set the target position of a servo on the selected port. Be careful as Boxlight Robotics is not responsible for damaged servos due to exceeding mechanical limits.  
Must have the [Setup](Py_Core_Servo_Controller.md#coreservocontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***servo*** : S1 - S6  
>>***target*** : int (0 - 255)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    csc1 = CoreControl.coreServoController(c, 'A0000000')

    csc1.servoTarget(csc1.S1, 128)
    
## **extendedModeEnable(*servo*, *mode*)**
>### Definition
>>Extend the range on the servo port from **750us - 2250us** to **500us - 2500us**. Be careful as Boxlight Robotics is not responsible for damaged servos due to exceeding mechanical limits.  
Must have the [Setup](Py_Core_Servo_Controller.md#coreservocontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***servo*** : S1 - S6  
>>***mode*** : True(1) or False(0)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    csc1 = CoreControl.coreServoController(c, 'A0000000')  
    
    csc1.extendedModeEnable(csc1.S1, True)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Core Servo Controller