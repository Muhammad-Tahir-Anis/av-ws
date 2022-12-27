
from src.map_parser_pkg.scripts.odr_map_obj import opendrive


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

    def road_info(self, road_id, s_axis, t_axis):
        # Getting all roads data from map
        roads = opendrive.road_list
        for road in roads:
            # For right lanes
            if road_id == road.id:
                print("ST: road info : ", s_axis, t_axis)

                # Checking road geometries
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
                    self.s_value = float(geometry.s)
                    if geometry.arc:
                        self.curvature = float(geometry.arc.curvature)

        return self.x_origin, self.y_origin, self.heading, self.curvature
