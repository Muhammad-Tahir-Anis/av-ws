from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.junction import Junction
from src.map_parser_pkg.odr_map.signals import Signals
from src.map_parser_pkg.odr_map.planview import Planview
from src.map_parser_pkg.odr_map.lateralprofile import Lateralprofile
from src.map_parser_pkg.odr_map.objects import Objects
from src.map_parser_pkg.odr_map.elevationprofile import Elevationprofile
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.lanes import Lanes

class Road:
	def __init__(self,link=None,userdata=None,junction=None,length=None,name=None,signals=None,planview=None,lateralprofile=None,objects=None,id=None,elevationprofile=None,type=None,lanes=None):
		self.link: Link = link
		self.userdata = userdata
		self.junction: Junction = junction
		self.length = length
		self.name = name
		self.signals: Signals = signals
		self.planview = planview
		self.lateralprofile = lateralprofile
		self.objects: Objects = objects
		self.id = id
		self.elevationprofile = elevationprofile
		self.type: Type = type
		self.lanes: Lanes = lanes
