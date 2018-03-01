
class Car:

    def __init__(self):

        self.pos = Position(0, 0)

        self.riding = False
        self.rides = []

        self.totarget = False

    @property
    def nrides(self):

        return len(self.rides)

    def add_ride(self, ride):

        self.rides.append(ride)
        #self.riding = True

    def check_ride(self):



    @property
    def last_ride(self):
        return self.rides[-1]

    def update(self):

#
