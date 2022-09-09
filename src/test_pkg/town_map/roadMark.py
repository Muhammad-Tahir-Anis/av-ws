from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.width import Width


class Roadmark:
	def __init__(self, laneChange,color,material,type,width,sOffset):
		self.laneChange = laneChange

		self.color = color

		self.material = material

		self.type: Type = type
		self.width: Width = width
		self.sOffset = sOffset
