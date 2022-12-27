
class DistanceThreshold:

    def __init__(self):
        self.threshold = 12.0
        pass

    def distance_calculator(self, npc_dist, ego_dist):
        distance_diff = npc_dist - ego_dist
        # if distance_diff >= 12.0:

    def avoid_obstacle(self, distance_diff):
        if distance_diff == self.threshold:
            pass


