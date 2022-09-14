from src.map_parser_pkg.odr_map.geometry import Geometry
from typing import List


class Planview:
	def __init__(self,geometry_list=None,geometry=None):
		self.geometry_list: List[Geometry] = geometry_list
		self.geometry: Geometry = geometry
