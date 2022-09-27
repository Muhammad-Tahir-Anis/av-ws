from src.map_parser_pkg.odr_map.speed import Speed


class Type:
	def __init__(cls,type=None,speed=None,s=None):
		cls.type = type
		cls.speed: Speed = speed
		cls.s = s
