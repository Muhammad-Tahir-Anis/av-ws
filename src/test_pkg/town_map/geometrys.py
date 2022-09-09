from src.test_pkg.town_map.arc import Arc


class Geometrys:
	def __init__(self, s,x,y,hdg,length,arc):
		self.s = s

		self.x = x

		self.y = y

		self.hdg = hdg

		self.length = length

		self.arc: Arc = arc