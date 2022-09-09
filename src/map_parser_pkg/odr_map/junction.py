from src.map_parser_pkg.odr_map.connection import Connection
from typing import List
from src.map_parser_pkg.odr_map.userData import Userdata

class Junction:
	def __init__(self,id=None,name=None,connection_list=None,userData=None):
		self.id = id
		self.name = name
		self.connection_list: List[Connection] = list()
		self.userData: Userdata = userData
