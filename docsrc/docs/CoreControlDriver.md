# **Core Control Module Driver**
-----
The Core Control Driver is used to set up all the Core Control Modules and read which modules are connected to the Fusion.

**List of available Python functions:**  

* [**CoreControl.driver()**](CoreControlDriver.md#corecontroldriver)
* [**printDevices()**](CoreControlDriver.md#printdevices)

**List of available Blockly blocks:**  

* [**Print Devices**](CoreControlDriver.md#print-devices)

## **Python**
-----
## **CoreControl.driver()**
>### Definition
>>This class contains the necessary drivers for our Core Control Modules and must be called at the beginning of the program before using any other class functions. 
>
>### Parameters
>>**None**
>
>### Returns
>>Core Control Object
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()

## **printDevices()**
>### Definition
>>Print a list of attached Core Control Modules showing the ttyl port, modules type and FTDI serial number. The serial number is used to indentify a specific controller in programming.  
>>
>>Device IDs for modules:  
**Core Device Interface** - USBAMUX  
**Core Legacy Module** - USBLSMUX  
**Core Motor Controller** - USBMCON  
**Core Servo Controller** - USBSCON
>
>### Parameters
>>**None**
>
>### Returns
>>**None**
>
>### Example
>>
    import CoreControl
    c = CoreControl.driver()
    c.printDevices() 
><img src="../img/Core_Control/printDevicesOutput.PNG" width="500">

## **Blockly**
-----
## **Print Devices**
>Print a list of attached Core Control Modules showing the ttyl port, modules type and FTDI serial number. The serial number is used to indentify a specific controller in programming.
>
>Device IDs for modules:  
**Core Device Interface** - USBAMUX  
**Core Legacy Module** - USBLSMUX  
**Core Motor Controller** - USBMCON  
**Core Servo Controller** - USBSCON
>
>### Block:
>
><img src="../img/Core_Control/printDevices.PNG" width="400">
>
>### Code:
>>
    import CoreControl
    c = CoreControl.driver()
>>
    c.printDevices
><img src="../img/Core_Control/printDevicesOutput.PNG" width="500">

    



## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Core Control Modules Driver