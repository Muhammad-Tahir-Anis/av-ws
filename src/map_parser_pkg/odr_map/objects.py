from src.map_parser_pkg.odr_map.object import Object
from typing import List


class Objects:
	def __init__(self,object_list=None,object=None):
		self.object_list: List[Object] = object_list
		self.object: Object = object
