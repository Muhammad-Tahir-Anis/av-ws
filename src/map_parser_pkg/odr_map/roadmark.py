from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width


class Roadmark:
	def __init__(self,material=None,type=None,color=None,width=None,lanechange=None,soffset=None):
		self.material = material
		self.type: Type = type
		self.color = color
		self.width: Width = width
		self.lanechange = lanechange
		self.soffset = soffset
