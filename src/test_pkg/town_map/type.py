from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.speed import Speed


class Type:
	def __init__(self, s,type,speed):
		self.s = s

		self.type: Type = type
		self.speed: Speed = speed