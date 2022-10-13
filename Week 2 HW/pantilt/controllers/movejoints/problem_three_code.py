"""movejoints controller."""


# Step 1: Import the modules.  We'll use 'Robot' to access/control the
# robot and 'numpy' if we want to do any fancy math.
from controller import Robot
import numpy as np


# Step 2: # Define the devices...
# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Extract the two motors.
panmotor  = robot.getDevice('pan')
tiltmotor = robot.getDevice('tilt')

# Also enable the camera (so you can see the video feed).
robot.getDevice("camera").enable(timestep)


# Step 3: Any initialization you want to do for your code?
Apan  = 1.0             # Amplitude for pan joint
Atilt = 0.5             # Amplitude for tilt joint
pan = tilt = 0          # Initialize pan tilt

# Step 4: Main continuous loop
while True:
    # Take one time step in the simulation.  At the end of this, time
    # will have advanced by (timestep).  Should the simulation run
    # into a problem (for example if you reset the simulation), this
    # will return (-1) and we should break out of the loop.
    if robot.step(timestep) == -1:
        break

    # Grab the current time.
    t = robot.getTime()
    
    #Apple
    if 0.0 <= t < 2.0:
        Apan = -0.62/2
        Atilt = -0.3/2
        dt = (t - 0) / (2.0 - 0.0)
        # Set the pan and tilt angles.  You will DEFINITELY want update these.
        pan  = 0 + Apan  * ( 1 - np.cos ( np.pi * dt ) )
        tilt = 0 + Atilt * ( 1 - np.cos ( np.pi * dt ) )
    
    if t == 2.0:
        pan0 = pan
        tilt0 = tilt
    #Soccor
        
    if 2.0 <= t < 5.0:
        Apan = (0.78-pan0)/2
        Atilt = (-0.17-tilt0)/2
        dt = (t - 2.0) / (5.0 - 2.0)
        # Set the pan and tilt angles.  You will DEFINITELY want update these.
        pan  = pan0 + Apan  * ( 1 - np.cos ( np.pi * dt ) )
        tilt = tilt0 + Atilt * ( 1 - np.cos ( np.pi * dt ) )
        
        
    if t == 5.0:
        pan0 = pan
        tilt0 = tilt
    #Start
    if 5.0<= t < 7.0:
        Apan = (0-pan0)/2
        Atilt = (0-tilt0)/2
        dt = (t - 5.0) / (7.0 - 5.0)
        # Set the pan and tilt angles.  You will DEFINITELY want update these.
        pan  = pan0 + Apan  * ( 1 - np.cos ( np.pi * dt ) )
        tilt = tilt0 + Atilt * ( 1 - np.cos ( np.pi * dt ) )
    
    if t == 7.0:
        pan = tilt = 0
    # Send the commands.
    panmotor.setPosition(pan)
    tiltmotor.setPosition(tilt)

    # Any bookkeeping you want to do?  Include the print statement to
    # graph the trajectories.
    print(round(t,2), round(pan,5) , round(tilt,5) )

    # You could also break the loop at the "end of time"
    if t >= 7.0:
        break


# Step 5: Clean up the code.  Nothing to do in this example.
pass
