from src.map_parser_pkg.odr_map.type import Type

class Roadmark:
	def __init__(self,sOffset=None,type=None,material=None,color=None,laneChange=None):
		self.sOffset = sOffset
		self.type: Type = type
		self.material = material
		self.color = color
		self.laneChange = laneChange
