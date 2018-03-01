class ride:

	def __init__(self,start, finish, earliest latest):
		self.start = start
		self.finish = finish
		self.earliest = earliest
		self.latest = latest
		self.steps = steps
		self.distance = abs(dist(start,finish))


	
	def dist(a,b):
    		return numpy.linalg.norm(a-b)
