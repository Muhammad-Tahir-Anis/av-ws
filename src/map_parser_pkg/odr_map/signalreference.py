from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.userdata import Userdata


class Signalreference:
	def __init__(self,id=None,s=None,validity=None,userdata=None,orientation=None,t=None):
		self.id = id
		self.s = s
		self.validity: Validity = validity
		self.userdata: Userdata = userdata
		self.orientation = orientation
		self.t = t
