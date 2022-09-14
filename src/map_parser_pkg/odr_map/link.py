from src.map_parser_pkg.odr_map.predecessor import Predecessor
from src.map_parser_pkg.odr_map.successor import Successor


class Link:
	def __init__(self,predecessor=None,successor=None):
		self.predecessor: Predecessor = predecessor
		self.successor: Successor = successor
