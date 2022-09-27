from src.map_parser_pkg.odr_map.lane import Lane
from typing import List


class Left:
	def __init__(cls,lane=None,lane_list=None):
		cls.lane: Lane = lane
		cls.lane_list: List[Lane] = lane_list
