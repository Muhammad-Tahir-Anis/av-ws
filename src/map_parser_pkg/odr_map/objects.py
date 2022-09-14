from src.map_parser_pkg.odr_map.object import Object
from typing import List


class Objects:
	def __init__(self,object=None,object_list=None):
		self.object: Object = object
		self.object_list: List[Object] = object_list
