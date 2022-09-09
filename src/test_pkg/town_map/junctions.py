from src.test_pkg.town_map.controller import Controller
from src.test_pkg.town_map.connection import Connection
from src.test_pkg.town_map.userData import Userdata


class Junctions:
	def __init__(self, name,id,controller,connection,userData):
		self.name = name

		self.id = id

		self.controller: Controller = controller
		self.connection: Connection = connection
		self.userData: Userdata = userData