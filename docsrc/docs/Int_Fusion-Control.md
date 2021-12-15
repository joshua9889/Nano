# **Intermediate Fusion Control**
-----
The Intermediate Fusion Control toolbox comes with the necessary Start, LED and End blocks.

[Fusion Driver Python Library Information](Py_Driver.md)

**List of available blocks:**  

* [**Start Block**](Int_Fusion-Control.md#start-block)
* [**Fusion LEDs**](Int_Fusion-Control.md#led)
* [**Comment**](Int_Fusion-Control.md#comment)
* [**End Program**](Int_Fusion-Control.md#end-program)

## **Start Block**
>Initializes the Fusion Robot at the start of every program. This block must be used in every Blockly program. By default the Start block is included in the programming environment. 
>
>### Block:
>
><img src="../img/Intermediate_Blocks/Control/Start.PNG" width="150">
>
>### Code Produced:
>
>>
    import Fusion
    f = Fusion.driver()

## **LED**
>Control the on-board Yellow and Blue LEDs. The LEDs can be either **ON** or **OFF**.  
>
>### Block:
>
><img src="../img/Intermediate_Blocks/Control/LED_color.PNG" width="160">
>
>### Code Produced:
>>
    f.setLED(f.YELLOW, 1)
 
## **Comment**
>Inserts inline comments into the program. This helps to label sections making it easier to find blocks of code.
>
>* In Python a comment is made starting with `#`.
>* Accepts ASCII characters.
>
>### Block:
>
><img src="../img/Intermediate_Blocks/Control/Comment.PNG" width="160">
>
>### Code Produced:
>>    
    #
    
>### Example:
>
><img src="../img/Intermediate_Blocks/Control/Comment_Example.PNG" width="350">
>>
    # This is the first comment.
    # This is my second comment.
    # This is my last comment.
   
## **End Program**
>Stop the current program running.
>
>### Block:
>
><img src="../img/Intermediate_Blocks/Control/End.PNG" width="150">
>
>### Code Produced:
>>
    exit()

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Intermediate Fusion Control