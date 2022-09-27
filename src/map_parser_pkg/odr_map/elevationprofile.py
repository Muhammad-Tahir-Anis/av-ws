from src.map_parser_pkg.odr_map.elevation import Elevation
from typing import List


class Elevationprofile:
	def __init__(cls,elevation_list=None,elevation=None):
		cls.elevation_list: List[Elevation] = elevation_list
		cls.elevation: Elevation = elevation
