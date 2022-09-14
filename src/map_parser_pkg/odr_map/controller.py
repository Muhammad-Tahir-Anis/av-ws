from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.control import Control
from typing import List


class Controller:
	def __init__(self,type=None,id=None,control_list=None,control=None,name=None,sequence=None):
		self.type: Type = type
		self.id = id
		self.control_list: List[Control] = control_list
		self.control: Control = control
		self.name = name
		self.sequence = sequence
