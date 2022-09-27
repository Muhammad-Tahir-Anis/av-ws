import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from ego_vehicle_control import EgoController
from gnss_status import GnssData
from src.map_parser_pkg.scripts.odr_map_obj import opendrive


def xy_to_st(x, y, road_id):
    for road in opendrive.road_list:
        if road_id == road.id:
            s = abs(float(road.planview.geometry_list[0].x) - x)
            t = abs(float(road.planview.geometry_list[0].y) - y)
            return s, t


def callback(data):
    # print(data)
    gnss = GnssData()
    t, s = xy_to_st(gnss.x, gnss.y, "0")
    print(gnss.x, gnss.y)
    print(s, t)
    if s <= 90:
        EgoController(data.header, 0.1, 0.0, 0.0, 0, 0, 0, 0)
    else:
        EgoController(data.header, 0, 0, 1, 0, 0, 0, 0)
    # rospy.spin()


def ego_vehicle_status_subscriber():
    sub = rospy.Subscriber('/carla/ego_vehicle/vehicle_status', CarlaEgoVehicleStatus, callback)
    rospy.spin()


def main():
    rospy.init_node('av_ego_status')
    ego_vehicle_status_subscriber()


if __name__ == '__main__':
    main()
