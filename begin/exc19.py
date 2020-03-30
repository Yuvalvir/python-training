class Person(object):
    def __init__(self, name="tal", age=20):
        self.__name = name
        self.___age = age

    def say(self):
        print "hi"

    def __str__(self):
        return "person {} is: {} years old".format(self.__name, self.___age)

    def get__name(self):
        return self.__name

    def get__age(self):
        return self.___age

    def set__name(self, name):
        self.__name = name

    def set__age(self, age):
        self.___age = age
