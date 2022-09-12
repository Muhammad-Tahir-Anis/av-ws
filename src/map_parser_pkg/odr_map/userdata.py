from src.map_parser_pkg.odr_map.vectorjunction import Vectorjunction
from src.map_parser_pkg.odr_map.vectorlane import Vectorlane
from typing import List
from src.map_parser_pkg.odr_map.vectorscene import Vectorscene
from src.map_parser_pkg.odr_map.vectorroad import Vectorroad
from src.map_parser_pkg.odr_map.vectorlane import Vectorlane
from src.map_parser_pkg.odr_map.vectorsignal import Vectorsignal

class Userdata:
	def __init__(self,vectorJunction=None,vectorLane_list=None,vectorScene=None,vectorRoad=None,vectorLane=None,vectorSignal=None):
		self.vectorjunction: Vectorjunction = vectorjunction
		self.vectorlane_list: List[Vectorlane] = list()
		self.vectorscene: Vectorscene = vectorscene
		self.vectorroad: Vectorroad = vectorroad
		self.vectorlane: Vectorlane = vectorlane
		self.vectorsignal: Vectorsignal = vectorsignal
