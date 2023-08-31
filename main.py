# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    College_Id:int
    gpa:float # here is the float  similar to int where it displays numbers with a decimal

def main(): # i used a my own examples right there to add a name and example
    Steve = Student('Steve',235609,3.7)
    Kate = Student('Kate',124578,2.6)

    print(Steve)
    print(Kate)


main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
