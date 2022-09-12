from src.map_parser_pkg.odr_map.junction import Junction
from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.signals import Signals
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.lateralprofile import Lateralprofile
from src.map_parser_pkg.odr_map.elevationprofile import Elevationprofile
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.planview import Planview
from src.map_parser_pkg.odr_map.objects import Objects
from src.map_parser_pkg.odr_map.lanes import Lanes

class Road:
	def __init__(self,length=None,junction=None,link=None,name=None,id=None,signals=None,type=None,lateralProfile=None,elevationProfile=None,userData=None,planView=None,objects=None,lanes=None):
		self.length = length
		self.junction: Junction = junction
		self.link: Link = link
		self.name = name
		self.id = id
		self.signals: Signals = signals
		self.type: Type = type
		self.lateralprofile: Lateralprofile = lateralprofile
		self.elevationprofile: Elevationprofile = elevationprofile
		self.userdata: Userdata = userdata
		self.planview: Planview = planview
		self.objects: Objects = objects
		self.lanes: Lanes = lanes
