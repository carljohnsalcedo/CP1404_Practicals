class Thing:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change(self, b):
        self.a += b
        