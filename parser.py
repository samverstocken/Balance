import numpy as np
from ride import ride
from car import car
import os

filedir = os.getcwd()
parentdir = os.path.split(filedir)[0]

filename = "a_example"

filename = os.path.join(parentdir, filename)


def parser(filename):
    
    f = open(filename, "r")

    FirstInfo = f.readline()
    FirstInfo = FirstInfo.split()
    
    rows = FirstInfo[0]
    columns = FirstInfo[1]
    vechicles = FirstInfo[2]
    rides = FirstInfo[3]
    bonus = FirstInfo[4]
    steps = FirstInfo[5]
    
    out = []

    for line in f: 

        lineInfo = line.split()
        a = lineInfo[0]
        b = lineInfo[1]
        c = lineInfo[2]
        d = lineInfo[3]
        start = (a,b)
        end = (c,d)
        es = lineInfo[4]
        lf = lineInfo[5]
        
        newride = ride(startp = start, endp = end, estart = es, efinish = lf)
        out.append(newride)
        
    f.close()

    return rows, columns, vechicles, rides, bonus, steps, out

parser(filename)
