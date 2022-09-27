from src.map_parser_pkg.odr_map.object import Object
from typing import List


class Objects:
	def __init__(cls,object_list=None,object=None):
		cls.object_list: List[Object] = object_list
		cls.object: Object = object
