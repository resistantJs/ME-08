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
        tilt = 0.4676990816975*np.power(t,3)-1.010398163395*np.power(t,2)
    #Soccor 
    if 2.0 <= t < 5.0:
        pan = 0.0708292214951852*np.power(t,3)-0.481907437901111*np.power(t,2)+1.07767909366222*t-1.41436220768148
        tilt = 0.164903295569259*np.power(t,3)-1.99328399127555*np.power(t,2)+7.56509274506111*t-8.77627588957407
            
    #Start
    if 5.0<= t < 7.0:
        pan = -0.11480465407256*np.power(t,3)+0.971280955838536*np.power(t,2)+0.468335823846707*t-11.4931212561268
        tilt = 0.00414634146341463*np.power(t,3)-0.0279878048780487*np.power(t,2)-0.0310975609756097*t+0.166890243902439
        
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
