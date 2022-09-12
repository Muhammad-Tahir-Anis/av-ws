from src.map_parser_pkg.odr_map.laneoffset import Laneoffset
from typing import List
from src.map_parser_pkg.odr_map.lanesection import Lanesection
from src.map_parser_pkg.odr_map.laneoffset import Laneoffset

class Lanes:
	def __init__(self,laneOffset_list=None,laneSection=None,laneOffset=None):
		self.laneoffset_list: List[Laneoffset] = list()
		self.lanesection: Lanesection = lanesection
		self.laneoffset: Laneoffset = laneoffset
