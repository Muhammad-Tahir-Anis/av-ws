from src.map_parser_pkg.odr_map.outline import Outline
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width

class Object:
	def __init__(self,outline=None,length=None,type=None,s=None,name=None,width=None,height=None,t=None,id=None,zOffset=None,orientation=None,pitch=None,hdg=None,roll=None):
		self.outline: Outline = outline
		self.length = length
		self.type: Type = type
		self.s = s
		self.name = name
		self.width: Width = width
		self.height = height
		self.t = t
		self.id = id
		self.zoffset = zoffset
		self.orientation = orientation
		self.pitch = pitch
		self.hdg = hdg
		self.roll = roll
