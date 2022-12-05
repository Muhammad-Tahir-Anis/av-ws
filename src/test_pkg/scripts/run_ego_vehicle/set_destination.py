from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class Destination:
    def __init__(self, road_id, lane_id):
        self.road_id = str(road_id)
        self.lane_id = str(lane_id)
        self.is_valid = self.validate_destination(self.road_id, self.lane_id)

    @property
    def is_destination(self):
        return self.is_valid

    @classmethod
    def validate_destination(cls, road_id, lane_id):
        roads = opendrive.road_list
        for road in roads:
            if road.id == road_id:
                left_lanes = road.lanes.lanesection.left
                if left_lanes:
                    is_lane = cls.check_lane(left_lanes, lane_id)
                    if is_lane:
                        return True
                right_lanes = road.lanes.lanesection.right
                if right_lanes:
                    is_lane = cls.check_lane(right_lanes, lane_id)
                    if is_lane:
                        return True
        return False

    @classmethod
    def check_lane(cls, lane_section, lane_id):
        if lane_section.lane_list:
            lanes = lane_section.lane_list
            for lane in lanes:
                if lane.id == lane_id and lane.type == "driving":
                    return True
            return False
        else:
            lanes = lane_section.lane
            if lanes.id == lane_id and lanes.type == "driving":
                return True
            return False
