# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    College_Id:int
    gpa:float

def main():
    Steve = Student('Steve',235609,3.7)
    Kate = Student('Kate',124578,2.6)

    print(Steve)
    print(Kate)


main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
