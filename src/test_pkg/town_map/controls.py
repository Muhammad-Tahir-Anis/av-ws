from src.test_pkg.town_map.type import Type


class Controls:
	def __init__(self, signalId,type):
		self.signalId = signalId

		self.type: Type = type