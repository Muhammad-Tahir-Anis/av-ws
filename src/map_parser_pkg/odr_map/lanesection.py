from src.map_parser_pkg.odr_map.left import Left
from src.map_parser_pkg.odr_map.center import Center
from src.map_parser_pkg.odr_map.right import Right

class Lanesection:
	def __init__(self,left=None,s=None,center=None,right=None):
		self.left: Left = left
		self.s = s
		self.center: Center = center
		self.right: Right = right
