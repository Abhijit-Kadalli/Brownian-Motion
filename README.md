# Brownian-Motion
This is a simple simulation of Brownian motion using the Pygame library in Python. The Brownian Motion is a random motion of particles suspended in a fluid, caused by collisions with other atoms or molecules in the fluid. This simulation shows the movement of a small particle moving in a screen and bouncing off the edges in a random direction, representing a small particle suspended in a fluid.

## Dependencies
1. Python 3.x
2. Pygame
3. Usage

To run the simulation, simply execute the brownian_motion.py file using the following command in your terminal:
```
python3 main.py
```
The particle will start moving on the screen and bouncing off the edges in a random direction.

### Note: 
The main file provided is an example of how the module should be used.

## Customization
You can customize various properties of the particle by modifying the arguments passed to the BrownianMotion class in the __init__ method:

color: color of the particle.
x: starting x-coordinate of the particle.
y: starting y-coordinate of the particle.
size: size of the particle.
speed: speed of the particle.
direction: starting direction of the particle.
screen: Pygame screen object to display the particle.
You can modify these properties to create your own Brownian Motion simulation with your desired settings.
