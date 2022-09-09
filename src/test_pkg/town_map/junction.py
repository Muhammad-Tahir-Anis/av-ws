from src.test_pkg.town_map.controller import Controller
from typing import List
from src.test_pkg.town_map.controller import Controller
from src.test_pkg.town_map.connection import Connection
from src.test_pkg.town_map.userData import Userdata


class Junction:
	def __init__(self, name,controller_list,controller,id,connection_list,userData):
		self.name = name

		self.controller_list: List[Controller] = list()
		self.controller: Controller = controller
		self.id = id

		self.connection_list: List[Connection] = list()
		self.userData: Userdata = userData