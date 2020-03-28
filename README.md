# ConwayGameOfLife
This code sample demonstrates the use of lists in python,using a sort of game. The principle of the game is as follows:
-Thers's a square cells list (A list of lists in python).
-There are cells which are alive, contain '#' 
-There are cells which are dead, contain ' '
-The program run on several steps, and on each step, a cell either becomes alive, continues to live, or die, based on the rules below:
    -If a living cell has 2 or 3 living neighborhors, it continues to live
    -If a dead cell has exactly 3 neighbors alive, it become alive on the next step.
    -All the rest cells die or remain dead on the next step.
