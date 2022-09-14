from src.map_parser_pkg.odr_map.left import Left
from src.map_parser_pkg.odr_map.right import Right
from src.map_parser_pkg.odr_map.center import Center


class Lanesection:
	def __init__(self,s=None,left=None,right=None,center=None):
		self.s = s
		self.left: Left = left
		self.right: Right = right
		self.center: Center = center
