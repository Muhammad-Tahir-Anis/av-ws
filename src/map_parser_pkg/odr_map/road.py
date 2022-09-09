from src.map_parser_pkg.odr_map.junction import Junction
from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.planView import Planview
from src.map_parser_pkg.odr_map.elevationProfile import Elevationprofile
from src.map_parser_pkg.odr_map.lateralProfile import Lateralprofile
from src.map_parser_pkg.odr_map.lanes import Lanes
from src.map_parser_pkg.odr_map.userData import Userdata

class Road:
	def __init__(self,name=None,length=None,id=None,junction=None,link=None,planView=None,elevationProfile=None,lateralProfile=None,lanes=None,userData=None):
		self.name = name
		self.length = length
		self.id = id
		self.junction: Junction = junction
		self.link: Link = link
		self.planView: Planview = planView
		self.elevationProfile: Elevationprofile = elevationProfile
		self.lateralProfile: Lateralprofile = lateralProfile
		self.lanes: Lanes = lanes
		self.userData: Userdata = userData
