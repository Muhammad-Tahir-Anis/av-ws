from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.validity import Validity

class Signalreference:
	def __init__(self,t=None,userdata=None,orientation=None,s=None,id=None,validity=None):
		self.t = t
		self.userdata = userdata
		self.orientation = orientation
		self.s = s
		self.id = id
		self.validity: Validity = validity
