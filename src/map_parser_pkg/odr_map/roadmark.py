from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width


class Roadmark:
	def __init__(self,lanechange=None,type=None,color=None,soffset=None,material=None,width=None):
		self.lanechange = lanechange
		self.type: Type = type
		self.color = color
		self.soffset = soffset
		self.material = material
		self.width: Width = width
