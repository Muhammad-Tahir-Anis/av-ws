from src.map_parser_pkg.odr_map.geometry import Geometry
from typing import List


class Planview:
	def __init__(cls,geometry_list=None,geometry=None):
		cls.geometry_list: List[Geometry] = geometry_list
		cls.geometry: Geometry = geometry
