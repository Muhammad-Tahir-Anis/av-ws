from src.map_parser_pkg.odr_map.elevation import Elevation
from typing import List


class Elevationprofile:
	def __init__(self,elevation=None,elevation_list=None):
		self.elevation: Elevation = elevation
		self.elevation_list: List[Elevation] = elevation_list
