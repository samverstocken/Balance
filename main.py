#!/user/bin/env python

# Imports
import numpy as np
from car import Car
from ride import Ride
from parser import parser
#from pts.core.tools import filesystem as fs

# Loop over the files
#for filepath in fs.files_in_path()

filename = "a_example.in"
filepath = "input_files/" + filename

# Read file
rows, columns, vehicles, rides, bonus, steps, out = parser(filepath)

print(rides)

# Sort the rides from highest number of steps
sorted_rides = sorted(rides, key=lambda ride: ride.distance)

print(sorted_rides)
