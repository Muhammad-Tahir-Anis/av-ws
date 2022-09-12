from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.validity import Validity

class Signal:
	def __init__(self,height=None,t=None,pitch=None,dynamic=None,width=None,orientation=None,userData=None,type=None,name=None,zOffset=None,hOffset=None,validity=None,country=None,roll=None,s=None,id=None,subtype=None,value=None,text=None):
		self.height = height
		self.t = t
		self.pitch = pitch
		self.dynamic = dynamic
		self.width: Width = width
		self.orientation = orientation
		self.userdata: Userdata = userdata
		self.type: Type = type
		self.name = name
		self.zoffset = zoffset
		self.hoffset = hoffset
		self.validity: Validity = validity
		self.country = country
		self.roll = roll
		self.s = s
		self.id = id
		self.subtype = subtype
		self.value = value
		self.text = text
