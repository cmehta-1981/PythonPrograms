x, y = 10, 20  # global variables


class MyCLass:
    x, y = 30, 40  # Class variables

    def add(self):
        x, y = 50, 60  # local variables

        print('display class variables', +self.x, self.y)
        print('displays local variables ', +x, +y)
        print('display global variables', +globals()['x'], +globals()['y'])

    def __init__(self):
        print('constructor called ', +self.x, +self.y)  # print class variables


obj = MyCLass()  # invoke constructor automatically
obj.add()
