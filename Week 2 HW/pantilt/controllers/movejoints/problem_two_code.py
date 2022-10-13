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
    
    
    if 1.0 <= t < 3.0:
        Apan = -0.62/2
        Atilt = -0.3/2
        dt = (t - 1) / (3.0 - 1.0)
        # Set the pan and tilt angles.  You will DEFINITELY want update these.
        pan  = Apan  * ( 1 - np.cos ( np.pi * dt ) )
        tilt = Atilt * ( 1 - np.cos ( np.pi * dt ) )
    
    if 3.0 <= t < 4.0:
        pan = -0.62
        tilt = -0.3
        
    
    # Send the commands.
    panmotor.setPosition(pan)
    tiltmotor.setPosition(tilt)

    # Any bookkeeping you want to do?  Include the print statement to
    # graph the trajectories.
    print(round(t,2), round(pan,5) , round(tilt,5) )

    # You could also break the loop at the "end of time"
    if t >= 4.0:
        break


# Step 5: Clean up the code.  Nothing to do in this example.
pass
