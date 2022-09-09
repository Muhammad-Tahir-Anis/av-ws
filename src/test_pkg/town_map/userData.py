from src.test_pkg.town_map.vectorLane import Vectorlane
from typing import List
from src.test_pkg.town_map.vectorLane import Vectorlane
from src.test_pkg.town_map.vectorJunction import Vectorjunction
from src.test_pkg.town_map.vectorSignal import Vectorsignal
from src.test_pkg.town_map.vectorScene import Vectorscene
from src.test_pkg.town_map.vectorRoad import Vectorroad


class Userdata:
	def __init__(self, vectorLane_list,vectorLane,vectorJunction,vectorSignal,vectorScene,vectorRoad):
		self.vectorLane_list: List[Vectorlane] = list()
		self.vectorLane: Vectorlane = vectorLane
		self.vectorJunction: Vectorjunction = vectorJunction
		self.vectorSignal: Vectorsignal = vectorSignal
		self.vectorScene: Vectorscene = vectorScene
		self.vectorRoad: Vectorroad = vectorRoad