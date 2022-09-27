from src.map_parser_pkg.odr_map.vectorscene import Vectorscene
from src.map_parser_pkg.odr_map.vectorsignal import Vectorsignal
from src.map_parser_pkg.odr_map.vectorjunction import Vectorjunction
from src.map_parser_pkg.odr_map.vectorlane import Vectorlane
from typing import List
from src.map_parser_pkg.odr_map.vectorroad import Vectorroad


class Userdata:
	def __init__(cls,vectorscene=None,vectorsignal=None,vectorjunction=None,vectorlane_list=None,vectorlane=None,vectorroad=None):
		cls.vectorscene: Vectorscene = vectorscene
		cls.vectorsignal: Vectorsignal = vectorsignal
		cls.vectorjunction: Vectorjunction = vectorjunction
		cls.vectorlane_list: List[Vectorlane] = vectorlane_list
		cls.vectorlane: Vectorlane = vectorlane
		cls.vectorroad: Vectorroad = vectorroad
