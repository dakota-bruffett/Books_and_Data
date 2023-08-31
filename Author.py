class Author:
    def __init__(self, name):
        self.name = name
        self.book = []

    def publish(self, title):
        self.book.append(title)

    def __str__(self):
         tittles = ','.join(self.book) or "no books Published"
         return f'{self.name}.Books: {tittles}'


def main():
    rowling = Author('J.K.Rowling')
    rowling.publish('harry potter and the philsopher stone')
    rowling.publish('Fanstic beasts and where to find them')
    print(rowling)

    clara = Author
    print(clara)
main()