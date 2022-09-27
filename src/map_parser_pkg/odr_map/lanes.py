from src.map_parser_pkg.odr_map.laneoffset import Laneoffset
from src.map_parser_pkg.odr_map.lanesection import Lanesection
from typing import List


class Lanes:
	def __init__(cls,laneoffset=None,lanesection=None,laneoffset_list=None):
		cls.laneoffset: Laneoffset = laneoffset
		cls.lanesection: Lanesection = lanesection
		cls.laneoffset_list: List[Laneoffset] = laneoffset_list
