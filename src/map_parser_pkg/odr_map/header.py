from src.map_parser_pkg.odr_map.userdata import Userdata


class Header:
	def __init__(self,revmajor=None,revminor=None,name=None,version=None,date=None,north=None,south=None,east=None,west=None,vendor=None,georeference=None,userdata=None):
		self.revmajor = revmajor
		self.revminor = revminor
		self.name = name
		self.version = version
		self.date = date
		self.north = north
		self.south = south
		self.east = east
		self.west = west
		self.vendor = vendor
		self.georeference = georeference
		self.userdata: Userdata = userdata
