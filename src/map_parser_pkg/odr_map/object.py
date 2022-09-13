from src.map_parser_pkg.odr_map.width import Width
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.outline import Outline

class Object:
	def __init__(self,pitch=None,t=None,height=None,width=None,orientation=None,s=None,length=None,zoffset=None,name=None,type=None,hdg=None,id=None,outline=None,roll=None):
		self.pitch = pitch
		self.t = t
		self.height = height
		self.width: Width = width
		self.orientation = orientation
		self.s = s
		self.length = length
		self.zoffset = zoffset
		self.name = name
		self.type: Type = type
		self.hdg = hdg
		self.id = id
		self.outline: Outline = outline
		self.roll = roll
