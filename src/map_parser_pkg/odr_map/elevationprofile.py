from src.map_parser_pkg.odr_map.elevation import Elevation
from typing import List
from src.map_parser_pkg.odr_map.elevation import Elevation

class Elevationprofile:
	def __init__(self,elevation_list=None,elevation=None):
		self.elevation_list: List[Elevation] = list()
		self.elevation: Elevation = elevation
