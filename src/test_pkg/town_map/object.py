from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.width import Width
from src.test_pkg.town_map.outline import Outline


class Object:
	def __init__(self, orientation,name,zOffset,roll,s,id,t,hdg,type,length,width,height,outline,pitch):
		self.orientation = orientation

		self.name = name

		self.zOffset = zOffset

		self.roll = roll

		self.s = s

		self.id = id

		self.t = t

		self.hdg = hdg

		self.type: Type = type
		self.length = length

		self.width: Width = width
		self.height = height

		self.outline: Outline = outline
		self.pitch = pitch
