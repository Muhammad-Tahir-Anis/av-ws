from typing import List


class RoadNode:
    def __init__(self, previous_road, road_id, next_road):
        self.previous_road = previous_road
        self.road_id = road_id
        self.next_road = next_road


class JunctionNode:
    def __init__(self, junction_id, roads):
        self.junction_id = junction_id
        self.roads = roads
