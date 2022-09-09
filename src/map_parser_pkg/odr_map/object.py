from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.outline import Outline

class Object:
	def __init__(self,id=None,name=None,s=None,t=None,zOffset=None,hdg=None,roll=None,pitch=None,orientation=None,type=None,width=None,length=None,outline=None):
		self.id = id
		self.name = name
		self.s = s
		self.t = t
		self.zOffset = zOffset
		self.hdg = hdg
		self.roll = roll
		self.pitch = pitch
		self.orientation = orientation
		self.type: Type = type
		self.width: Width = width
		self.length = length
		self.outline: Outline = outline
