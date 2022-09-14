from src.map_parser_pkg.odr_map.lanelink import Lanelink
from typing import List


class Connection:
	def __init__(self,lanelink_list=None,id=None,contactpoint=None,lanelink=None,incomingroad=None,connectingroad=None):
		self.lanelink_list: List[Lanelink] = lanelink_list
		self.id = id
		self.contactpoint = contactpoint
		self.lanelink: Lanelink = lanelink
		self.incomingroad = incomingroad
		self.connectingroad = connectingroad
