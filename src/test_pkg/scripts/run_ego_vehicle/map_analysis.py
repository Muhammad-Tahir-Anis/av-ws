from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.logs import Log


class MapAnalysis:
    x_origin: float = 0
    y_origin: float = 0
    heading: float = 0
    curvature: float = 0
    road_ended: bool = False
    s_value: float = 0

    def __int__(self):
        self.x_origin: float = 0
        self.y_origin: float = 0
        self.heading: float = 0
        self.curvature: float = 0
        self.s_value: float = 0

    def road_info(self, road_id, s_axis, log: Log):
        roads = opendrive.road_list
        for road in roads:
            if road_id == road.id:
                if s_axis > float(road.length):
                    # print("S: road info : ", s_axis)
                    log.s_axis = s_axis
                    self.road_ended = True
                    self.s_value = 0
                else:
                    self.road_ended = False
                    # print("Road_id:", road_id)
                    log.road_id = road_id
                if road.planview.geometry_list:
                    geometries = road.planview.geometry_list
                    for geometry in geometries:
                        if geometries.index(geometry) < len(geometries) - 1:
                            next_geometry = geometries[geometries.index(geometry) + 1]
                            geometry.s = float(geometry.s)
                            next_geometry.s = float(next_geometry.s)
                            if geometry.s <= s_axis < next_geometry.s:
                                if geometry.arc:
                                    self.curvature = float(geometry.arc.curvature)
                                self.heading = float(geometry.hdg)
                                self.x_origin = float(geometry.x)
                                self.y_origin = float(geometry.y)
                                self.s_value = float(geometry.s)
                        elif geometries[len(geometries) - 1]:
                            if geometry.s <= s_axis:
                                if geometry.arc:
                                    self.curvature = float(geometry.arc.curvature)
                                self.heading = float(geometry.hdg)
                                self.x_origin = float(geometry.x)
                                self.y_origin = float(geometry.y)
                                self.s_value = float(geometry.s)
                else:
                    geometry = road.planview.geometry
                    self.heading = float(geometry.hdg)
                    self.x_origin = float(geometry.x)
                    self.y_origin = float(geometry.y)

        return self.x_origin, self.y_origin, self.heading, self.curvature, self.s_value, self.road_ended
