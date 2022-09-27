from src.map_parser_pkg.odr_map.superelevation import Superelevation
from typing import List


class Lateralprofile:
	def __init__(cls,superelevation=None,superelevation_list=None):
		cls.superelevation: Superelevation = superelevation
		cls.superelevation_list: List[Superelevation] = superelevation_list
