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
