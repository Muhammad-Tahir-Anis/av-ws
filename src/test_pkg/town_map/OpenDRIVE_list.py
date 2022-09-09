from src.test_pkg.town_map.road import Road
from src.test_pkg.town_map.controller import Controller
from src.test_pkg.town_map.junction import Junction


class Opendrive_list:
	def __init__(self, header,road,controller,junction):
		self.header = header

		self.road: Road = road
		self.controller: Controller = controller
		self.junction: Junction = junction