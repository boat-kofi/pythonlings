# Exercise: Classes 8

#
# Add a `__str__` method to the Book class so that
# `str(book)` returns the string "Book: <title> by <author>".
# Right now the class has no __str__, so str() returns the default repr.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


book = Book("1984", "Orwell")
