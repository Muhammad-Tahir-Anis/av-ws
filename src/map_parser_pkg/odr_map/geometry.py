from src.map_parser_pkg.odr_map.arc import Arc

class Geometry:
	def __init__(self,length=None,s=None,x=None,arc=None,line=None,hdg=None,y=None):
		self.length = length
		self.s = s
		self.x = x
		self.arc: Arc = arc
		self.line = line
		self.hdg = hdg
		self.y = y
