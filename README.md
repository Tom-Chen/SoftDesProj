SoftDesProj
===========

TODO:


a README file explaining what is included and where.
[DONE]all project code (final version and earlier versions if appropriate)
evidence that the project works (screenshots, youtube videos, example input/outputs)
installation guide (what python modules need to be present, python 2/3 compatibility, etc)
[DONE]user guide (how to use the project)
design guide (explanation of how the project works, key classes, etc)
self-evaluation (what could be improved (either functionally or internally), what feature most 		happy with)

2D Artillery Game

Our code is split into four files:
main.py - The core of the game engine. Iterates at the specified update rate, controlling movement, player input, and frame updating.
tank.py - Houses the tank object. Handles the movement of the tank's rectangle and changing the tank image. Sends the updated coordinates and parameters back to main to be updated.
projectile.py - Houses the projectile object. Controls the projectile's velocity as a function of time and sends updated coordinates to main to be updated.
terrain.py - Houses the terrain object. Allows the terrain's position to be adjusted on game initialization.

The img folder contains all the necessary images.

The file instructions.pdf gives a tutorial on how to play the game, along with all of the game's controls and weapon types.


