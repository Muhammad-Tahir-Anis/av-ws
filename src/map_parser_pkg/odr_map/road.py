from src.map_parser_pkg.odr_map.signals import Signals
from src.map_parser_pkg.odr_map.planview import Planview
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.lanes import Lanes
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.junction import Junction
from src.map_parser_pkg.odr_map.lateralprofile import Lateralprofile
from src.map_parser_pkg.odr_map.objects import Objects
from src.map_parser_pkg.odr_map.elevationprofile import Elevationprofile
from src.map_parser_pkg.odr_map.link import Link


class Road:
	def __init__(self,signals=None,id=None,planview=None,type=None,lanes=None,length=None,userdata=None,junction=None,lateralprofile=None,objects=None,name=None,elevationprofile=None,link=None):
		self.signals: Signals = signals
		self.id = id
		self.planview: Planview = planview
		self.type: Type = type
		self.lanes: Lanes = lanes
		self.length = length
		self.userdata: Userdata = userdata
		self.junction: Junction = junction
		self.lateralprofile: Lateralprofile = lateralprofile
		self.objects: Objects = objects
		self.name = name
		self.elevationprofile: Elevationprofile = elevationprofile
		self.link: Link = link
