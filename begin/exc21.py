class BigThing(object):
    def __init__(self, x):
        self.__x = x

    def size(self):
        if type(self.__x) == int:
            return self.__x
        if type(self.__x) == list or type(self.__x) == str or type(self.__x) == dict:
            return len(self.__x)
