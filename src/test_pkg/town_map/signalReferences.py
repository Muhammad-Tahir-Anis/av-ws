from src.test_pkg.town_map.validity import Validity
from src.test_pkg.town_map.userData import Userdata


class Signalreferences:
	def __init__(self, id,s,t,orientation,validity,userData):
		self.id = id

		self.s = s

		self.t = t

		self.orientation = orientation

		self.validity: Validity = validity
		self.userData: Userdata = userData