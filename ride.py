class ride:

	def __init__(self,start, finish, earliest, latest):
		self.start = start
		self.finish = finish
		self.earliest = earliest
		self.latest = latest
		self.distance = self.dist(start,finish)


	def dist(self, a,b):
    		return abs(a[0]-b[0]) + abs(a[1]-b[1])
