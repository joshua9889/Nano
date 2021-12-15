# **Virtual Gamepad**
-----
This library allows you to display and use a virtual gamepad right on your touch screen device to control the Fusion. The Virtual Gamepad comes with 2 joysticks and 4 buttons that are controlled using the functions below.  
Once the code is written, start the python program and click the Virtual Gamepad button on the toolbar to open the window. The Virtual Gamepad window will open on the current IP address on port 5000 (Default: **my.bot:5000** or *192.168.50.1:5000*) in a new tab.
  
>[Virtual Gamepad Visual Programming Blocks](Blk_VirtualGamepad.md)

**List of available functions:**  

* [**VirtualGamepad.service()**](Py_VirtualGamepad.md#virtualgamepadservice)
* [**VirtualGamepad.service(*cam*, *resolution*, *fps*, *mode*)**](Py_VirtualGamepad.md#virtualgamepadservicecam-resolution-fps-mode)
* [**leftJoystick(*mixer*, *x_inv*, *y_inv*)**](Py_VirtualGamepad.md#leftjoystickmixer-x_inv-y_inv)
* [**rightJoystick(*mixer*, *x_inv*, *y_inv*)**](Py_VirtualGamepad.md#rightjoystickmixer-x_inv-y_inv)
* [**readButton(*button*)**](Py_VirtualGamepad.md#readbuttonbutton)
* [**telemetry(*line*, *value*)**](Py_VirtualGamepad.md#telemetryline-value)

![](img/VirtualGamepad/VirtualGamepad.png)

## **VirtualGamepad.service()**
>### Definition
>>This class contains the necessary drivers for the Virtual Gamepad and must be called at the beginning of the program before using any other class functions. This call also starts the server for the Virtual Gamepad.
>
>### Parameters
>>**None**
>
>### Returns
>>**Virtual Gamepad Object**
>
>### Example
>>
    import VirtualGamepad
    v = VirtualGamepad.service()
    
## **VirtualGamepad.service(*cam*, *resolution*, *fps*, *mode*)**
>### Definition
>>This class contains the necessary drivers for the Virtual Gamepad and must be called at the beginning of the program before using any other class functions. This call also starts the server for the Virtual Gamepad. Using this function with all the parameters will enable you to use a USB camera. Use the standard [VirtualGamepad.service()](Py_VirtualGamepad.md#virtualgamepadservice) function if you do not have a camera attached.
>
>### Parameters
>>***cam*** : If set to **True** it will enable the use of a USB camera or PiCamera to live stream video back to the virtual gamepad background. A camera must be attached to the Fusion in order to use this block or an exception will occur when the drivers are initialized. Use [VirtualGamepad.service()](Py_VirtualGamepad.md#virtualgamepadservice) if you do not have a camera attached.  
>>***resolution*** : The resolution parameter allows the user to change the default resolution of *(320x240)* to any defined value supported by their selected camera by entering *(width, height)*.  
>>***fps*** : Frames per second is the rate at which the live stream frames are displayed to screen. Default is *10*fps however can be increased depending on the camera abilities and WiFi connection strength.  
>>***mode*** : Mode refers to the type of camera that is connected to the device. The default mode is *'YUV'* however *'MJPG'* and *'PICAM'* are also supported. Certain cameras may work better on one mode than the other and the user should refer to the manufacturer documentation or support to determine what modes are supported. 
>
>### Returns
>>**Virtual Gamepad Object**
>
>### Example
>>   
    # Use default values
    import VirtualGamepad
    v = VirtualGamepad.service(True)
>>
    # Use custom values
    import VirtualGamepad
    v = VirtualGamepad.service(True, (800,600), 30, "MJPG")
>>   
    # Change a single parameter
    import VirtualGamepad
    v = VirtualGamepad.service(True, fps=60)

## **leftJoystick(*mixer*, *x_inv*, *y_inv*)**
>### Definition
>>Read the X-axis and Y-axis of the left joystick. The values range from -100 to 100 on each axis.
>
>### Parameters
>>***mixer*** : When set to **True** the mixer will combine the X and Y values to create a tank drive style of control. Default is set to **False**.  
>>***x_inv*** : Invert the X-Axis value. Default is set to **False**.  
>>***y_inv*** : Invert the Y-Axis value. Default is set to **False**.  
>
>### Returns
>>***axis value*** : tuple (X-axis, Y-axis) where X-axis/Y-axis = -100 to 100
>
>### Example
>>
    import VirtualGamepad
    v = VirtualGamepad.service()
    # Use Default Joystick
    left = v.leftJoystick()
    print left       # (100,0)
    print left[0]    # 100
    print left[1]    # 0
    # Use Mixer
    left = v.leftJoystick(True)
    # Change a single parameter
    left = v.leftJoystick(y_inv=True)
    # Change the Joystick
    left = v.leftJoystick(True, False, True)
    
## **rightJoystick(*mixer*, *x_inv*, *y_inv*)**
>### Definition
>>Read the X-axis and Y-axis of the right joystick. The values range from -100 to 100 on each axis.
>
>### Parameters
>>***mixer*** : When set to **True** the mixer will combine the X and Y values to create a tank drive style of control. Default is set to **False**.  
>>***x_inv*** : Invert the X-Axis value. Default is set to **False**.  
>>***y_inv*** : Invert the Y-Axis value. Default is set to **False**.  
>
>### Returns
>>***axis value*** : tuple (X-axis, Y-axis) where X-axis/Y-axis = -100 to 100
>
>### Example
>>
    import VirtualGamepad
    v = VirtualGamepad.service()
    # Use Default Joystick
    right = v.rightJoystick()
    print right       # (100,0)
    print right[0]    # 100
    print right[1]    # 0
    # Use Mixer
    right = v.rightJoystick(True)
    # Change a single parameter
    right = v.rightJoystick(y_inv=True)
    # Change the Joystick
    right = v.rightJoystick(True, False, True)

## **readButton(*button*)**  
>### Definition
>>Read a button from the Virtual Gamepad. There are 4 available buttons: 
>>
>>* **A** = 0  
>>* **B** = 1  
>>* **X** = 2  
>>* **Y** = 3  
>
>### Parameters
>>***button*** : The select button that you want to read from.
>
>### Returns
>>***value*** : int (0 or 1)
>
>### Example
>>
    import VirtualGamepad
    v = VirtualGamepad.service()
    A = v.readButton('A')
    A = v.readButton(0)
    X = v.readButton('X')
    X = v.readButton(2)

## **telemetry(*line*, *value*)**  
>### Definition
>>Print valuable data to the Virtual Gamepad screen. This is very useful when wanting to read the return values from sensors or the Virtual Gamepad functions.
>
>### Parameters
>>***line*** : The line number the data should be printed on starting with 0.  
>>***value*** : The data that is printed to the line.
>
>### Returns
>>**None**
>
>### Example
>>
    import VirtualGamepad
    v = VirtualGamepad.service()
    while True:
        (left_x, left_y) = v.leftJoystick(True, y_inv=True)
        (right_x, right_y) = v.leftJoystick(True, y_inv=True)
        v.telemetry(0, "left_x value = " + str(left_x))
        v.telemetry(1, "left_y value = " + str(left_y))
        v.telemetry(2, "right_x value = " + str(right_x))
        v.telemetry(3, "right_y value = " + str(right_y))
        v.telemetry(4, "A value = " + str(v.readButton('A')))
        v.telemetry(5, "B value = " + str(v.readButton('B')))
        v.telemetry(6, "X value = " + str(v.readButton('X')))
        v.telemetry(7, "Y value = " + str(v.readButton('Y')))

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Virtual Gamepad