from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width
from typing import List
from src.map_parser_pkg.odr_map.roadmark import Roadmark
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.link import Link


class Lane:
	def __init__(self,type=None,width_list=None,width=None,roadmark_list=None,id=None,roadmark=None,userdata=None,level=None,link=None):
		self.type: Type = type
		self.width_list: List[Width] = width_list
		self.width: Width = width
		self.roadmark_list: List[Roadmark] = roadmark_list
		self.id = id
		self.roadmark: Roadmark = roadmark
		self.userdata: Userdata = userdata
		self.level = level
		self.link: Link = link
