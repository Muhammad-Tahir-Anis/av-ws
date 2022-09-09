from src.test_pkg.town_map.right import Right
from src.test_pkg.town_map.center import Center
from src.test_pkg.town_map.left import Left


class Lanesection:
	def __init__(self, right,center,left,s):
		self.right: Right = right
		self.center: Center = center
		self.left: Left = left
		self.s = s
