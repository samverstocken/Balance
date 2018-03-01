class ride:

	def __init__(self,start, finish, earliest, latest, ID):
		self.start = start
		self.finish = finish
		self.earliest = earliest
		self.latest = latest
        self.distance = self.dist(start,finish)
        self.rideID = ID
        self.status = False

	def dist(self, a,b):
    		return abs(a[0]-b[0]) + abs(a[1]-b[1])
