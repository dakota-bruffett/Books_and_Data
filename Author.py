class Author:
    def __init__(self, name): # heres how to tell the books for the self , name
        self.name = name
        self.book = []

    def publish(self, title):# this is the code that would publsih the code
        self.book.append(title)

    def __str__(self): # this would turn the code into strings for the assinment
         tittles = ','.join(self.book) or "no books Published"
         return f'{self.name}.Books: {tittles}'


def main(): # this main code adds on to a collection of code printing code like Auther and publiuhed book
    rowling = Author('J.K.Rowling')
    rowling.publish('harry potter and the philsopher stone')
    rowling.publish('Fanstic beasts and where to find them')
    print(rowling)

    clara = Author
    print(clara)
main()