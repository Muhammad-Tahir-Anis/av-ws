from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.width import Width


class Roadmarks:
	def __init__(self, sOffset,type,material,color,width,laneChange):
		self.sOffset = sOffset

		self.type: Type = type
		self.material = material

		self.color = color

		self.width: Width = width
		self.laneChange = laneChange
