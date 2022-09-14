from src.map_parser_pkg.odr_map.laneoffset import Laneoffset
from typing import List
from src.map_parser_pkg.odr_map.lanesection import Lanesection


class Lanes:
	def __init__(self,laneoffset_list=None,laneoffset=None,lanesection=None):
		self.laneoffset_list: List[Laneoffset] = laneoffset_list
		self.laneoffset: Laneoffset = laneoffset
		self.lanesection: Lanesection = lanesection
