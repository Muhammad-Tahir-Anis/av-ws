from src.map_parser_pkg.odr_map.left import Left
from src.map_parser_pkg.odr_map.right import Right
from src.map_parser_pkg.odr_map.center import Center

class Lanesection:
	def __init__(self,left=None,right=None,s=None,center=None):
		self.left: Left = left
		self.right: Right = right
		self.s = s
		self.center: Center = center
