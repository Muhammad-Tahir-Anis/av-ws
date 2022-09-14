from src.map_parser_pkg.odr_map.geometry import Geometry
from typing import List


class Planview:
	def __init__(self,geometry=None,geometry_list=None):
		self.geometry: Geometry = geometry
		self.geometry_list: List[Geometry] = geometry_list
