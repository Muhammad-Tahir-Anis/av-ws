from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.validity import Validity

class Signal:
	def __init__(self,height=None,zoffset=None,dynamic=None,pitch=None,width=None,text=None,userdata=None,name=None,id=None,s=None,type=None,subtype=None,validity=None,t=None,country=None,orientation=None,value=None,hoffset=None,roll=None):
		self.height = height
		self.zoffset = zoffset
		self.dynamic = dynamic
		self.pitch = pitch
		self.width: Width = width
		self.text = text
		self.userdata = userdata
		self.name = name
		self.id = id
		self.s = s
		self.type: Type = type
		self.subtype = subtype
		self.validity: Validity = validity
		self.t = t
		self.country = country
		self.orientation = orientation
		self.value = value
		self.hoffset = hoffset
		self.roll = roll
