
class Student(Person):
    def __init__(self, name, age, avg):
        super(Student, self).__init__(name="liat", age=55)
        self.__avg = avg

    def get__avg(self):
        return self.__avg

    def set__avg(self, avg):
        self.__avg = avg
