from position import Position


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

        self.distancetostart = 0
        self.distancetofinnish = 0

        # self.disttotarget =

    @property
    def riding(self):
        return self.current is not None

    @property
    def waiting(self):
        return self.waiter is not None

    def add_ride(self, ride):
        self.waiter = ride

    @property
    def available(self):
        return self.waiter is None and self.current is None

    @property
    def dist_to_finish(self):
        return self.pos.distance(self.current.finish)

    def update(self, t):

        # WAITING
        if self.waiting:

            print("WAITING")

            # ALREADY ARRIVED, WAITING FOR CLIENT
            if self.pos == self.waiter.start:

                print("   ALREADY ARRIVED, WAITING FOR CLIENT")

                # START DRIVING TO FINISH, WAITER BECOMES NOW CURRENT
                if t >= self.waiter.earliest:

                    self.current = self.waiter
                    self.waiter = None

                # JUST KEEP WAITING: NO POS CHANGE
                else:
                    print("   KEEP WAITING")

            # NOT YET ARRIVED AT START POSITION
            else:

                # MOVE X FIRST
                if self.pos.x != self.waiter.start.x:

                    if self.pos.x < self.waiter.start.x:
                        self.pos.moveright()
                    else:
                        self.pos.moveleft()

                # MOVE Y FIRST
                elif self.pos.y != self.waiter.start.y:

                    if self.pos.y < self.waiter.start.y:
                        self.pos.moveup()
                    else:
                        self.pos.movedown()

                else:
                    raise RuntimeError("DOO?GNPOG")

        # DRIVING
        elif self.riding:

            # ARRIVED AT DESTINATION?
            if self.pos == self.current.finish:

                self.history.append(self.current)
                self.current = None

            # NOT YET ARRIVED
            else:

                # MOVE X FIRST
                if self.pos.x != self.current.finish.x:

                    if self.pos.x < self.current.finish.x:
                        self.pos.moveright()
                    else:
                        self.pos.moveleft()

                # MOVE Y FIRST
                elif self.pos.y != self.current.finish.y:

                    if self.pos.y < self.current.finish.y:
                        self.pos.moveup()
                    else:
                        self.pos.movedown()

                else:
                    raise RuntimeError("DOO?GNPOG")

        #
        else:
            pass
