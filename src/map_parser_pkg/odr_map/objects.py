from src.map_parser_pkg.odr_map.object import Object
from typing import List

class Objects:
	def __init__(self,object_list=None):
		self.object_list: List[Object] = list()
