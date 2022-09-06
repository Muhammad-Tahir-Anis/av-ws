import json

classes_list = []


def main():
    with open('json_map.json') as map_data:
        carla_map = json.load(map_data)
        json_iterator(carla_map)
        for attribute in classes_list:
            print(attribute)


def get_classes(key, value):
    if isinstance(value, list):
        for index in value:
            get_classes(key, index)
    else:
        if not str((key, list(value))) in classes_list:
            classes_list.append(str((key, list(value))))


def class_creator(key, value):
    """
    This function creates list of possible classes which is essential to make TOW-MAP model class for creating map
    object for future use
     :param value:
     :param key:
     :return:
    """
    get_classes(key, value)

    for my_class in classes_list:
        str_to_class(my_class)
    # class_list.append(type(name, (), attribute_list))
    # with open("%s.py"%name, "w") as python_file:
    #     class_temp = "class {name}:\n\tdef __init__(self,{attributes})"


def str_to_class(class_string):
    my_class = list(class_string.split(","))
    print(my_class)


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
                # print(key)  # At this point we got keys of json.

                # This if condition checks that the key should not have the value of type string or none to make
                # relevant classes
                if not isinstance(value[key], (str, type(None))):
                    class_creator(key, value[key])
                json_iterator(value[key])
    elif isinstance(value, list):
        for index in value:
            json_iterator(index)
    else:
        pass
        # print(value)


if __name__ == '__main__':
    main()
