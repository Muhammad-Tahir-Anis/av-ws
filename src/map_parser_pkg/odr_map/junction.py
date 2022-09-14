from src.map_parser_pkg.odr_map.controller import Controller
from typing import List
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.connection import Connection


class Junction:
	def __init__(self,controller=None,controller_list=None,userdata=None,id=None,connection_list=None,name=None):
		self.controller: Controller = controller
		self.controller_list: List[Controller] = controller_list
		self.userdata: Userdata = userdata
		self.id = id
		self.connection_list: List[Connection] = connection_list
		self.name = name
