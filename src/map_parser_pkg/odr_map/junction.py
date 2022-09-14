from src.map_parser_pkg.odr_map.controller import Controller
from typing import List
from src.map_parser_pkg.odr_map.connection import Connection
from src.map_parser_pkg.odr_map.userdata import Userdata


class Junction:
	def __init__(self,controller_list=None,id=None,controller=None,connection_list=None,userdata=None,name=None):
		self.controller_list: List[Controller] = controller_list
		self.id = id
		self.controller: Controller = controller
		self.connection_list: List[Connection] = connection_list
		self.userdata: Userdata = userdata
		self.name = name
