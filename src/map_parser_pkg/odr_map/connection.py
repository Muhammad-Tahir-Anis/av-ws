from src.map_parser_pkg.odr_map.lanelink import Lanelink
from typing import List
from src.map_parser_pkg.odr_map.lanelink import Lanelink

class Connection:
	def __init__(self,lanelink_list=None,contactpoint=None,connectingroad=None,lanelink=None,incomingroad=None,id=None):
		self.lanelink_list = lanelink_list
		self.contactpoint = contactpoint
		self.connectingroad = connectingroad
		self.lanelink = lanelink
		self.incomingroad = incomingroad
		self.id = id
