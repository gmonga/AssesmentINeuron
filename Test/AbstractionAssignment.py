from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def name1(self):
        print("abc...")
        pass

    #noraml method
    def gender(self):
        print("gender is female")

class student_1(Student):
    def name1(self):
        print("i am student_1")
class student_2(Student):
    def name1(self):
        print("i am student_2")
class student_3(Student):
    def name1(self):
        print("i am student_3")

s=student_2()
s.name1()
s.gender()