from src.map_parser_pkg.odr_map.type import Type


class Control:
	def __init__(cls,type=None,signalid=None):
		cls.type: Type = type
		cls.signalid = signalid
