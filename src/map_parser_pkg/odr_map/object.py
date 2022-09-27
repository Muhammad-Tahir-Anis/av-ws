from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.outline import Outline
from src.map_parser_pkg.odr_map.type import Type


class Object:
	def __init__(cls,width=None,outline=None,name=None,id=None,height=None,s=None,hdg=None,roll=None,pitch=None,orientation=None,length=None,zoffset=None,type=None,t=None):
		cls.width: Width = width
		cls.outline: Outline = outline
		cls.name = name
		cls.id = id
		cls.height = height
		cls.s = s
		cls.hdg = hdg
		cls.roll = roll
		cls.pitch = pitch
		cls.orientation = orientation
		cls.length = length
		cls.zoffset = zoffset
		cls.type: Type = type
		cls.t = t
