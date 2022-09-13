from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.type import Type

class Roadmark:
	def __init__(self,width=None,material=None,color=None,type=None,lanechange=None,soffset=None):
		self.width: Width = width
		self.material = material
		self.color = color
		self.type: Type = type
		self.lanechange = lanechange
		self.soffset = soffset
