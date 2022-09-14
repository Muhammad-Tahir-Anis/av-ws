from src.map_parser_pkg.odr_map.type import Type


class Control:
	def __init__(self,signalid=None,type=None):
		self.signalid = signalid
		self.type: Type = type
