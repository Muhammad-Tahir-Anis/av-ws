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

    def spawn_at_road(self,road_id: int, lane_section: str):
        roads = opendrive.road_list

        road_id = str(road_id)
        if isinstance(roads, list):
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
                            for lane in road.lanes.lanesection.left.lane_list:
                                if lane.type == "driving":
                                    self.driving_lanes.append(int(lane.id))
                            self.driving_lane = max(self.driving_lanes)
                            for lane in road.lanes.lanesection.left.lane_list:
                                if lane.id == str(self.driving_lane):
                                    self.lane_offset = float(lane.width.a)
                            return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_offset)
                    if lane_section == "right":
                        if road.lanes.lanesection.right.lane_list:
                            for lane in road.lanes.lanesection.right.lane_list:
                                if lane.type == "driving":
                                    self.driving_lanes.append(int(lane.id))
                            self.driving_lane = min(self.driving_lanes)
                            for lane in road.lanes.lanesection.right.lane_list:
                                if lane.id == str(self.driving_lane):
                                    self.lane_offset = float(lane.width.a)
                            return self.adjust_spawn_point(self.x,self.y,lane_section, self.heading, self.lane_offset)
                    # print(f"value of X:{x} \nvalue of Y:{y} \nvalue of heading:{heading}")

        else:
            if road_id == roads.id:
                if roads.planview.geometry_list:
                    self.x = roads.planview.geometry_list[0].x
                    self.y = roads.planview.geometry_list[0].y
                    self.heading = float(roads.planview.geometry_list[0].hdg)
                    # print(f"value of X:{x} \nvalue of Y:{y} \nvalue of heading:{heading}")
                    # according to OpenDrive standards value of 's' on first
                    # index of geometry list will always be 0

                else:
                    self.x = roads.planview.geometry.x
                    self.y = roads.planview.geometry.y
                    self.heading = roads.planview.geometry.hdg
                    # print(f"value of X:{x} \nvalue of Y:{y} \nvalue of heading:{heading}")

            else:
                print("Road not found on the map")

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
                y = y + lane_offset + lane_offset/len(cls.driving_lanes)
            elif heading_range_90[0] >= heading >= heading_range_90[1]:
                heading = heading
                w = heading
                x = x + lane_offset + lane_offset/len(cls.driving_lanes)
            elif heading_range_180[0] >= heading >= heading_range_180[1]:
                heading = 1
                w = 0
                y = y + lane_offset + lane_offset/len(cls.driving_lanes)
            elif heading_range_270[0] >= heading >= heading_range_270[1]:
                heading = heading
                w = - heading
                x = x + lane_offset + lane_offset/len(cls.driving_lanes)
            elif heading_range_360[0] >= heading >= heading_range_360[1]:
                heading = 0
                w = 0
                y = y + lane_offset + lane_offset/len(cls.driving_lanes)
            else:
                x = x
                y = y
            # w = heading
        if lane_section == "right":
            if heading_range_0[0] >= heading >= heading_range_0[1]:
                heading = 1
                w = 0
                if len(cls.driving_lanes) == 1:
                    y = y - lane_offset/2
                else:
                    y = y - (len(cls.driving_lanes)*lane_offset - lane_offset/2)
            elif heading_range_90[0] >= heading >= heading_range_90[1]:
                heading = heading
                w = -heading
                if len(cls.driving_lanes) == 1:
                    x = x - lane_offset / 2
                else:
                    x = x - (len(cls.driving_lanes) * lane_offset - lane_offset / 2)
            elif heading_range_180[0] >= heading >= heading_range_180[1]:
                heading = -1
                w = 0
                if len(cls.driving_lanes) == 1:
                    y = y - lane_offset / 2
                else:
                    y = y - (len(cls.driving_lanes) * lane_offset - lane_offset / 2)
            elif heading_range_270[0] >= heading >= heading_range_270[1]:
                heading = heading
                w = heading
                if len(cls.driving_lanes) == 1:
                    x = x - lane_offset / 2
                else:
                    x = x - (len(cls.driving_lanes) * lane_offset - lane_offset / 2)
            elif heading_range_360[0] >= heading >= heading_range_360[1]:
                heading = 1
                w = 0
                if len(cls.driving_lanes) == 1:
                    y = y - lane_offset / 2
                else:
                    y = y - (len(cls.driving_lanes) * lane_offset - lane_offset / 2)
            else:
                x = x
                y = y
            # w = -heading
        return x,y,heading,w


def main():
    odr_map = OdrMap()
    print(odr_map.spawn_at_road(11, "right"), len(odr_map.driving_lanes))


if __name__ == '__main__':
    main()
