from src.map_parser_pkg.odr_map.center import Center
from src.map_parser_pkg.odr_map.left import Left
from src.map_parser_pkg.odr_map.right import Right


class Lanesection:
	def __init__(cls,center=None,left=None,right=None,s=None):
		cls.center: Center = center
		cls.left: Left = left
		cls.right: Right = right
		cls.s = s
