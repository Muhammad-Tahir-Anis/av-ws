import pickle


class NpcDataStorage:
    def __init__(self):
        # self.param = param
        # self.save = save_object(param)
        pass

    @classmethod
    def save_object(cls, obj):
        try:
            with open("data.pickle", "wb") as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

    @classmethod
    def load_object(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)


# load_file = NpcDataStorage()
# data = load_file.load_object("data.pickle")
#
# print(data)
# print(isinstance(obj, MyClass))