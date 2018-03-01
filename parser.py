import numpy as np
from ride import ride
from car import car
import os



filename = "a_example.in"



def parser(filename):
    filedir = os.getcwd()
    filedir = os.path.join(filedir,"input_files")
    filename = os.path.join(filedir, filename)

    f = open(filename, "r")

    FirstInfo = f.readline()
    FirstInfo = FirstInfo.split()
    
    rows = float(FirstInfo[0])
    columns = float(FirstInfo[1])
    vechicles = float(FirstInfo[2])
    rides = float(FirstInfo[3])
    bonus = float(FirstInfo[4])
    steps = float(FirstInfo[5])
    
    out = []

    for line in f: 

        lineInfo = line.split()
        a = float(lineInfo[0])
        b = float(lineInfo[1])
        c = float(lineInfo[2])
        d = float(lineInfo[3])
        start = (a,b)
        end = (c,d)
        es = float(lineInfo[4])
        lf = float(lineInfo[5])
        
        newride = ride(start, end, es, lf)
        out.append(newride)
        
    f.close()

    return rows, columns, vechicles, rides, bonus, steps, out

print(parser(filename))
