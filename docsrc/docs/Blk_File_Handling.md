# **File Handling**
-----
This library allows you to handle file manipulation(reading/writing) using Blockly.

**List of available blocks:**  

* [**Open File**](Blk_File_Handling.md#open-file)
* [**Write to File**](Blk_File_Handling.md#write-to-file)
* [**Close File**](Blk_File_Handling.md#close-file)

## **Open File**
>Searches for the desired filename and returns a file object or list of text.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileOpenBlock.png">
>
>#### Options
> - Append - Appends text to an existing file or creates file if does not exist.
> - Overwrite - Overwrites an existing file or creates a file if does not exist.
> - Read - Returns a list of strings of all the lines in the file, throws error if file does not exist.
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileOpenOptions.png">
>
>
>### Code Produced:
>
>>
	open("filename.txt", "a")
    
>### Example:
>
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileOpenBlockAssignment.png">
>
>>Code:
>>>   
    BlocklyFile = None
	BlocklyFile = open("filename.txt", "a")

## **Write to File**
>Writes a string of text to the file.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileWriteBlock.png">
>
>### Code Produced:
>
>>
	.write('' + '\n')
    
>### Example:
>
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileWriteExample.png">
>
>>Code:
>>>   
	BlocklyFile.write('Some Text' + '\n')

## **Close File**
>Closes the file and prevents future reading and writing. In Python It is good practice to close files after using them.
>    
>### Block:
>
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileCloseBlock.png">
>
>### Code Produced:
>
>>
	.close()
    
>### Example:
>
><img src="../img/Intermediate_Blocks/FileHandling/BlocklyFileCloseExample.png">
>
>>Code:
>>>   
	BlocklyFile.close()

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Blockly File Handling