# **Core Legacy Module (45-2202)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Legacy Module Python Library Information](Py_Core_Legacy_Module.md)  

**List of available blocks:**  

* [**Setup**](Blk_Core_Legacy_Module.md#setup)
* [**Set LED**](Blk_Core_Legacy_Module.md#set-led)
* [**Analog Read**](Blk_Core_Legacy_Module.md#analog-read)
* [**I2C Read**](Blk_Core_Legacy_Module.md#i2c-read)
* [**I2C Write**](Blk_Core_Legacy_Module.md#i2c-write)

## **Setup**
>This block contains the necessary drivers for our Core Legacy Module and must be called at the beginning of the program. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Block:
>
><img src="../img/Core_Control/clm_setup.PNG" width="450">
>
>### Code:
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
>>
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
    
## **Set LED**
>Turn on or off any of the four green on-board LEDs.  
Must have the [Setup](Blk_Core_Legacy_Module.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/clm_setLED.PNG" width="300">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    clm1.setLED(1, clm1.ON)
    
## **Analog Read**
>Read from an analog device attached to the corresponding port.  
Must have the [Setup](Blk_Core_Legacy_Module.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/clm_analogRead.PNG" width="370">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    clm1.analogRead(clm1.S0)
    
## **I2C Read**
>Read data from an I2C device connected to a specified ***port*** based on the ***address*** of the device, the ***register*** location and the ***length*** of values to be read.   
Must have the [Setup](Blk_Core_Legacy_Module.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/clm_i2cRead.PNG" width="700">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    print clm1.i2cRead(clm1.S0, 0x02, 0x42, 1)
    
## **I2C Write**
>Write data to an I2C device connected to a specified ***port*** based on the ***address*** of the device, the ***register*** location with a ***buffer*** of values.   
Must have the [Setup](Blk_Core_Legacy_Module.md#setup) block at the start of your program for this block to work.
>
>### Block:
>
><img src="../img/Core_Control/clm_i2cWrite.PNG" width="700">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    clm1.i2cWrite(clm1.S0, 0x02, 0x42, [1])
    

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Core Legacy Module