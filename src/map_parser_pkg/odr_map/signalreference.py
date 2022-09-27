from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.validity import Validity


class Signalreference:
	def __init__(cls,id=None,s=None,userdata=None,orientation=None,validity=None,t=None):
		cls.id = id
		cls.s = s
		cls.userdata: Userdata = userdata
		cls.orientation = orientation
		cls.validity: Validity = validity
		cls.t = t
