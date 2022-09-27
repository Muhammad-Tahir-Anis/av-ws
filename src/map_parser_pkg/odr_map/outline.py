from src.map_parser_pkg.odr_map.cornerlocal import Cornerlocal
from typing import List


class Outline:
	def __init__(cls,cornerlocal_list=None):
		cls.cornerlocal_list: List[Cornerlocal] = cornerlocal_list
