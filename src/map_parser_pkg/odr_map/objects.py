from src.map_parser_pkg.odr_map.object import Object
from typing import List
from src.map_parser_pkg.odr_map.object import Object

class Objects:
	def __init__(self,object_list=None,object=None):
		self.object_list: List[Object] = list()
		self.object: Object = object
