from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.type import Type


class Roadmark:
	def __init__(cls,width=None,material=None,soffset=None,type=None,color=None,lanechange=None):
		cls.width: Width = width
		cls.material = material
		cls.soffset = soffset
		cls.type: Type = type
		cls.color = color
		cls.lanechange = lanechange
