# **Core Legacy Module (45-2202)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Legacy Module Visual Programming Blocks](Blk_Core_Legacy_Module.md)

**List of available functions:**  

* [**coreLegacyModule(*driver*, *serial*)**](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial)
* [**setLED(*led*, *value*)**](Py_Core_Legacy_Module.md#setledled-value)
* [**analogRead(*port*)**](Py_Core_Legacy_Module.md#analogreadport)
* [**getAddress(*port*)**](Py_Core_Legacy_Module.md#getaddressport)
* [**i2cRead(*port*, *address*, *register*, *length*)**](Py_Core_Legacy_Module.md#i2creadport-address-register-length)
* [**i2cWrite(*port*, *address*, *register*, *buffer*)**](Py_Core_Legacy_Module.md#i2cwriteport-address-register-buffer)
* [**enable9V(*port*, *state*)**](Py_Core_Legacy_Module.md#enable9vport-state)
* [**digitalEnable(*port*, *pin*, *value*)**](Py_Core_Legacy_Module.md#digitalenableport-pin-value)

## **coreLegacyModule(*driver*, *serial*)**
>### Definition
>>This class contains the necessary drivers for our Core Legacy Module and must be called at the beginning of the program before using any other class functions. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**c**)  
>>***serial*** : Enter the FTDI serial number of the module. 
>
>### Returns
>>Core Legacy Module Object
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
>>
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
    
## **setLED(*led*, *value*)**
>### Definition
>>Turn on or off any of the four green on-board LEDs.  
Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***led*** : 0 - 3  
>>***value*** : ON(1) or OFF(0)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    clm1.setLED(0, 1)
    clm1.setLED(2, clm1.ON)
    
## **analogRead(*port*)**
>### Definition
>>Read from an analog device attached to the corresponding port.    
Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : S0 - S5  
>
>### Returns
>>***value*** : 0 - 1023
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    print clm1.setLED(clm1.S0)

## **getAddress(*port*)**
>### Definition
>>Return the I2C address of the sensors connected to the selected port.  
>Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>**None**
>
>### Returns
>>***address*** : The I2C address in hexadecimal
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    print clm1.getAddresses()
    
## **i2cRead(*port*, *address*, *register*, *length*)**
>### Definition
>>Read data from an I2C device connected to a specified ***port*** based on the ***address*** of the device, the ***register*** location and the ***length*** of values to be read.    
Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : S0 - S5  
>>***address*** : The current I2C address of the sensor connected  
>>***register*** :  The register location within the sensor to start reading from  
>>***length*** :  The number of registers to read starting from the ***register*** location
>
>### Returns
>>***value*** : Dependent on sensor type
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    print clm1.i2cRead(clm1.S0, 0x02, 0x42, 1)
    
## **i2cWrite(*port*, *address*, *register*, *buffer*)**
>### Definition
>>Write data to an I2C device connected to a specified ***port*** based on the ***address*** of the device, the ***register*** location with a ***buffer*** of values.  
Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : S0 - S5  
>>***address*** : The current I2C address of the sensor connected  
>>***register*** :  The register location within the sensor to start reading from  
>>***buffer*** :  An array of values to be written to the I2C device
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
>>
    clm1.i2cWrite(clm1.S0, 0x02, 0x42, [1, 0])
    
## **enable9V(*port*, *state*)**
>### Definition
>>Ports **S4** and **S5** have a feature that enable a 9V output. This is useful when using the Ultrasonic sensor to get the full range of readings.  
Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : S4 or S5  
>>***state*** : True(1) or False(0)  
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
    clm1.enable9V(clm1.S4, True)
    
## **digitalEnable(*port*, *pin*, *value*)**
>### Definition
>>Turn digital pin **0** or **1** to a state of ON or OFF. These is typically used to control the LEGO light sensor LED. In I2C mode, this function is ignored.  
Must have the [Setup](Py_Core_Legacy_Module.md#corelegacymoduledriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : S0 - S5  
>>***pin*** : 0 or 1  
>>***value*** : 0 or 1  
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    clm1 = CoreControl.coreLegacyModule(c, 'AL00VCO2')
    clm1.digitalEnable(clm1.S1, 0, 1)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Core Legacy Module