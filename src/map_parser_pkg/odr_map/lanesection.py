from src.map_parser_pkg.odr_map.left import Left
from src.map_parser_pkg.odr_map.center import Center

class Lanesection:
	def __init__(self,s=None,left=None,center=None):
		self.s = s
		self.left: Left = left
		self.center: Center = center
