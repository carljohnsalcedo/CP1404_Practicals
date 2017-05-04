class Point:
    def __init__(self, x=0, y=0):
        self.x_point = x
        self.y_point = y

    def __str__(self):
        return "({},{})".format(self.x_point, self.y_point)

    def move(self, dx, dy):
        self.x_point = self.x_point + dx
        self.y_point = self.y_point + dy

    def reset(self):
        self.x_point = 0
        self.y_point = 0
