# **Core Motor Controller (45-2203)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Motor Controller Visual Programming Blocks](Blk_Core_Motor_Controller.md)

**List of available functions:**  

* [**coreMotorController(*driver*, *serial*)**](Py_Core_Motor_Controller.md#coremotorcontrollerdriver-serial)
* [**constantSpeed(*motor*, *speed*)**](Py_Core_Motor_Controller.md#constantspeedmotor-speed)
* [**constantPower(*motor*, *power*)**](Py_Core_Motor_Controller.md#constantpowermotor-power)
* [**runToPosition(*motor*, *power*, *target*)**](Py_Core_Motor_Controller.md#runtopositionmotor-power-target)
* [**readEncoder(*motor*)**](Py_Core_Motor_Controller.md#readencodermotor)
* [**readBattVoltage()**](Py_Core_Motor_Controller.md#readbattvoltage)


## **coreMotorController(*driver*, *serial*)**
>### Definition
>>This class contains the necessary drivers for our Core Motor Controller and must be called at the beginning of the program before using any other class functions. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**c**)  
>>***serial*** : Enter the FTDI serial number of the module. 
>
>### Returns
>>Core Motor Controller Object
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
>>
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')

## **constantSpeed(*motor*, *speed*)**
>### Definition
>>Set the speed of a motor connected to one of the motor ports. This function will maintain speed of the motors which means that 100% motor speed being applied only runs around 80% of maximum efficiency. Therefore if the motor encounters additional friction more power to the motor can be applied to maintain the speed.  
Must have the [Setup](Py_Core_Motor_Controller.md#coremotorcontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***motor*** : M1 or M2  
>>***speed*** : int (±100)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    cmc1.constantSpeed(cmc1.M1, 50)
    
## **constantPower(*motor*, *power*)**
>### Definition
>>Set the power of a motor connected to one of the motor ports.  
Must have the [Setup](Py_Core_Motor_Controller.md#coremotorcontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***motor*** : M1 or M2  
>>***power*** : int (±100)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    cmc1.constantPower(cmc1.M1, 50)
    
## **runToPosition(*motor*, *power*, *target*)**
>### Definition
>>Run the motor to a specific encoder count at a set power. Motors vary with encoder counts per revolution which could create different results.  
Must have the [Setup](Py_Core_Motor_Controller.md#coremotorcontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***motor*** : M1 or M2  
>>***power*** : int (±100)  
>>***target*** : int (-‭2,147,483,648 - +‭2,147,483,647‬)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    cmc1.runToPosition(cmc1.M1, 50, 10000)
    
## **readEncoder(*motor*)**
>### Definition
>>Run the current encoder count of a motor.  
Must have the [Setup](Py_Core_Motor_Controller.md#coremotorcontrollerdriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***motor*** : M1 or M2   
>
>### Returns
>>***target*** : int (-‭2,147,483,648 - +‭2,147,483,647‬)
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    print cmc1.readEncoder(cmc1.M1) 
    
## **readBattVoltage()**
>### Definition
>>Run the current battery voltage of the 12V battery powering the Core Motor Controller. The value return is returned in 20mV increments.  
Must have the [Setup](Py_Core_Motor_Controller.md#coremotorcontrollerdriver-serial) function at the start of your program for this function to work.  
>>For example a returned value of 601 gives a voltage of (601 x .02) = **12.02V**
>
>### Parameters
>>**None**   
>
>### Returns
>>***Battery Voltage Multiplier*** : int ()
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    print cmc1.readBattVoltage() 

    

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Core Motor Controller