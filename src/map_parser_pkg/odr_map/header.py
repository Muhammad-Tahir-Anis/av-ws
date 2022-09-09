from src.map_parser_pkg.odr_map.userData import Userdata

class Header:
	def __init__(self,revMajor=None,revMinor=None,name=None,version=None,date=None,north=None,south=None,east=None,west=None,vendor=None,geoReference=None,userData=None):
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
