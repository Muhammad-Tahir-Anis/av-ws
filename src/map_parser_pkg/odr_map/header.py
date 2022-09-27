from src.map_parser_pkg.odr_map.userdata import Userdata


class Header:
	def __init__(cls,revmajor=None,revminor=None,name=None,version=None,date=None,north=None,south=None,east=None,west=None,vendor=None,georeference=None,userdata=None):
		cls.revmajor = revmajor
		cls.revminor = revminor
		cls.name = name
		cls.version = version
		cls.date = date
		cls.north = north
		cls.south = south
		cls.east = east
		cls.west = west
		cls.vendor = vendor
		cls.georeference = georeference
		cls.userdata: Userdata = userdata
