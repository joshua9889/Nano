# **Time**
-----
The Time toolbox contains blocks for delaying or sleeping the program as well as capuring timestamps.

## **Wait in Seconds**
>Wait **X** number of seconds before continuing to the next line of code.
>
>* **X** is a positive number.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Time/Wait_Second.PNG" width="200">
>
>### Code Produced:
>
>>Import:
>>>
    import time

>>Code:
>>>
    time.sleep(1)
	
## **Get time**
>Returns a current timestamp of the system clock.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/Time/BlocklyGetTimeBlock.png">
>
>### Code Produced:
>
>>Import:
>>>
    import time

>>Code:
>>>
    time.time()
    
>### Example:
>
><img src="../img/Intermediate_Blocks/Time/BlocklyGetTimeExample.png">
>
>>Code:
>>>   
    import time
	StartTime = None
	StartTime = time.time()
	print(StartTime)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly Time