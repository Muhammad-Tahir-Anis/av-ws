from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.roadMark import Roadmark
from src.map_parser_pkg.odr_map.userData import Userdata

class Lane:
	def __init__(self,id=None,type=None,level=None,roadMark=None,userData=None):
		self.id = id
		self.type: Type = type
		self.level = level
		self.roadMark: Roadmark = roadMark
		self.userData: Userdata = userData
