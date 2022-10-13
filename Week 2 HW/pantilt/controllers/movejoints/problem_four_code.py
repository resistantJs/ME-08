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
        pan = 0.154999999999999*np.power(t,3) - 0.464999999999999*np.power(t,2)
        tilt = 0.0749999999999999*np.power(t,3) - 0.224999999999999*np.power(t,2)
    #Soccor 
    if 2.0 <= t < 5.0:
        pan = -0.103703703703703*np.power(t,3) + 1.08888888888888*np.power(t,2) - 3.11111111111111*t + 2.07629629629629
        tilt = -0.00962962962962962*np.power(t,3) + 0.101111111111111*np.power(t,2) - 0.288888888888888*t - 0.0496296296296296
        
    #Start
    if 5.0<= t < 7.0:
        pan = -0.0190243902439024*np.power(t,3) + 0.128414634146341*np.power(t,2) + 0.142682926829268*t - 0.765731707317073
        tilt = 0.00414634146341463*np.power(t,3) - 0.0279878048780487*np.power(t,2) - 0.0310975609756097*t + 0.166890243902439
    
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
