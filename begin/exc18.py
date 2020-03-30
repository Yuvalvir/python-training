class Dog(object):
    def __init__(self,x="bobi"):
        self.__name = x
        self.__age = 5

    def birthday(self):
        self.age += 1

    def get_birthday(self):
        return self.age

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return "Dog name and age: {}.{}".format(self.get_name(), self.get_age())
