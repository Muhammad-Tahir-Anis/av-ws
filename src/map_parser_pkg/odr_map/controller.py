from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.control import Control
from src.map_parser_pkg.odr_map.control import Control
from typing import List

class Controller:
	def __init__(self,type=None,control=None,control_list=None,name=None,id=None,sequence=None):
		self.type: Type = type
		self.control: Control = control
		self.control_list: List[Control] = list()
		self.name = name
		self.id = id
		self.sequence = sequence
