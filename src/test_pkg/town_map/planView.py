from src.test_pkg.town_map.geometry import Geometry
from typing import List
from src.test_pkg.town_map.geometry import Geometry


class Planview:
	def __init__(self, geometry_list,geometry):
		self.geometry_list: List[Geometry] = list()
		self.geometry: Geometry = geometry