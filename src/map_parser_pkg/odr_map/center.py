from src.map_parser_pkg.odr_map.lane import Lane


class Center:
	def __init__(cls,lane=None):
		cls.lane: Lane = lane
