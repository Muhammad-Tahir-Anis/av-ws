from src.map_parser_pkg.odr_map.lane import Lane
from typing import List


class Right:
	def __init__(self,lane_list=None,lane=None):
		self.lane_list: List[Lane] = lane_list
		self.lane: Lane = lane
