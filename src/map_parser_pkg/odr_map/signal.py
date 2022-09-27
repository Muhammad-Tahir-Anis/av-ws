from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.validity import Validity
from src.map_parser_pkg.odr_map.width import Width


class Signal:
	def __init__(cls,hoffset=None,value=None,zoffset=None,type=None,id=None,height=None,userdata=None,pitch=None,orientation=None,dynamic=None,name=None,country=None,validity=None,t=None,width=None,subtype=None,s=None,roll=None,text=None):
		cls.hoffset = hoffset
		cls.value = value
		cls.zoffset = zoffset
		cls.type: Type = type
		cls.id = id
		cls.height = height
		cls.userdata: Userdata = userdata
		cls.pitch = pitch
		cls.orientation = orientation
		cls.dynamic = dynamic
		cls.name = name
		cls.country = country
		cls.validity: Validity = validity
		cls.t = t
		cls.width: Width = width
		cls.subtype = subtype
		cls.s = s
		cls.roll = roll
		cls.text = text
