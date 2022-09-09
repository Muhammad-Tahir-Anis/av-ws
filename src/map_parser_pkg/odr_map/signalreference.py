from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.userData import Userdata

class Signalreference:
	def __init__(self,id=None,s=None,t=None,orientation=None,validity=None,userData=None):
		self.id = id
		self.s = s
		self.t = t
		self.orientation = orientation
		self.validity: Validity = validity
		self.userData: Userdata = userData
