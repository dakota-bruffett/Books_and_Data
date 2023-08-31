class Author:
    def __int__(self, name):
        self.name = name
        self.book = []

    def publish(self, title):
        self.book.append(title)

    def __str__(self):
         tittles = ','.join(self.books) or "no books Published"
         return f'{self.name}.Books: {tittles}'


    def main(self):
        rowling = Author('J.K.Rowling')
        rowling.publish('harry potter and the philsopher stone')
        rowling.publish('Fanstic beasts and where to find them')
        print(rowling)

        clara = Author
        print(clara)
