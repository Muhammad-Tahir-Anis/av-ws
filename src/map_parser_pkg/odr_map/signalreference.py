from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.validity import Validity


class Signalreference:
	def __init__(self,userdata=None,s=None,id=None,orientation=None,validity=None,t=None):
		self.userdata: Userdata = userdata
		self.s = s
		self.id = id
		self.orientation = orientation
		self.validity: Validity = validity
		self.t = t
