from src.test_pkg.town_map.control import Control
from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.control import Control
from typing import List


class Controller:
	def __init__(self, control,name,sequence,id,type,control_list):
		self.control: Control = control
		self.name = name

		self.sequence = sequence

		self.id = id

		self.type: Type = type
		self.control_list: List[Control] = list()