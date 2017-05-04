class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.vintage = ""
        self.is_vintage()

    def get_age(self):
        self.year = 2016 - self.year

    def is_vintage(self):
        self.get_age()
        if self.year >= 50:
            self.vintage = "(vintage)"
        self.year = 2016 - self.year

    def __str__(self):
        return "{:>20} ({}), worth ${:10,.2f} {}".format(self.name, self.year, self.cost, self.vintage)
