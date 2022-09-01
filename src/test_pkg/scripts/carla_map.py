import json


class_list = []


def main():
    with open('json_map.json') as map_data:
        # carla_map = json.load(map_data, object_hook=lambda d: SimpleNamespace(**d))
        carla_map = json.load(map_data)
        # print(type(carla_map))
        json_iterator(carla_map)
        for classes in class_list:
            print(classes)

        my_list = list(map(str, class_list))
        for classed in my_list:
            print(classed)


#
# def json_iterator(value):
#     """
#     This iterator traverse json dictionary branch by branch.
#     It will not go to another branch until current branch will be traversed completely
#     :param value: json dict
#     :return:
#     """
#     keys_list = []
#     if isinstance(value, dict):
#         if value.keys():
#             for key in value.keys():
#                 keys_list.append(key)
#                 print(key)
#                 json_iterator(value[key])
#     elif isinstance(value, list):
#         for index in value:
#             json_iterator(index)
#     else:
#         print(value)


def class_creator(name):
    class_list.append(type(name, (), {}))


def json_iterator(value):
    """
    This iterator traverse json dictionary branch by branch.
    It will not go to another branch until current branch will be traversed completely
    :param value: json dict
    :return:
    """
    keys_list = []
    if isinstance(value, dict):
        if value.keys():
            for key in value.keys():
                keys_list.append(key)
                print(key)
                # print(type(key, (), {}))
                if not isinstance(value[key], (str, type(None))):
                    class_type = type(key, (), {})
                    print(class_type)
                    if class_type in class_list:
                        pass
                    else:
                        class_creator(key)
                json_iterator(value[key])
    elif isinstance(value, list):
        for index in value:
            json_iterator(index)
    else:
        print(value)


if __name__ == '__main__':
    main()
