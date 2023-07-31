'''democode.py

   Demonstration Code for the HEBI motors and gimbal

'''

# Import useful packages
import hebi
import numpy as np
import matplotlib.pyplot as plt

from time import sleep, time


#
#  HEBI Initialization
#
# Lookup hebi motors on the network
lookup = hebi.Lookup()


#
#  HEBI Discovery - Optional, Interesting if you don't know the names
#
# Change to False to skip...
if True:
    # Give the Lookup process 2 seconds to discover modules
    sleep(2)

    # Print the results. 
    print('HEBI motors found on network:')
    for entry in lookup.entrylist:
        # Extract the family/name/address
        family  = entry.family
        name    = entry.name
        address = entry.mac_address

        # Print...
        print(f'family {family}  name {name}  address {address}')


#
#  Select the HEBI Motors
#
# Create a group from your motor names. Change motor numbers to yours,
# with [pan, tilt] order!
names = ['4.5', '7.4']
group = lookup.get_group_from_names(['robotlab'], names)

if group is None:
  print("Unable to find both motors " + str(names))
  raise Exception("Unable to connect to motors")

# Allocate command and feedback spaces.  We'll use (command) to send
# commands and (feedback) to receive motor position/velocity/effort
# data.  Pre-allocating makes the code faster and more predictable.
command  = hebi.GroupCommand(group.size)
feedback = hebi.GroupFeedback(group.size)


#
#  Find the initial HEBI positions.
#
feedback = group.get_next_feedback(reuse_fbk=feedback)
pan0  = feedback.position[0]
tilt0 = feedback.position[1]


#
#  Prepare other things
#

LENGTH = 1000
TIME = np.zeros(LENGTH)
PAN = np.zeros(LENGTH)
TILT = np.zeros(LENGTH)
index = 0

# Pick the "opposite ends"
pan1  = 1.57 * (-1 + 2*(pan0  < 0))
tilt1 = 1.57 * (-1 + 2*(tilt0 < 0))

# Determine the center and amplitude for cos waves.
Apan  = (pan0  - pan1 )/2       # Amplitude for pan joint
Atilt = (tilt0 - tilt1)/2       # Amplitude for tilt joint
cpan  = (pan0  + pan1 )/2       # Center for pan joint
ctilt = (tilt0 + tilt1)/2       # Center for tilt joint


#
#  Continually loop
#
start = time()
while True:
    # Grab the current time.
    t = time() - start

    # Get the feedback data.
    feedback = group.get_next_feedback(reuse_fbk=feedback)
    pan  = feedback.position[0]
    tilt = feedback.position[1]

    # Print three columns: time, pan position, tilt position
    print('time: '+ t, 'pan: ' + pan, 'tilt: ' + tilt)


    # Create the commands.
    despan  = cpan  + Apan  * np.cos(t)
    destilt = ctilt + Atilt * np.cos(t)

    # Set and send the commands
    command.position = [despan, destilt]
    # UNCOMMENT THIS:
    group.send_command(command)
