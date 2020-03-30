class BigCat(BigThing):
    def __init__(self, weight):
        super(BigCat, self).__inhit__(name="mitzi", age=5)
        self.__weight=weight
    def size(self):
        if self.__weight>15:
            return "fat"
        elif self.__weight>20:
            return "very fat"
        else:
            return "ok"

