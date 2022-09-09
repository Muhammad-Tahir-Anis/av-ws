from src.test_pkg.town_map.type import Type


class Controllers:
	def __init__(self, id,type,sequence):
		self.id = id

		self.type: Type = type
		self.sequence = sequence
