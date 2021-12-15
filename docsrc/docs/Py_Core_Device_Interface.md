# **Core Device Interface (45-2201)**
-----
Before running the program, be sure to identify each module's FTDI serial number by running the [Print Devices](CoreControlDriver.md) function.

>[Core Device Interface Visual Programming Blocks](Blk_Core_Device_Interface.md)

**List of available functions:**  

* [**coreDeviceInterface(*driver*, *serial*)**](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial)
* [**setLED(*led*, *value*)**](Py_Core_Device_Interface.md#setledled-value)
* [**analogRead(*analog_port*)**](Py_Core_Device_Interface.md#analogreadanalog_port)
* [**digitalState(*port*, *state*)**](Py_Core_Device_Interface.md#digitalstateport-state)
* [**digitalRead(*port*)**](Py_Core_Device_Interface.md#digitalreadport)
* [**digitalWrite(*port*, *value*)**](Py_Core_Device_Interface.md#digitalwriteport-value)
* [**analogOutputWrite(*port*, *voltage*, *frequency*, *mode*)**](Py_Core_Device_Interface.md#analogoutputwriteport-voltage-frequency-mode)
* [**setPWM(*port*, *on_time*, *period*)**](Py_Core_Device_Interface.md#setpwmport-on_time-period)
* [**getAddresses()**](Py_Core_Device_Interface.md#getaddresses)
* [**i2cRead(*address*, *register*, *length*)**](Py_Core_Device_Interface.md#i2creadaddress-register-length)
* [**i2cWrite(*address*, *register*, *buffer*)**](Py_Core_Device_Interface.md#i2cwriteaddress-register-buffer)

## **coreDeviceInterface(*driver*, *serial*)**
>### Definition
>>This class contains the necessary drivers for our Core Device Interface and must be called at the beginning of the program before using any other class functions. The FTDI serial number is used for identifying a Core Control Module and must be entered as shown in the example.
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**c**)  
>>***serial*** : Enter the FTDI serial number of the module. 
>
>### Returns
>>Core Device Interface Object
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    import CoreControl
    c = CoreControl.driver()
>>
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
    
## **setLED(*led*, *value*)**
>### Definition
>>Turn on or off the on-board LEDs.  
Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***led*** : RED or BLUE  
>>***value*** : 0 or 1
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    cdi1.setLED(cdi1.RED, 1)
    
## **analogRead(*analog_port*)**
>### Definition
>>Read from an analog device attached to the corresponding port.  
Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***analog port*** : A0 - A7
>
>### Returns
>>***analog reading*** : int(0 - 1023)
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    print cdi1.analogRead(cdi1.A0)
    
## **digitalState(*port*, *state*)**
>### Definition
>>Set the digital port to be either an INPUT or an OUTPUT.  
Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : D0 - D7  
>>***state*** : INPUT(0) or OUTPUT(1)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    cdi1.digitalState(cdi1.D0, cdi1.INPUT)
    cdi1.digitalState(cdi1.D1, cdi1.OUTPUT)
    
## **digitalRead(*port*)**
>### Definition
>>Read from a digital device attached to the corresponding port.  
Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : D0 - D7  
>
>### Returns
>>***digital reading*** : 0 or 1
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
    cdi1.digitalState(cdi1.D0, cdi1.INPUT)
>>
    print cdi1.digitalRead(cdi1.D0)
    
## **digitalWrite(*port*, *value*)**
>### Definition
>>Write to a digital device attached to the corresponding port.  
Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : D0 - D7  
>>***value*** : 0 or 1
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
    cdi1.digitalState(cdi1.D1, cdi1.OUTPUT)
>>
    cdi1.digitalWrite(cdi1.D1, 1)
    
## **analogOutputWrite(*port*, *voltage*, *frequency*, *mode*)**
>### Definition
>>Output a wave form at a set voltage and frequency from one of the analog output ports.  
Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : AO0 or AO1  
>>***voltage*** :

>>* ***DC*** : -1024 - +1023 (-4V - +4V)
>>* ***Other*** : 0 - 1023 (0V - 8V)

>>***frequency*** : 0Hz to 5000Hz (0 in DC mode)  
>>***mode*** : DC(0), Sine(1), Square(2), Triangle(3)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    # Output a DC voltage at +4V
    cdi1.analogOutputWrite(cdi1.AO0, 1023, 0, 0)
    # Output a Sine wave with pk-pk of 4V at a frequency of 2000Hz
    cdi1.analogOutputWrite(cdi1.AO1, 512, 2000, 1)
    
## **setPWM(*port*, *on_time*, *period*)**
>### Definition
>>Set a PWM output to a specific port. This port cannot operate servos. The ***on time*** parameter sets the pulse width for the channel output in units of 1µS. Setting a value greater than ***period*** will result in the output being set to 1. The ***period*** parameter sets the pulse repetition period for the channel output in units of 1µS.   
>![](img/Core_Control/pwm.png)  
>Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***port*** : P0 or P1  
>>***on time*** : 0 - 65,535 (µS) 
>>***period*** : 0 - 65,535 (µS)
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    cdi1.setPWM(cdi1.P0, 500, 1000)
    
## **getAddresses()**
>### Definition
>>Return a list of connected I2C devices.  
>Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>**None**
>
>### Returns
>>***addresses*** : A buffer of connected I2C addresses in hexadecimal
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    print cdi1.getAddresses()
    
## **i2cRead(*address*, *register*, *length*)**
>### Definition
>>Read data from an I2C device based on the ***address*** of the device, the ***register*** location and the ***length*** of values to be read.  
>Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***address*** : The current I2C address of the sensor connected  
>>***register*** :  The register location within the sensor to start reading from  
>>***length*** :  The number of registers to read starting from the ***register*** location
>
>### Returns
>>***I2C value(s)*** : A buffer of values starting with the value in the ***register*** location to the set ***length***
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    print cdi1.i2cRead(0x4C, 0x01, 2)
    
## **i2cWrite(*address*, *register*, *buffer*)**
>### Definition
>>Write data to an I2C device based on the ***address*** of the device, the ***register*** location with a ***buffer*** of values.  
>Must have the [Setup](Py_Core_Device_Interface.md#coredeviceinterfacedriver-serial) function at the start of your program for this function to work.
>
>### Parameters
>>***address*** : The current I2C address of the sensor connected  
>>***register*** :  The register location within the sensor to start writing to  
>>***buffer*** :  An array of values to be written to the I2C device
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    cdi1 = CoreControl.coreDeviceInterface(c, 'A900VGFC')
>>
    cdi1.i2cWrite(0x4C, 0x04, [7])
    cdi1.i2cWrite(0x20, 0x10, [2, 1])

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Core Device Interface