# **Fusion Driver**
-----
The Fusion Driver Class contains code for base controller functionality, LED control, motor controller, servo control and generic analog/digital control functions. 

**List of available functions:**  

* [**Fusion.driver()**](Py_Driver.md#fusiondriver)  
* [**readBattRaw()**](Py_Driver.md#readbattraw)
* [**readBatt()**](Py_Driver.md#readbatt)
* [**setLED(*led*, *value*)**](Py_Driver.md#setledled-value)
* [**analogRead(*port*)**](Py_Driver.md#analogread-port)
* [**digitalRead(*port*)**](Py_Driver.md#digitalreadport)
* [**digitalState(*port*, *state*)**](Py_Driver.md#digitalstateport-state)
* [**digitalWrite(*port*, *state*)**](Py_Driver.md#digitalwriteport-state)
* [**i2cRead(*addr*, *reg*, *len*)**](Py_Driver.md#i2creadaddr-reg-len)
* [**i2cWrite(*addr*, *reg*, *buf[]*)**](Py_Driver.md#i2cwriteaddr-reg-buf)

## **Fusion.driver()**
>### Definition
>>The following class is used to provide base functionality of the Fusion control board and provide drivers to interface with the various array of sensors, servos and motors.
>
>### Parameters
>>**None**
>
>### Returns
>>**Fusion Driver Object**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()

## **readBattRaw()**
>### Definition
>>Read the raw value of the battery voltage from the on-board ADC converter.
>
>### Parameters
>>**None**
>
>### Returns
>>**Raw Voltage** : int (0 - 1023)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    print f.readBattRaw()

## **readBatt()**
>### Definition
>>Read the scaled value of the battery voltage from the on-board ADC converter.
>
>### Parameters
>>**None**
>
>### Returns
>>**Voltage** : float (volts)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    print f.readBatt()

## **setLED(*led*, *value*)**
>### Definition
>>Set the selected on-board LED or **ON** (1) or **OFF** (0).
>>
>>* [Set LED Visual Programming Block](Int_Fusion-Control.md#led)
>
>### Parameters
>>***led*** : BLUE or YELLOW  
>>***value*** : int (1 or 0)
>
>>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.setLED(f.YELLOW, 1)

## **analogRead( *port* )**
>### Definition
>>Used to read analog devices connected to ports **A0** - **A7**.
>
>### Parameters
>>***port*** : A0 - A7
>
>### Returns
>>**Value** : int (0 - 1023)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    print f.analogRead(f.A0)

## **digitalRead(*port*)**
>### Definition
>>Used to read digital devices connected to ports **D0** - **D7**.
>
>### Parameters
>>***port*** : D0 - D7
>
>### Returns
>>***Value*** : int (0 - 1)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    print f.digitalRead(f.D0)

## **digitalState(*port*, *state*)**
>### Definition
>>Sets the state of the selected digital port **D0** - **D7** as input or output.
>
>### Parameters
>>***port*** : D0 - D7  
>>***state*** : INPUT or OUTPUT
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.digitalState(f.D0, f.OUTPUT)

## **digitalWrite(*port*, *state*)**
>### Definition
>>Sets the value of the selected digital port **D0** - **D7** when in output mode.
>
>### Parameters
>>***port*** : D0 - D7  
>>***state*** : int (1 or 0)
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    f.digitalState(f.D0, f.OUTPUT)
    f.digitalWrite(f.D0, 1)

## **i2cRead(*addr*, *reg*, *len*)**
>### Definition
>>Read up to 32 bytes from a device on the I2C buffer.
>
>### Parameters
>>***addr*** : Device I2C Address  
>>***reg*** : First register to read from  
>>***len*** : Number of registers to read
>
>### Returns
>>**buf[reg1, reg2, ...]**  
>>**i2c_error** : A global value can be read or cleared at any time, displays errors detected during the last I2C transaction. 
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    print f.i2cRead(0x20, 0x00, 3)

## **i2cWrite(*addr*, *reg*, *buf[ ]* )**
>### Definition
>>Write a buffer of up to 32 bytes to a device on the I2C buffer. The length is determined based on the length of the buffer being written.
>
>### Parameters
>>***addr*** : Device I2C Address  
>>***reg*** : First register to read from  
>>***buf[]*** : Buffer of up to 32 bytes
>
>### Returns
>>**i2c_error** : A global value can be read or cleared at any time, displays errors detected during the last I2C transaction. 
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    buf = [1, 2]
    f.i2cWrite(0x20, 0x00, buf)
    f.i2cWrite(0x20, 0x02, [3, 4])
    
## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Driver