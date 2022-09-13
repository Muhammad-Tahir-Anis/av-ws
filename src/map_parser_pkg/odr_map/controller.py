from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.control import Control
from src.map_parser_pkg.odr_map.control import Control
from typing import List

class Controller:
	def __init__(self,sequence=None,name=None,type=None,control=None,id=None,control_list=None):
		self.sequence = sequence
		self.name = name
		self.type: Type = type
		self.control: Control = control
		self.id = id
		self.control_list: List[Control] = list()
