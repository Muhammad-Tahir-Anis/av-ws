from src.map_parser_pkg.odr_map.type import Type

class Control:
	def __init__(self,signalId=None,type=None):
		self.signalId = signalId
		self.type: Type = type
