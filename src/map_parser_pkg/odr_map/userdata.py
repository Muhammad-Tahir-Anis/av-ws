from src.map_parser_pkg.odr_map.vectorlane import Vectorlane
from typing import List
from src.map_parser_pkg.odr_map.vectorscene import Vectorscene
from src.map_parser_pkg.odr_map.vectorroad import Vectorroad
from src.map_parser_pkg.odr_map.vectorjunction import Vectorjunction
from src.map_parser_pkg.odr_map.vectorsignal import Vectorsignal


class Userdata:
	def __init__(self,vectorlane=None,vectorlane_list=None,vectorscene=None,vectorroad=None,vectorjunction=None,vectorsignal=None):
		self.vectorlane: Vectorlane = vectorlane
		self.vectorlane_list: List[Vectorlane] = vectorlane_list
		self.vectorscene: Vectorscene = vectorscene
		self.vectorroad: Vectorroad = vectorroad
		self.vectorjunction: Vectorjunction = vectorjunction
		self.vectorsignal: Vectorsignal = vectorsignal
