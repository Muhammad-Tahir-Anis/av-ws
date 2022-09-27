from src.map_parser_pkg.odr_map.lanelink import Lanelink
from typing import List


class Connection:
	def __init__(cls,lanelink=None,connectingroad=None,lanelink_list=None,id=None,contactpoint=None,incomingroad=None):
		cls.lanelink: Lanelink = lanelink
		cls.connectingroad = connectingroad
		cls.lanelink_list: List[Lanelink] = lanelink_list
		cls.id = id
		cls.contactpoint = contactpoint
		cls.incomingroad = incomingroad
