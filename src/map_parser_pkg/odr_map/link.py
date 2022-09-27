from src.map_parser_pkg.odr_map.predecessor import Predecessor
from src.map_parser_pkg.odr_map.successor import Successor


class Link:
	def __init__(cls,predecessor=None,successor=None):
		cls.predecessor: Predecessor = predecessor
		cls.successor: Successor = successor
