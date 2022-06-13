
class human():
    def details(self):
        print("we are human")

class parent1(human):

    def details(self):
        print("i am female parent")

class parent2(human):
    def details(self):
        print("i am male parent ")

class child(parent1,parent2):

    def details(self):
        print("i am a child")
        print( "i amd 1 yr old")
        print("my parents are ")
        parent2.details(self)
        parent1.details(self)
        human.details(self)


c=child()
c.details()

