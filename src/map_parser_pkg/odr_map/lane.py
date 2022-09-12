from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.roadmark import Roadmark
from typing import List
from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.roadmark import Roadmark
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.userdata import Userdata

class Lane:
	def __init__(self,type=None,roadMark_list=None,link=None,level=None,id=None,roadMark=None,width_list=None,width=None,userData=None):
		self.type: Type = type
		self.roadmark_list: List[Roadmark] = list()
		self.link: Link = link
		self.level = level
		self.id = id
		self.roadmark: Roadmark = roadmark
		self.width_list: List[Width] = list()
		self.width: Width = width
		self.userdata: Userdata = userdata
