from src.test_pkg.town_map.lane import Lane
from typing import List
from src.test_pkg.town_map.lane import Lane


class Left:
	def __init__(self, lane_list,lane):
		self.lane_list: List[Lane] = list()
		self.lane: Lane = lane