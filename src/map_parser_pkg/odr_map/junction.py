from src.map_parser_pkg.odr_map.controller import Controller
from typing import List
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.controller import Controller
from src.map_parser_pkg.odr_map.connection import Connection

class Junction:
	def __init__(self,controller_list=None,userdata=None,controller=None,connection_list=None,id=None,name=None):
		self.controller_list: List[Controller] = list()
		self.userdata = userdata
		self.controller: Controller = controller
		self.connection_list: List[Connection] = list()
		self.id = id
		self.name = name
