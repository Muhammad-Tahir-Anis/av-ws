from src.test_pkg.town_map.planView import Planview
from src.test_pkg.town_map.junction import Junction
from src.test_pkg.town_map.lateralProfile import Lateralprofile
from src.test_pkg.town_map.link import Link
from src.test_pkg.town_map.signals import Signals
from src.test_pkg.town_map.elevationProfile import Elevationprofile
from src.test_pkg.town_map.lanes import Lanes
from src.test_pkg.town_map.userData import Userdata
from src.test_pkg.town_map.type import Type
from src.test_pkg.town_map.objects import Objects


class Road:
	def __init__(self, planView,name,junction,lateralProfile,link,signals,id,length,elevationProfile,lanes,userData,type,objects):
		self.planView: Planview = planView
		self.name = name

		self.junction: Junction = junction
		self.lateralProfile: Lateralprofile = lateralProfile
		self.link: Link = link
		self.signals: Signals = signals
		self.id = id

		self.length = length

		self.elevationProfile: Elevationprofile = elevationProfile
		self.lanes: Lanes = lanes
		self.userData: Userdata = userData
		self.type: Type = type
		self.objects: Objects = objects