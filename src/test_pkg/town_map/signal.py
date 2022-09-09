from src.test_pkg.town_map.width import Width
from src.test_pkg.town_map.userData import Userdata
from src.test_pkg.town_map.validity import Validity
from src.test_pkg.town_map.type import Type


class Signal:
	def __init__(self, dynamic,roll,zOffset,s,t,subtype,text,width,userData,pitch,validity,value,name,country,height,orientation,hOffset,id,type):
		self.dynamic = dynamic

		self.roll = roll

		self.zOffset = zOffset

		self.s = s

		self.t = t

		self.subtype = subtype

		self.text = text

		self.width: Width = width
		self.userData: Userdata = userData
		self.pitch = pitch

		self.validity: Validity = validity
		self.value = value

		self.name = name

		self.country = country

		self.height = height

		self.orientation = orientation

		self.hOffset = hOffset

		self.id = id

		self.type: Type = type