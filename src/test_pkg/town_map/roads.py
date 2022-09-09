from src.test_pkg.town_map.signals import Signals
from src.test_pkg.town_map.planView import Planview
from src.test_pkg.town_map.junction import Junction
from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.objects import Objects
from src.test_pkg.town_map.link import Link
from src.test_pkg.town_map.lateralProfile import Lateralprofile
from src.test_pkg.town_map.lanes import Lanes
from src.test_pkg.town_map.elevationProfile import Elevationprofile
from src.test_pkg.town_map.userData import Userdata


class Roads:
	def __init__(self, signals,name,planView,length,id,junction,type,objects,link,lateralProfile,lanes,elevationProfile,userData):
		self.signals: Signals = signals
		self.name = name

		self.planView: Planview = planView
		self.length = length

		self.id = id

		self.junction: Junction = junction
		self.type: Type = type
		self.objects: Objects = objects
		self.link: Link = link
		self.lateralProfile: Lateralprofile = lateralProfile
		self.lanes: Lanes = lanes
		self.elevationProfile: Elevationprofile = elevationProfile
		self.userData: Userdata = userData