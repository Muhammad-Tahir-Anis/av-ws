import math

from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class OdrMap:
    lane_width = None
    driving_lane = None
    driving_lanes: list = list()
    _road = None

    def __init__(self):
        self.lane_width = None
        self.lane_offset = None
        self.heading = None
        self.y = None
        self.x = None

    def spawn_at_road(self, road_id: int, lane_section: str):
        roads = opendrive.road_list
        road_id = str(road_id)
        for road in roads:
            if road_id == road.id:
                self._road = road
            else:
                print("Junction")
        if self._road.planview.geometry_list:
            self.x = float(self._road.planview.geometry_list[0].x)
            self.y = float(self._road.planview.geometry_list[0].y)
            self.heading = float(self._road.planview.geometry_list[0].hdg)
            # according to OpenDrive standards value of 's' on first
            # index of geometry list will always be 0
        else:
            self.x = float(self._road.planview.geometry.x)
            self.y = float(self._road.planview.geometry.y)
            self.heading = float(self._road.planview.geometry.hdg)
        if self._road.lanes.laneoffset_list:
            self.lane_offset = float(self._road.lanes.laneoffset_list[0].a)
        else:
            self.lane_offset = float(self._road.lanes.laneoffset.a)
        if lane_section == "left":
            if self._road.lanes.lanesection.left.lane_list:
                lane_section_list = self._road.lanes.lanesection.left.lane_list
            else:
                lane_section_list = self._road.lanes.lanesection.left.lane
            self.lane_width = self.select_lane_section(lane_section_list)
            if self.lane_offset >= 0:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               self.lane_offset)
            else:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               lane_offset=0)
        if lane_section == "right":
            if self._road.lanes.lanesection.right.lane_list:
                lane_section_list = self._road.lanes.lanesection.right.lane_list
            else:
                lane_section_list = self._road.lanes.lanesection.right.lane
            self.lane_width = self.select_lane_section(lane_section_list)
            if self.lane_offset <= 0:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               -self.lane_offset)
            else:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               lane_offset=0)

    @classmethod
    def select_lane_section(cls, lane_section_list):
        if isinstance(lane_section_list, list):
            for lane in lane_section_list:
                if lane.type == "driving":
                    cls.driving_lanes.append(lane.id)
            cls.driving_lane = int(max(cls.driving_lanes))
            print(cls.driving_lanes)
            print(cls.driving_lane)
            for lane in lane_section_list:
                if lane.id == str(cls.driving_lane):
                    cls.lane_width = float(lane.width.a)
        else:
            if lane_section_list.type == "driving":
                cls.driving_lanes.append(int(lane_section_list.id))
            if lane_section_list.id == str(cls.driving_lane):
                cls.lane_width = float(lane_section_list.width.a)
        return cls.lane_width

    @classmethod
    def adjust_spawn_point(cls, x, y, lane_section, heading, lane_width, lane_offset):
        w = 0
        print(x)
        print(y)
        s_translation = x - x
        t_translation = y - y
        s = (s_translation * math.cos(heading)) - (t_translation * math.sin(heading))
        t = (t_translation * math.cos(heading)) - (s_translation * math.sin(heading))
        print(s, t)
        # s = (x*math.cos(heading)) - (y*math.sin(heading))
        # t = (y*math.cos(heading)) - (x*math.sin(heading))
        # heading_range_0 = [0 + 1, 0 - 1]
        # heading_range_90 = [(math.pi / 2) + 1, (math.pi / 2) - 1]
        # heading_range_180 = [math.pi + 1, math.pi - 1]
        # heading_range_270 = [(3 * math.pi / 2) + 1, (3 * math.pi / 2) - 1]
        # heading_range_360 = [(2 * math.pi) + 1, (2 * math.pi) - 1]
        # if lane_section == "left":
        #     if heading_range_0[0] >= heading >= heading_range_0[1]:
        #         heading = 0
        #         w = 0
        #         y = y + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_90[0] >= heading >= heading_range_90[1]:
        #         heading = heading
        #         w = heading
        #         x = x + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_180[0] >= heading >= heading_range_180[1]:
        #         heading = 1
        #         w = 0
        #         y = y + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_270[0] >= heading >= heading_range_270[1]:
        #         heading = heading
        #         w = - heading
        #         x = x + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_360[0] >= heading >= heading_range_360[1]:
        #         heading = 0
        #         w = 0
        #         y = y + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        #     else:
        #         w = 0
        #         x = x
        #         y = y
        # if lane_section == "right":
        #     if heading_range_0[0] >= heading >= heading_range_0[1]:
        #         heading = 1
        #         w = 0
        #         y = y - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_90[0] >= heading >= heading_range_90[1]:
        #         heading = heading
        #         w = -heading
        #         x = x - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_180[0] >= heading >= heading_range_180[1]:
        #         heading = 0
        #         w = 0
        #         y = y - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_270[0] >= heading >= heading_range_270[1]:
        #         heading = heading
        #         w = heading
        #         x = x - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
        #     elif heading_range_360[0] >= heading >= heading_range_360[1]:
        #         heading = 1
        #         w = 0
        #         y = y - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
        #     else:
        #         w = 0
        #         x = x
        #         y = y

        if lane_section == "left":
            t = t + lane_offset + cls.center_lane(len(cls.driving_lanes),lane_width)
            w = heading
        if lane_section == "right":
            t = t - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
            w = 0
        print(s, t)
        y = y + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        x_translation = t_translation + y
        y_translation = s_translation + x
        x = (x_translation * math.cos(-heading) - y_translation * math.sin(-heading))
        y = (y_translation * math.cos(-heading) - x_translation * math.sin(-heading))
        print(x,y)

        return x, y, heading, w

    @classmethod
    def center_lane(cls, no_of_lanes, lane_width):
        point = ((2 * no_of_lanes - 1) / 2) * lane_width
        print(point)
        return point

    def normalize_s(self, last_s, next_road, s_list):
        for road in opendrive.road_list:
            if float(road.id) == next_road:
                if road.planview.geometry_list:
                    for geometry in road.planview.geometry_list:
                        s_list.append([float(geometry.s) + last_s, road.id])
                    last_s = float(road.planview.geometry_list[len(road.planview.geometry_list) - 1].s)
                else:
                    s_list.append([float(road.planview.geometry.s) + last_s, road.id])
                    last_s = float(road.planview.geometry.s)
                next_road = float(self.what_next(next_road)[0])
                self.normalize_s(last_s, next_road, s_list)

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
    odr_map.spawn_at_road(0, "right")


if __name__ == '__main__':
    main()
