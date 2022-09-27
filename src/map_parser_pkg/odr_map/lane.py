from src.map_parser_pkg.odr_map.roadmark import Roadmark
from typing import List
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.type import Type


class Lane:
	def __init__(cls,roadmark_list=None,width=None,id=None,roadmark=None,width_list=None,userdata=None,level=None,link=None,type=None):
		cls.roadmark_list: List[Roadmark] = roadmark_list
		cls.width: Width = width
		cls.id = id
		cls.roadmark: Roadmark = roadmark
		cls.width_list: List[Width] = width_list
		cls.userdata: Userdata = userdata
		cls.level = level
		cls.link: Link = link
		cls.type: Type = type
