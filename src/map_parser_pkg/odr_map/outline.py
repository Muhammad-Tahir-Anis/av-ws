from src.map_parser_pkg.odr_map.cornerLocal import Cornerlocal
from typing import List

class Outline:
	def __init__(self,cornerLocal_list=None):
		self.cornerLocal_list: List[Cornerlocal] = list()
