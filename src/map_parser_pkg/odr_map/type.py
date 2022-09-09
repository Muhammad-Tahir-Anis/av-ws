from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.speed import Speed

class Type:
	def __init__(self,s=None,type=None,speed=None):
		self.s = s
		self.type: Type = type
		self.speed: Speed = speed
