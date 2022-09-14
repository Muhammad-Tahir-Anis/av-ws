from src.map_parser_pkg.odr_map.right import Right
from src.map_parser_pkg.odr_map.center import Center
from src.map_parser_pkg.odr_map.left import Left


class Lanesection:
	def __init__(self,right=None,center=None,left=None,s=None):
		self.right: Right = right
		self.center: Center = center
		self.left: Left = left
		self.s = s
