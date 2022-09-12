from src.map_parser_pkg.odr_map.lanelink import Lanelink
from src.map_parser_pkg.odr_map.lanelink import Lanelink
from typing import List

class Connection:
	def __init__(self,laneLink=None,incomingRoad=None,id=None,contactPoint=None,laneLink_list=None,connectingRoad=None):
		self.lanelink: Lanelink = lanelink
		self.incomingroad = incomingroad
		self.id = id
		self.contactpoint = contactpoint
		self.lanelink_list: List[Lanelink] = list()
		self.connectingroad = connectingroad
