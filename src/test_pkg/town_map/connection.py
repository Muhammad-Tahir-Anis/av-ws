from src.test_pkg.town_map.laneLink import Lanelink
from src.test_pkg.town_map.laneLink import Lanelink
from typing import List


class Connection:
	def __init__(self, incomingRoad,contactPoint,id,laneLink,connectingRoad,laneLink_list):
		self.incomingRoad = incomingRoad

		self.contactPoint = contactPoint

		self.id = id

		self.laneLink: Lanelink = laneLink
		self.connectingRoad = connectingRoad

		self.laneLink_list: List[Lanelink] = list()