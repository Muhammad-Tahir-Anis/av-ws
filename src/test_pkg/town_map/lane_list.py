from src.test_pkg.town_map.roadMark import Roadmark


class Lane_list:
	def __init__(self, id,type,level,roadMark,userData):
		self.id = id

		self.type = type

		self.level = level

		self.roadMark: Roadmark = roadMark
		self.userData = userData
