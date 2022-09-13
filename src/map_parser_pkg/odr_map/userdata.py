from src.map_parser_pkg.odr_map.vectorjunction import Vectorjunction
from src.map_parser_pkg.odr_map.vectorscene import Vectorscene
from src.map_parser_pkg.odr_map.vectorlane import Vectorlane
from typing import List
from src.map_parser_pkg.odr_map.vectorroad import Vectorroad
from src.map_parser_pkg.odr_map.vectorsignal import Vectorsignal
from src.map_parser_pkg.odr_map.vectorlane import Vectorlane

class Userdata:
	def __init__(self,vectorjunction=None,vectorscene=None,vectorlane_list=None,vectorroad=None,vectorsignal=None,vectorlane=None):
		self.vectorjunction = vectorjunction
		self.vectorscene = vectorscene
		self.vectorlane_list = vectorlane_list
		self.vectorroad = vectorroad
		self.vectorsignal = vectorsignal
		self.vectorlane = vectorlane
