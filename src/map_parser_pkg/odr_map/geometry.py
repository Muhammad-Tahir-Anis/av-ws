from src.map_parser_pkg.odr_map.arc import Arc


class Geometry:
	def __init__(self,line=None,y=None,s=None,length=None,hdg=None,x=None,arc=None):
		self.line = line
		self.y = y
		self.s = s
		self.length = length
		self.hdg = hdg
		self.x = x
		self.arc: Arc = arc
