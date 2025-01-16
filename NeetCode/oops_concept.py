"""
This page conatins high level understanding of oops concept in python.
"""

org = "Globallogic India"
exp = 4

print(type(org))  # output : <class 'str'>
print(type(exp))  # output : <class 'int'>


# this is due to org variable belongs to str class ,
# similarly for exp varibale contains value for int class

# We can also create our owns CLASS and its properties
# we are defining school class
class Schools:
    place = 'Odisa'
    area = 2300
    students = 5000

    def get_all_students(self):
        return self.students


q1 = Schools()
# get the methods of class using objects
print(q1.get_all_students())

print(type(q1))
print(type(q1.get_all_students()))

# getting all the properties of class School
print(q1.place)
print(q1.area)

"""
Now we will be working with classes having argumets i.e , constructor.
Constructor: Its is called when ever class object is called for specific class.
"""


class Humans:

    def __init__(self):
        self.age = 30
        self.color = 'Brown'
        self.gender = 'male'

    def get_age(self):
        return self.age


q2 = Humans()
print(q2.age)
print(q2.gender)
print(q2.get_age())


class Mutants:

    def __init__(self, hands, eyes, color):
        self.eyes = eyes
        self.hand = hands
        self.color = color

    def get_mutants_hands_count(self):
        return f'The count of this mutant hand is: {self.hand}'


q3 = Mutants(67, 5, "Green")
print(q3.get_mutants_hands_count())
print(q3.eyes)
