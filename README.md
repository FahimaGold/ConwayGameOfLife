# PythonScripts
This project contains some python scripts.
 
The file "conwayGame.py"  demonstrates the use of lists in python,using a sort of game. The principle of the game is as follows:

-Thers's a square cells list (A list of lists in python)

-There are cells which are alive, contain '#'

-There are cells which are dead, contain ' '

-The program run on several steps, and on each step, a cell either becomes alive, continues to live, or die, based on the rules below:

    -If a living cell has 2 or 3 living neighborhors, it continues to live
    
    -If a dead cell has exactly 3 neighbors alive, it become alive on the next step.
    
    -All the rest cells die or remain dead on the next step.
  
 ----------------------------------------------
 
 The file "mclip.py" is an example of copying a senetence to clipbaord. This script, takes an extra argument from the command line to work. This arguement depicts a key in a dictionnary, which its value will be copied to clipboard. To do so, you need to install a python module that doesn't exite by defaut: 
 
    -Open your cmd and go to the directory where you installed python. In my case, C:\python34\scripts
    
    -Type the command: pip install pyperclip
    
 Now that you've installed the "pyperclip" module, you're ready to run your script from cmd as follow:
 c:\python34\python mclip.py agree     #agree is the argument
 You're then supposed to see on cmd the following output: Text for agree copied to clipboard.
    
    
