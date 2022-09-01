
import rospy
from carla_msgs.srv import GetBlueprints


def get_blueprints_client():
    rospy.wait_for_service('carla/get_blueprints')
    try:
        blueprints_client = rospy.ServiceProxy('carla/get_blueprints',GetBlueprints)
        response = blueprints_client("")
        return response.blueprints
    except rospy.ServiceException as e:
        return "Exception Occurred : " + str(e)


def main():
    rospy.init_node('my_blueprint_node')

    blueprints = get_blueprints_client()
    # for blueprint in blueprints:
    print(blueprints)


if __name__ == '__main__':
    main()
