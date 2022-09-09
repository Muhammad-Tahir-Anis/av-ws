from src.test_pkg.town_map.laneSection import Lanesection
from src.test_pkg.town_map.laneOffset import Laneoffset
from typing import List
from src.test_pkg.town_map.laneOffset import Laneoffset


class Lanes:
	def __init__(self, laneSection,laneOffset_list,laneOffset):
		self.laneSection: Lanesection = laneSection
		self.laneOffset_list: List[Laneoffset] = list()
		self.laneOffset: Laneoffset = laneOffset