from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.speed import Speed

class Type:
	def __init__(self,type=None,speed=None,s=None):
		self.type: Type = type
		self.speed: Speed = speed
		self.s = s
