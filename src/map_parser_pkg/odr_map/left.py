from src.map_parser_pkg.odr_map.lane import Lane
from typing import List

class Left:
	def __init__(self,lane_list=None):
		self.lane_list: List[Lane] = list()
