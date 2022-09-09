from src.map_parser_pkg.odr_map.laneOffset import Laneoffset
from src.map_parser_pkg.odr_map.laneSection import Lanesection

class Lanes:
	def __init__(self,laneOffset=None,laneSection=None):
		self.laneOffset: Laneoffset = laneOffset
		self.laneSection: Lanesection = laneSection
