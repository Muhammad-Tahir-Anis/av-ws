from src.map_parser_pkg.odr_map.lane import Lane
from typing import List


class Right:
	def __init__(self,lane=None,lane_list=None):
		self.lane: Lane = lane
		self.lane_list: List[Lane] = lane_list
