from src.test_pkg.town_map.predecessor import Predecessor
from src.test_pkg.town_map.successor import Successor


class Link:
	def __init__(self, predecessor,successor):
		self.predecessor: Predecessor = predecessor
		self.successor: Successor = successor