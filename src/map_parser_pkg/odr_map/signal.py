from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.userdata import Userdata


class Signal:
	def __init__(self,country=None,value=None,id=None,t=None,height=None,type=None,name=None,width=None,validity=None,text=None,subtype=None,userdata=None,zoffset=None,hoffset=None,dynamic=None,s=None,pitch=None,orientation=None,roll=None):
		self.country = country
		self.value = value
		self.id = id
		self.t = t
		self.height = height
		self.type: Type = type
		self.name = name
		self.width: Width = width
		self.validity: Validity = validity
		self.text = text
		self.subtype = subtype
		self.userdata: Userdata = userdata
		self.zoffset = zoffset
		self.hoffset = hoffset
		self.dynamic = dynamic
		self.s = s
		self.pitch = pitch
		self.orientation = orientation
		self.roll = roll
