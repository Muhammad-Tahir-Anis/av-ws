from src.map_parser_pkg.odr_map.connection import Connection
from typing import List
from src.map_parser_pkg.odr_map.controller import Controller
from src.map_parser_pkg.odr_map.userdata import Userdata


class Junction:
	def __init__(cls,connection_list=None,controller=None,name=None,id=None,controller_list=None,userdata=None):
		cls.connection_list: List[Connection] = connection_list
		cls.controller: Controller = controller
		cls.name = name
		cls.id = id
		cls.controller_list: List[Controller] = controller_list
		cls.userdata: Userdata = userdata
