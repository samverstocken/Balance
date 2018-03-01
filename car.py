
class Car:

    def __init__(self):

        """
        This function ...
        """

        self.pos = Position(0, 0)

        self.history = []
        self.current = None
        self.waiter = None

        self.totarget = False

        #self.disttotarget =

    @property
    def riding(self):
        return self.current is not None

    @property
    def waiting(self):
        return self.waiting is not None

    def add_ride(self, ride):
        self.waiter = ride

    @property
    def available(self):
        return self.waiting is None and self.current is None

    @property
    def dist_to_finish(self):
        return self.pos.distance(self.current.finish)

    def update(self):

        if self.waiting: # WAITING

            if self.pos == self.waiting.pos:


            else:

        elif self.riding: # DRIVING



        else: pass


#
