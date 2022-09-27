from src.map_parser_pkg.odr_map.control import Control
from typing import List
from src.map_parser_pkg.odr_map.type import Type


class Controller:
	def __init__(cls,control_list=None,sequence=None,name=None,id=None,control=None,type=None):
		cls.control_list: List[Control] = control_list
		cls.sequence = sequence
		cls.name = name
		cls.id = id
		cls.control: Control = control
		cls.type: Type = type
