from src.map_parser_pkg.odr_map.arc import Arc

class Geometry:
	def __init__(self,x=None,s=None,length=None,y=None,arc=None,hdg=None,line=None):
		self.x = x
		self.s = s
		self.length = length
		self.y = y
		self.arc: Arc = arc
		self.hdg = hdg
		self.line = line
