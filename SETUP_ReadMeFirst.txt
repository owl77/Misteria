# Misteria
Multiplayer online text adventure based on SSH written in Python 3.7-8.

Requirements:

Server with a Unix-like OS (it was tested on Termux/Android)
SSH
Python 3.7-8

It can also be played on a local network (wlan).

Setup:

Clone the repository 
Check file permissions 
> python init.py (initialise or reset the game)
> sshd (or equivalent command to start ssh daemon, if necessary)
Set up a .bashrc file, something like:

------------ .bashrc ----------------
figlet Misteria
python3.8 path_to_folder/main.py
-------------------------------------

There are also security issues that need to be addressed to prevent players from gaining access to the program files (such as by using scp). 
But once main.py is running the keyboard interrupts are all disabled.
Good luck !

Gameplay:

Users login to the server using SSH. 
Then they can either create a new character or login with an existing one.

Included in the  init.py code are two test characters called 'Elf' and 'Zelda' both having password '123'.
There is also an example of an NPC.

The file classes.py is a good place to start studying the code. You can edit world.py to start designing
the world.
The concurrency of this program relies heavily on signals, shared files and the pickle library.

In the present state it can serve as the basis for a MUSH (multi-user social hallucination) such as existed in the early
days of the internet: there are different rooms to explore, objects that can be collected and the users can message
each other, etc. It is then relatively straightforward to implement a global game dynamics and develop it further into a MUD (multi-user dungeon).

