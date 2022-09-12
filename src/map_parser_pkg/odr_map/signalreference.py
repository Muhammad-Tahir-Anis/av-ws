from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.userdata import Userdata

class Signalreference:
	def __init__(self,s=None,t=None,id=None,validity=None,orientation=None,userData=None):
		self.s = s
		self.t = t
		self.id = id
		self.validity: Validity = validity
		self.orientation = orientation
		self.userdata: Userdata = userdata
