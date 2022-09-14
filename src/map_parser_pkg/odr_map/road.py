from src.map_parser_pkg.odr_map.signals import Signals
from src.map_parser_pkg.odr_map.elevationprofile import Elevationprofile
from src.map_parser_pkg.odr_map.lanes import Lanes
from src.map_parser_pkg.odr_map.lateralprofile import Lateralprofile
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.planview import Planview
from src.map_parser_pkg.odr_map.objects import Objects
from src.map_parser_pkg.odr_map.junction import Junction
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.link import Link


class Road:
	def __init__(self,signals=None,elevationprofile=None,lanes=None,lateralprofile=None,userdata=None,id=None,planview=None,objects=None,junction=None,length=None,type=None,name=None,link=None):
		self.signals: Signals = signals
		self.elevationprofile: Elevationprofile = elevationprofile
		self.lanes: Lanes = lanes
		self.lateralprofile: Lateralprofile = lateralprofile
		self.userdata: Userdata = userdata
		self.id = id
		self.planview: Planview = planview
		self.objects: Objects = objects
		self.junction: Junction = junction
		self.length = length
		self.type: Type = type
		self.name = name
		self.link: Link = link
