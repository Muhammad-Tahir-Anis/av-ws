from src.map_parser_pkg.odr_map.type import Type

class Control:
	def __init__(self,type=None,signalId=None):
		self.type: Type = type
		self.signalid = signalid
