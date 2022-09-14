from src.map_parser_pkg.odr_map.superelevation import Superelevation
from typing import List


class Lateralprofile:
	def __init__(self,superelevation=None,superelevation_list=None):
		self.superelevation: Superelevation = superelevation
		self.superelevation_list: List[Superelevation] = superelevation_list
