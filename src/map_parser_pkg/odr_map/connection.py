from src.map_parser_pkg.odr_map.lanelink import Lanelink
from typing import List


class Connection:
	def __init__(self,connectingroad=None,lanelink_list=None,lanelink=None,id=None,incomingroad=None,contactpoint=None):
		self.connectingroad = connectingroad
		self.lanelink_list: List[Lanelink] = lanelink_list
		self.lanelink: Lanelink = lanelink
		self.id = id
		self.incomingroad = incomingroad
		self.contactpoint = contactpoint
