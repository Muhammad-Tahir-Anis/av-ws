from src.test_pkg.town_map.userData import Userdata


class Header:
	def __init__(self, revMajor,revMinor,name,version,date,north,south,east,west,vendor,geoReference,userData):
		self.revMajor = revMajor

		self.revMinor = revMinor

		self.name = name

		self.version = version

		self.date = date

		self.north = north

		self.south = south

		self.east = east

		self.west = west

		self.vendor = vendor

		self.geoReference = geoReference

		self.userData: Userdata = userData