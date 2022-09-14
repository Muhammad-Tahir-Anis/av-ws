from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.outline import Outline
from src.map_parser_pkg.odr_map.width import Width


class Object:
	def __init__(self,orientation=None,s=None,id=None,height=None,type=None,pitch=None,outline=None,length=None,roll=None,hdg=None,name=None,zoffset=None,width=None,t=None):
		self.orientation = orientation
		self.s = s
		self.id = id
		self.height = height
		self.type: Type = type
		self.pitch = pitch
		self.outline: Outline = outline
		self.length = length
		self.roll = roll
		self.hdg = hdg
		self.name = name
		self.zoffset = zoffset
		self.width: Width = width
		self.t = t
