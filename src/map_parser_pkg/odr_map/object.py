from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.outline import Outline
from src.map_parser_pkg.odr_map.width import Width


class Object:
	def __init__(self,type=None,id=None,s=None,zoffset=None,hdg=None,roll=None,length=None,height=None,orientation=None,pitch=None,outline=None,t=None,name=None,width=None):
		self.type: Type = type
		self.id = id
		self.s = s
		self.zoffset = zoffset
		self.hdg = hdg
		self.roll = roll
		self.length = length
		self.height = height
		self.orientation = orientation
		self.pitch = pitch
		self.outline: Outline = outline
		self.t = t
		self.name = name
		self.width: Width = width
