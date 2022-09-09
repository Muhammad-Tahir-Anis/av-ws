from src.map_parser_pkg.odr_map.type import Type

class Controller:
	def __init__(self,id=None,type=None,sequence=None):
		self.id = id
		self.type: Type = type
		self.sequence = sequence
