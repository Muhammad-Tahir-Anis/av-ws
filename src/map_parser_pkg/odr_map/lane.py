from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.roadmark import Roadmark
from typing import List
from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.roadmark import Roadmark
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.type import Type

class Lane:
	def __init__(self,width=None,roadmark_list=None,link=None,userdata=None,roadmark=None,width_list=None,type=None,level=None,id=None):
		self.width: Width = width
		self.roadmark_list = roadmark_list
		self.link: Link = link
		self.userdata = userdata
		self.roadmark = roadmark
		self.width_list: List[Width] = list()
		self.type: Type = type
		self.level = level
		self.id = id
