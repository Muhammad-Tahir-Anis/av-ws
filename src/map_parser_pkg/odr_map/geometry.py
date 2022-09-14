from src.map_parser_pkg.odr_map.arc import Arc


class Geometry:
	def __init__(self,y=None,line=None,s=None,length=None,hdg=None,arc=None,x=None):
		self.y = y
		self.line = line
		self.s = s
		self.length = length
		self.hdg = hdg
		self.arc: Arc = arc
		self.x = x
