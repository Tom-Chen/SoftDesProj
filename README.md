2D Artillery Game

Our code is split into five files:
main.py - The core of the game engine. Iterates at the specified update rate, controlling movement, player input, and frame updating.
tank.py - Houses the tank object. Handles the movement of the tank's rectangle and changing the tank image. Sends the updated coordinates and parameters back to main to be updated.
projectile.py - Houses the projectile object. Controls the projectile's velocity as a function of time and sends updated coordinates to main to be updated.
terrain.py - Houses the terrain object. Allows the terrain's position to be adjusted on game initialization.
text.py - Used for text that needs to be updated. Defines text as sprites that can easily be redrawn. Used in main for changing values in the player information displays.

The img folder contains all the necessary images for the game.

The file instructions.pdf gives a tutorial on the game's controls and weapon types. The instructions also contain a screenshot of the game.