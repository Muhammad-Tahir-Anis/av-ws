from src.map_parser_pkg.odr_map.lane import Lane
from typing import List
from src.map_parser_pkg.odr_map.lane import Lane

class Left:
	def __init__(self,lane_list=None,lane=None):
		self.lane_list: List[Lane] = list()
		self.lane: Lane = lane
