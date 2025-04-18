# Base Class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title # Title of the book
        self.author = author # Author of the book
        self.pages = pages # Number of pages in the book
        self.genre = genre # Genre of the book
        self.is_checked_out = False #Checks whether the book is borrowed. If false, the book is available.

    