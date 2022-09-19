import rospy
from carla_msgs.srv import DestroyObject


def destroy_object_srv():
    rospy.wait_for_service('/carla/destroy_object')
    try:
        service = rospy.ServiceProxy('/carla/destroy_object', DestroyObject)
        response = service(32)
        return response
    except rospy.ServiceException as e:
        return e


def main():
    response = destroy_object_srv()
    print(response)


if __name__ == '__main__':
    main()
