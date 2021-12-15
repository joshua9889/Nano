# **Sound Generator (45-2016)**
-----
The Sound Generator can generate a sound based on volume, pitch and duration. This sensor also can overwrite settings during a tone to change the pitch, volume, or extend the duration of the tone.

>**Sensor Type** : Four Wire I2C  
>**Default I2C Address** : 0x34  
>**Sensor ID Code** : 0x53  
>**Dimensions** : 32mm x 32mm x 19mm  
>**Mounting Holes** : 24mm x 24mm  
>**Power** : 5V DC, 22mA Max  
>**Signal Logic Levels** : Logic 0 - 0V, Logic 1 - 5V  
>**I2C Bus Speed** : 100kHz max  
>**I2C Address Change Option** : Yes (Even Number 0x10 - 0xEE)  
>[Sound Generator Visual Programming Blocks](Blk_Sound_Generator.md)

**List of available functions:**  

* [**Fusion.sound(*driver*, *addr*)**](Py_Sound_Generator.md#fusionsounddriver-addr)
* [**setVolume(*volume*)**](Py_Sound_Generator.md#setvolumevolume)
* [**setPitch(*pitch*)**](Py_Sound_Generator.md#setpitchpitch)
* [**setDuration(*duration*)**](Py_Sound_Generator.md#setdurationduration)
* [**getDuration()**](Py_Sound_Generator.md#getduration)
* [**setSound(*volume*, *pitch*, *duration*)**](Py_Sound_Generator.md#setsoundvolume-pitch-duration)
* [**setSoundBlocking(*volume*, *pitch*, *duration*, *pause*)**](Py_Sound_Generator.md#setsoundblockingvolume-pitch-duration-pause)

![](img/Sensor_Diagrams/Sound.png)

## **Fusion.sound(*driver*, *addr*)**
>### Definition
>>This class contains the necessary drivers for our Sound Generator and must be called at the beginning of the program before using any other class functions. 
>
>### Parameters
>>***driver*** : Main driver object so the class can call driver functions (**f**)  
>>***addr*** : Enter an I2C address in hexadecimal if different from default 
>
>### Returns
>>**Sound Generator Object**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s1 = Fusion.sound(f)
    s2 = Fusion.sound(f, 0x40)

## **setVolume(*volume*)**  
>### Definition
>>Controls the amplitude of the output signal from 0 (**LOW**) to 3 (**MAX**).
>>
>>* [Constants](Py_Constants.md)
>
>### Parameters
>>***volume*** : int (0 - 3) (**LOW**, **MED**, **HIGH**, **MAX**)  
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s = Fusion.sound(f)
    s.setVolume(s.HIGH)
    
## **setPitch(*pitch*)**
>### Definition
>>The Pitch controls the frequency of the output in increments of 1Hz. The frequencies range from 1Hz to 5kHz. The speaker resonates at about 2kHz, so the speaker will sound much louder at this frequency.
>
>### Parameters
>>***pitch(Hz)*** : int (0 - 5000)  
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s = Fusion.sound(f)
    s.setPitch(2500)
    
## **setDuration(*duration*)**
>### Definition
>>The duration controls the length of the tone in increments of 10ms ranging from 10ms – 2.55s. The duration of the tone begins a countdown and will stop when the counter reaches 0. The duration may be updated at anytime to extend the length of a tone past 2.55s.
>
>### Parameters
>>***duration(ms)*** : int (0 - 2550)  
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s = Fusion.sound(f)
    s.setDuration(1500)
    
## **getDuration()**  
>### Definition
>>Get the remaining time of the tone being played. This is useful to updated the tone generated just before the current tone is complete so that there is not a gap of sound.
>
>### Parameters
>>**None**
>
>### Returns
>>***duration(ms)*** : int (0 - 2550)
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s = Fusion.sound(f)
    s.setSound(s.MAX, 2500, 2000)
>>    
    while s.getDuration(): pass
    s.setSound(s.MED, 1500, 1000)

## **setSound(*volume*, *pitch*, *duration*)**
>### Definition
>>This function allows the user to set the volume, pitch and duration all in a single call. This tone can be interrupted or change before the duration reaches 0.
>>
>>* [Constants](Py_Constants.md)
>
>### Parameters
>>***volume*** : int (0 - 3) (**LOW**, **MED**, **HIGH**, **MAX**)  
>>***pitch (Hz)*** : int (1 - 5000) **Recommended not to exceed 5,000Hz**  
>>***duration (ms)*** : int (0 - 2550)
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s = Fusion.sound(f)
    s.setSound(s.MAX, 2500, 1500)
    
## **setSoundBlocking(*volume*, *pitch*, *duration*, *pause*)**
>### Definition
>>This function allows the user to set the volume, pitch and duration all in a single call with a blocking function feature. What makes this function different from `setSound()` is that this function blocks other actions while a sound is being played, therefore no other code in the program can run. The parameter *pause* is the time after the tone until the next line of code is executed.
>>
>>* [Constants](Py_Constants.md)
>
>### Parameters
>>***volume*** : int (0 - 3) (**LOW**, **MED**, **HIGH**, **MAX**)  
>>***pitch (Hz)*** : int (1 - 5000) **Recommended not to exceed 5,000Hz**  
>>***duration (ms)*** : int (0 - 65535)  
>>***pause (ms)*** : int (0 - 65535)
>
>### Returns
>>**None**
>
>### Example
>>
    import Fusion
    f = Fusion.driver()
    s = Fusion.sound(f)
    s.setSoundBlocking(s.MAX, 2500, 4500, 1000)

## **Questions?**
>Contact Boxlight Robotics at [support@BoxlightRobotics.com](mailto:support@BoxlightRobotics.com) with a detailed description of the steps you have taken and observations you have made.
>
>**Email Subject**: Fusion Python Sound Generator