from src.test_pkg.town_map.superelevation import Superelevation
from src.test_pkg.town_map.superelevation import Superelevation
from typing import List


class Lateralprofile:
	def __init__(self, superelevation,superelevation_list):
		self.superelevation: Superelevation = superelevation
		self.superelevation_list: List[Superelevation] = list()