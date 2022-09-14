from src.map_parser_pkg.odr_map.header import Header
from src.map_parser_pkg.odr_map.road import Road
from typing import List
from src.map_parser_pkg.odr_map.controller import Controller
from src.map_parser_pkg.odr_map.junction import Junction


class Opendrive:
	def __init__(self,header=None,road_list=None,controller_list=None,junction_list=None):
		self.header: Header = header
		self.road_list: List[Road] = road_list
		self.controller_list: List[Controller] = controller_list
		self.junction_list: List[Junction] = junction_list
