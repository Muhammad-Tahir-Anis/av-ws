from src.map_parser_pkg.odr_map.elevationprofile import Elevationprofile
from src.map_parser_pkg.odr_map.junction import Junction
from src.map_parser_pkg.odr_map.lateralprofile import Lateralprofile
from src.map_parser_pkg.odr_map.signals import Signals
from src.map_parser_pkg.odr_map.userdata import Userdata
from src.map_parser_pkg.odr_map.planview import Planview
from src.map_parser_pkg.odr_map.link import Link
from src.map_parser_pkg.odr_map.lanes import Lanes
from src.map_parser_pkg.odr_map.type import Type
from src.map_parser_pkg.odr_map.objects import Objects


class Road:
	def __init__(cls,elevationprofile=None,junction=None,lateralprofile=None,name=None,id=None,signals=None,userdata=None,planview=None,link=None,length=None,lanes=None,type=None,objects=None):
		cls.elevationprofile: Elevationprofile = elevationprofile
		cls.junction: Junction = junction
		cls.lateralprofile: Lateralprofile = lateralprofile
		cls.name = name
		cls.id = id
		cls.signals: Signals = signals
		cls.userdata: Userdata = userdata
		cls.planview: Planview = planview
		cls.link: Link = link
		cls.length = length
		cls.lanes: Lanes = lanes
		cls.type: Type = type
		cls.objects: Objects = objects
