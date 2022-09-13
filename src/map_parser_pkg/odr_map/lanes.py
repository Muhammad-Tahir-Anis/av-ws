from src.map_parser_pkg.odr_map.laneoffset import Laneoffset
from src.map_parser_pkg.odr_map.lanesection import Lanesection
from src.map_parser_pkg.odr_map.laneoffset import Laneoffset
from typing import List

class Lanes:
	def __init__(self,laneoffset=None,lanesection=None,laneoffset_list=None):
		self.laneoffset = laneoffset
		self.lanesection = lanesection
		self.laneoffset_list = laneoffset_list
