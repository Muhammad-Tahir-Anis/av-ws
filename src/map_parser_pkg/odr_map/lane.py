from src.map_parser_pkg.odr_map.roadmark import Roadmark
from typing import List
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.link import Link


class Lane:
	def __init__(self,roadmark=None,roadmark_list=None,userdata=None,id=None,width=None,type=None,width_list=None,level=None,link=None):
		self.roadmark: Roadmark = roadmark
		self.roadmark_list: List[Roadmark] = roadmark_list
		self.userdata: Userdata = userdata
		self.id = id
		self.width: Width = width
		self.type: Type = type
		self.width_list: List[Width] = width_list
		self.level = level
		self.link: Link = link
