from src.test_pkg.town_map.width import Width
from typing import List
from src.test_pkg.town_map.link import Link
from src.test_pkg.town_map.width import Width
from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.roadMark import Roadmark
from src.test_pkg.town_map.userData import Userdata
from src.test_pkg.town_map.roadMark import Roadmark


class Lane:
	def __init__(self, width_list,link,width,id,type,roadMark_list,level,userData,roadMark):
		self.width_list: List[Width] = list()
		self.link: Link = link
		self.width: Width = width
		self.id = id

		self.type: Type = type
		self.roadMark_list: List[Roadmark] = list()
		self.level = level

		self.userData: Userdata = userData
		self.roadMark: Roadmark = roadMark