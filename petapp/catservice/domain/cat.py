class Cat:
    def __init__(self, name):
        self.name = name

    def pet(self):
        return "purr"

    @staticmethod
    def from_name(name):
        return Cat(name)