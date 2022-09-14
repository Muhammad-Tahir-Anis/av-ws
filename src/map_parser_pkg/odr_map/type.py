from src.map_parser_pkg.odr_map.speed import Speed


class Type:
	def __init__(self,type=None,speed=None,s=None):
		self.type = type
		self.speed: Speed = speed
		self.s = s
