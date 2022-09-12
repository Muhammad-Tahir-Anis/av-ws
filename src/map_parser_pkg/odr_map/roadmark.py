from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width

class Roadmark:
	def __init__(self,type=None,width=None,laneChange=None,material=None,sOffset=None,color=None):
		self.type: Type = type
		self.width: Width = width
		self.lanechange = lanechange
		self.material = material
		self.soffset = soffset
		self.color = color
