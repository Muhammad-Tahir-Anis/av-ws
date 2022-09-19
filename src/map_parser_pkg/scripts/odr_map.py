import math

from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class OdrMap:
    driving_lanes: list = list()
    driving_lane: int = 0
    x: float = 0
    y: float = 0
    heading: float = 0
    lane_offset: float = 0

    def __init__(self):
        pass

    def spawn_at_road(self, road_id: int, lane_section: str):
        roads = opendrive.road_list

        road_id = str(road_id)
        for road in roads:
            if road_id == road.id:
                if road.planview.geometry_list:
                    self.x = float(road.planview.geometry_list[0].x)
                    self.y = float(road.planview.geometry_list[0].y)
                    self.heading = float(road.planview.geometry_list[0].hdg)
                    # according to OpenDrive standards value of 's' on first
                    # index of geometry list will always be 0
                else:
                    self.x = float(road.planview.geometry.x)
                    self.y = float(road.planview.geometry.y)
                    self.heading = float(road.planview.geometry.hdg)
                if lane_section == "left":
                    if road.lanes.lanesection.left.lane_list:
                        lane_section_list = road.lanes.lanesection.left.lane_list
                    else:
                        lane_section_list = road.lanes.lanesection.left.lane
                    self.lane_offset = self.select_lane(lane_section_list)
                    return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_offset)
                if lane_section == "right":
                    if road.lanes.lanesection.right.lane_list:
                        lane_section_list = road.lanes.lanesection.right.lane_list
                    else:
                        lane_section_list = road.lanes.lanesection.right.lane
                    self.lane_offset = self.select_lane(lane_section_list)
                    return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_offset)
            else:
                print("Junction")

    @classmethod
    def select_lane(cls, lane_section_list):
        if isinstance(lane_section_list, list):
            for lane in lane_section_list:
                if lane.type == "driving":
                    cls.driving_lanes.append(lane.id)
            cls.driving_lane = int(max(cls.driving_lanes))
            print(cls.driving_lanes)
            print(cls.driving_lane)
            for lane in lane_section_list:
                if lane.id == str(cls.driving_lane):
                    cls.lane_offset = float(lane.width.a)
        else:
            if lane_section_list.type == "driving":
                cls.driving_lanes.append(int(lane_section_list.id))
            if lane_section_list.id == str(cls.driving_lane):
                cls.lane_offset = float(lane_section_list.width.a)
        return cls.lane_offset

    @classmethod
    def adjust_spawn_point(cls, x, y, lane_section, heading, lane_offset):
        global w
        heading_range_0 = [0 + 1, 0 - 1]
        heading_range_90 = [(math.pi / 2) + 1, (math.pi / 2) - 1]
        heading_range_180 = [math.pi + 1, math.pi - 1]
        heading_range_270 = [(3 * math.pi / 2) + 1, (3 * math.pi / 2) - 1]
        heading_range_360 = [(2 * math.pi) + 1, (2 * math.pi) - 1]
        if lane_section == "left":
            if heading_range_0[0] >= heading >= heading_range_0[1]:
                heading = 0
                w = 0
                y = y + cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_90[0] >= heading >= heading_range_90[1]:
                heading = heading
                w = heading
                x = x + cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_180[0] >= heading >= heading_range_180[1]:
                heading = 1
                w = 0
                y = y + cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_270[0] >= heading >= heading_range_270[1]:
                heading = heading
                w = - heading
                x = x + cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_360[0] >= heading >= heading_range_360[1]:
                heading = 0
                w = 0
                y = y + cls.center_lane(len(cls.driving_lanes), lane_offset)
            else:
                x = x
                y = y
        if lane_section == "right":
            if heading_range_0[0] >= heading >= heading_range_0[1]:
                heading = 1
                w = 0
                y = y - cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_90[0] >= heading >= heading_range_90[1]:
                heading = heading
                w = -heading
                x = x - cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_180[0] >= heading >= heading_range_180[1]:
                heading = 0
                w = 0
                y = y - cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_270[0] >= heading >= heading_range_270[1]:
                heading = heading
                w = heading
                x = x - cls.center_lane(len(cls.driving_lanes), lane_offset)
            elif heading_range_360[0] >= heading >= heading_range_360[1]:
                heading = 1
                w = 0
                y = y - cls.center_lane(len(cls.driving_lanes), lane_offset)
            else:
                x = x
                y = y
        return x, y, heading, w

    @classmethod
    def center_lane(cls, no_of_lanes, lane_offset):
        point = ((2 * no_of_lanes - 1) / 2) * lane_offset
        print(point)
        return point

    def normalize_s(self, last_s, next_road, s_list):
        for road in opendrive.road_list:
            if float(road.id) == next_road:
                if road.planview.geometry_list:
                    for geometry in road.planview.geometry_list:
                        s_list.append([float(geometry.s)+last_s, road.id])
                    last_s = float(road.planview.geometry_list[len(road.planview.geometry_list)-1].s)
                else:
                    s_list.append([float(road.planview.geometry.s)+last_s, road.id])
                    last_s = float(road.planview.geometry.s)
                next_road = float(self.what_next(next_road)[0])
                self.normalize_s(last_s,next_road,s_list)

    def what_s(self):
        s_list = []
        last_s = 0
        next_road = 0
        self.normalize_s(last_s, next_road, s_list)
        [print(s) for s in s_list]

    def what_next(self, road_id):
        roads = opendrive.road_list
        for road in roads:
            if road_id == float(road.id):
                next_road = road.link.successor.elementid
                previous_road = road.link.predecessor.elementid
                return next_road, previous_road


def main():
    odr_map = OdrMap()
    odr_map.what_s()


if __name__ == '__main__':
    main()
