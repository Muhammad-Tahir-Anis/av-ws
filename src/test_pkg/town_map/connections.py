from src.test_pkg.town_map.laneLink import Lanelink


class Connections:
	def __init__(self, id,incomingRoad,connectingRoad,contactPoint,laneLink):
		self.id = id

		self.incomingRoad = incomingRoad

		self.connectingRoad = connectingRoad

		self.contactPoint = contactPoint

		self.laneLink: Lanelink = laneLink