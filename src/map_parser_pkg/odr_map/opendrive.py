from src.map_parser_pkg.odr_map.header import Header
from src.map_parser_pkg.odr_map.road import Road
from typing import List
from src.map_parser_pkg.odr_map.controller import Controller
from src.map_parser_pkg.odr_map.junction import Junction


class Opendrive:
	def __init__(cls,header=None,road_list=None,controller_list=None,junction_list=None):
		cls.header: Header = header
		cls.road_list: List[Road] = road_list
		cls.controller_list: List[Controller] = controller_list
		cls.junction_list: List[Junction] = junction_list
