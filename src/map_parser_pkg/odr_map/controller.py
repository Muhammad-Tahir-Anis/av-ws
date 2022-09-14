from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.control import Control
from typing import List


class Controller:
	def __init__(self,sequence=None,id=None,type=None,control_list=None,control=None,name=None):
		self.sequence = sequence
		self.id = id
		self.type: Type = type
		self.control_list: List[Control] = control_list
		self.control: Control = control
		self.name = name
