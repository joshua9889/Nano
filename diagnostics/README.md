# Fusion Diagnostics 

Version:    1.0.0
Date:       2/27/18
Author:     Justin Mathews

All files and folder names must stay the same within the diagnostics folder or the 
program will not operate. 

Execution:
./runRemi.sh diagnosticGui.py

Ip address:
http://localhost:8081 (or current ip of connected device passed from GUI)

Termination:
sig interrupt (Ctrl-C) (same fasion as stopping a python program in editor)


Compilation:
When distributing the final production code, run ./compile.sh and keep the following:

remi/
psutil/
diagnosticGui.py
src.so
runRemi.sh 
