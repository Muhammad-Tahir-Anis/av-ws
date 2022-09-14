from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.userdata import Userdata


class Signal:
	def __init__(self,height=None,hoffset=None,type=None,zoffset=None,pitch=None,width=None,s=None,roll=None,validity=None,userdata=None,t=None,country=None,value=None,id=None,text=None,subtype=None,orientation=None,dynamic=None,name=None):
		self.height = height
		self.hoffset = hoffset
		self.type: Type = type
		self.zoffset = zoffset
		self.pitch = pitch
		self.width: Width = width
		self.s = s
		self.roll = roll
		self.validity: Validity = validity
		self.userdata: Userdata = userdata
		self.t = t
		self.country = country
		self.value = value
		self.id = id
		self.text = text
		self.subtype = subtype
		self.orientation = orientation
		self.dynamic = dynamic
		self.name = name
