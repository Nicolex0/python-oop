# Base Class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title # Title of the book
        self.author = author # Author of the book
        self.pages = pages # Number of pages in the book
        self.genre = genre # Genre of the book
        self.is_checked_out = False #Checks whether the book is borrowed. If false, the book is available.

    def get_details(self):
        status = "Available" if not self.is_checked_out else "Checked Out" # Checks if book is checked out and sets the status text
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}, Status: {status}" # status text