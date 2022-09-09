from src.test_pkg.town_map.arc import Arc


class Geometry:
	def __init__(self, arc,y,x,s,hdg,length,line):
		self.arc: Arc = arc
		self.y = y

		self.x = x

		self.s = s

		self.hdg = hdg

		self.length = length

		self.line = line
