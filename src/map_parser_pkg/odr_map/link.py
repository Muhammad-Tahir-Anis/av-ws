from src.map_parser_pkg.odr_map.successor import Successor
from src.map_parser_pkg.odr_map.predecessor import Predecessor



class Link:
	def __init__(self,successor=None,predecessor=None):
		self.successor: Successor = successor
		self.predecessor: Predecessor = predecessor
