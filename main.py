#!/user/bin/env python

# Imports
import numpy as np
from car import Car
from ride import Ride
from parser import parser
#from pts.core.tools import filesystem as fs

#from pts.core.tools import formatting as fmt

import argparse
from position import Position

# Loop over the files
# for filepath in fs.files_in_path()


# Sort the rides from highest number of steps
#sorted_rides = sorted(rides, key=lambda ride: ride.distance)

# print(sorted_rides)

#sorted_rides = sorted(rides, key=lambda ride: ride.start)
# print(sorted_rides)

argp = argparse.ArgumentParser()
argp.add_argument('which', type=int)
argp.add_argument('--output', type=str, default="output.txt")

# Get arguments
args = argp.parse_args()

# -----------------------------------------------------------------

def get_distance(posa, posb):
    """
    This function ...
    :param posa:
    :param posb:
    :return:
    """

    return abs(posa[0] - posb[0]) + abs(posa[1] - posb[1])

# -----------------------------------------------------------------


filenames = ["a_example.in", "b_should_be_easy.in",
             "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]

# -----------------------------------------------------------------


class Runner(object):

    def __init__(self, which=0, output="output.txt"):
        """
        This function ...
        """

        # Read file
        rows, columns, nvehicles, nrides, bonus, steps, rides = parser(
            filenames[which])

        ####
        self.rides = rides
        self.cars = []

        #
        self.initialize_cars(nvehicles)

        # sET out o^^ut file path
        self.outfilepath = output

        self.time = 0
        self.nsteps = steps

    # -----------------------------------------------------------------

    def initialize_cars(self, ncars):
        """
        This function ..
        :return:
        """

        for _ in range(ncars):

            #
            car = Car()
            self.cars.append(car)

    # -----------------------------------------------------------------

    def run(self):
        """
        This function ...
        :return:
        """

        for t in range(self.nsteps):

            self.time = t

            for car in self.cars:
                car.update(self.time)

            for ride in self.rides:
                if ride is None:
                    continue

                # POSSIBLE???
                if ride.possible:
                    print("POSSIBLE")
                    #car = self.find_nearest_car(ride.start)
                    car = self.find_nearest_available_car(ride.start)
                    print(car)
                    if car is None:

                        pass

                    else:

                        if car.pos.distance(ride.start) > ride.earliest - t:
                            print("impossible!")
                        else:
                            car.add_ride(ride)

                # self.rides.pop(ride.rideID)
                self.rides[ride.rideID] = None

        self.write()

    # -----------------------------------------------------------------

    @property
    def car_positions(self):
        """
        This function ...
        :return:
        """

        positions = []
        for car in self.cars:
            positions.append(car.pos)
        return positions

    # -----------------------------------------------------------------

    @property
    def available_cars(self):

        return [car for car in self.cars if car.available]

    # -----------------------------------------------------------------

    @property
    def available_car_positions(self):

        return [car.pos for car in self.available_cars]

    def find_nearest_car(self, position):
        """
        This function ...
        :param position:
        :return:
        """

        distances = [get_distance(car_position, position)
                     for car_position in self.car_positions]
        #nearest_indices = np.argmin(distances)
        try:
            nearest_index = np.argmin(distances)
        except ValueError:
            return None
        # print(nearest_index)
        return self.cars[nearest_index]

    def find_nearest_available_car(self, pos):
        """
        This function ..
        :param position:
        :return:
        """

        distances = [car_position.distance(pos)
                     for car_position in self.available_car_positions]
        print(distances)
        try:
            nearest_index = np.argmin(distances)
        except ValueError:
            return None
        return self.available_cars[nearest_index]

    # -----------------------------------------------------------------

    @property
    def ncars(self):

        return len(self.cars)

    # -----------------------------------------------------------------

    def write(self):
        """
        This function ...
        :return:
        """

        with open(self.outfilepath, 'w') as f:

            # for i in range(self.ncars):
            for i, car in enumerate(self.cars):
                nrides = len(car.history)
                f.write(str(nrides) + " ")

                for ride in car.history: f.write(str(ride.rideID) + " ")

                f.write('\n')

# ----------------------------------------------------------------


# Run
runner = Runner(args.which, output=args.output)
runner.run()

# -----------------------------------------------------------------
