from src.map_parser_pkg.odr_map.arc import Arc


class Geometry:
	def __init__(cls,arc=None,s=None,y=None,hdg=None,length=None,x=None,line=None):
		cls.arc: Arc = arc
		cls.s = s
		cls.y = y
		cls.hdg = hdg
		cls.length = length
		cls.x = x
		cls.line = line
