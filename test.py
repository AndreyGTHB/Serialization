from Serializable import Serializable

ser = Serializable("json", "test.json")

# test 1
print(ser.read_file())


class A(object):
    def __init__(self):
        super(A, self).__init__()

        self.num = 1
        self.second_num = 2


a = A()
print (dir(a))
