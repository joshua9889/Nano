# **Core Motor Controller (45-2203)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Motor Controller Python Library Information](Py_Core_Motor_Controller.md)  

**List of available blocks:**  

* [**Setup**](Blk_Core_Motor_Controller.md#setup)
* [**Motor Speed**](Blk_Core_Motor_Controller.md#motor-speed)
* [**Motor Power**](Blk_Core_Motor_Controller.md#motor-power)
* [**Run To Position**](Blk_Core_Motor_Controller.md#run-to-position)
* [**Read Encoder**](Blk_Core_Motor_Controller.md#read-encoder)
* [**Read Battery Voltage**](Blk_Core_Motor_Controller.md#read-battery-voltage)

## **Setup**
>This block contains the necessary drivers for our Core Motor Controller and must be called at the beginning of the program. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Block:
>
><img src="../img/Core_Control/cmc_setup.PNG" width="450">
>
>### Code:
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
>>
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
    
## **Motor Speed**
>Set the speed of a motor connected to one of the motor ports. This block will maintain speed of the motors which means that 100% motor speed being applied only runs around 80% of maximum efficiency. Therefore if the motor encounters additional friction more power to the motor can be applied to maintain the speed.  
Must have the [Setup](Blk_Core_Motor_Controller.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/cmc_motorSpeed.PNG" width="300">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    cmc1.constantSpeed(cmc1.M1, 100)
    
## **Motor Power**
>Set the power of a motor connected to one of the motor ports.  
Must have the [Setup](Blk_Core_Motor_Controller.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/cmc_motorPower.PNG" width="300">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    cmc1.constantPower(cmc1.M1, 100)
    
## **Run To Position**
>Run the motor to a specific encoder count at a set power. Motors vary with encoder counts per revolution which could create different results.  
Must have the [Setup](Blk_Core_Motor_Controller.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/cmc_runToPosition.PNG" width="600">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    cmc1.runToPosition(cmc1.M1, 60, 5000)
    
## **Read Encoder**
>Run the current encoder count of a motor.   
Must have the [Setup](Blk_Core_Motor_Controller.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/cmc_readEncoder.PNG" width="400">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    print cmc1.readEncoder(cmc1.M1)
    
## **Read Battery Voltage**
>Run the current battery voltage of the 12V battery powering the Core Motor Controller. The value return is returned in 20mV increments.  
Must have the [Setup](Blk_Core_Motor_Controller.md#setup) block at the start of your program for this block to work.  
For example a returned value of 601 gives a voltage of (601 x .02) = **12.02V**   
>
>### Block:
>
><img src="../img/Core_Control/cmc_readBattVoltage.PNG" width="300">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    cmc1 = CoreControl.coreMotorController(c, 'AL00VVPP')
>>
    print cmc1.readBattVoltage()


## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Core Motor Controller