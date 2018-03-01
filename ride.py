from position import Position

class Ride:

	def __init__(self, start, finish, earliest, latest, ID):

		self.start = Position(*start)
		self.finish = Position(*finish)
		self.earliest = earliest
		self.latest = latest
		self.rideID = ID
		self.status = False

	@property
	def distance(self):
		return self.finish.distance(self.start)

	@property
	def possible(self):
		#startpos = Position(0,0)
		#sreturn self.start.distance(startpos) + self.start.distance(self.finish) > self.latest

		return self.finish.distance(self.start) < self.latest - self.earliest
