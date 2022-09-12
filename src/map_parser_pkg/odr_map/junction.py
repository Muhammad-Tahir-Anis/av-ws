from src.map_parser_pkg.odr_map.controller import Controller
from src.map_parser_pkg.odr_map.controller import Controller
from typing import List
from src.map_parser_pkg.odr_map.connection import Connection
from src.map_parser_pkg.odr_map.userdata import Userdata

class Junction:
	def __init__(self,controller=None,controller_list=None,name=None,connection_list=None,id=None,userData=None):
		self.controller: Controller = controller
		self.controller_list: List[Controller] = list()
		self.name = name
		self.connection_list: List[Connection] = list()
		self.id = id
		self.userdata: Userdata = userdata
