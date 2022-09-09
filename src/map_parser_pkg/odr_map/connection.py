from src.map_parser_pkg.odr_map.laneLink import Lanelink
from typing import List

class Connection:
	def __init__(self,id=None,incomingRoad=None,connectingRoad=None,contactPoint=None,laneLink_list=None):
		self.id = id
		self.incomingRoad = incomingRoad
		self.connectingRoad = connectingRoad
		self.contactPoint = contactPoint
		self.laneLink_list: List[Lanelink] = list()
