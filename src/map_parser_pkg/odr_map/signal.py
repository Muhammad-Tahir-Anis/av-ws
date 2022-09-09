from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.userData import Userdata

class Signal:
	def __init__(self,name=None,id=None,s=None,t=None,zOffset=None,hOffset=None,roll=None,pitch=None,orientation=None,dynamic=None,country=None,type=None,subtype=None,value=None,text=None,height=None,width=None,validity=None,userData=None):
		self.name = name
		self.id = id
		self.s = s
		self.t = t
		self.zOffset = zOffset
		self.hOffset = hOffset
		self.roll = roll
		self.pitch = pitch
		self.orientation = orientation
		self.dynamic = dynamic
		self.country = country
		self.type: Type = type
		self.subtype = subtype
		self.value = value
		self.text = text
		self.height = height
		self.width: Width = width
		self.validity: Validity = validity
		self.userData: Userdata = userData
