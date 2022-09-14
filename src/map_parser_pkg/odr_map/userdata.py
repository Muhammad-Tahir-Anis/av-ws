from src.map_parser_pkg.odr_map.vectorroad import Vectorroad
from src.map_parser_pkg.odr_map.vectorlane import Vectorlane
from typing import List
from src.map_parser_pkg.odr_map.vectorjunction import Vectorjunction
from src.map_parser_pkg.odr_map.vectorscene import Vectorscene
from src.map_parser_pkg.odr_map.vectorsignal import Vectorsignal


class Userdata:
	def __init__(self,vectorroad=None,vectorlane=None,vectorlane_list=None,vectorjunction=None,vectorscene=None,vectorsignal=None):
		self.vectorroad: Vectorroad = vectorroad
		self.vectorlane: Vectorlane = vectorlane
		self.vectorlane_list: List[Vectorlane] = vectorlane_list
		self.vectorjunction: Vectorjunction = vectorjunction
		self.vectorscene: Vectorscene = vectorscene
		self.vectorsignal: Vectorsignal = vectorsignal
