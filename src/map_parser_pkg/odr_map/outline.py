from src.map_parser_pkg.odr_map.cornerlocal import Cornerlocal
from typing import List

class Outline:
	def __init__(self,cornerLocal_list=None):
		self.cornerlocal_list: List[Cornerlocal] = list()
