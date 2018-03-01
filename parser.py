import numpy as np
from ride import Ride
from car import Car
import os


filename = "a_example.in"


def parser(filename):
    filedir = os.getcwd()
    filedir = os.path.join(filedir, "input_files")
    filename = os.path.join(filedir, filename)

    f = open(filename, "r")

    FirstInfo = f.readline()
    FirstInfo = FirstInfo.split()

    rows = int(FirstInfo[0])
    columns = int(FirstInfo[1])
    vechicles = int(FirstInfo[2])
    rides = int(FirstInfo[3])
    bonus = int(FirstInfo[4])
    steps = int(FirstInfo[5])

    out = []

    ID = 0
    for line in f:

        lineInfo = line.split()
        a = int(lineInfo[0])
        b = int(lineInfo[1])
        c = int(lineInfo[2])
        d = int(lineInfo[3])
        start = (a, b)
        end = (c, d)
        es = int(lineInfo[4])
        lf = int(lineInfo[5])

        newride = Ride(start, end, es, lf, ID)
        out.append(newride)
        ID += 1

    f.close()

    return rows, columns, vechicles, rides, bonus, steps, out

# print(parser(filename))
