# Base Class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title # Title of the book
        self.author = author # Author of the book
        self.pages = pages # Number of pages in the book
        self.genre = genre # Genre of the book
        self.is_checked_out = False #Checks whether the book is borrowed. If false, the book is available.

    # Show book details
    def get_details(self):
        status = "Available" if not self.is_checked_out else "Checked Out" # Checks if book is checked out and sets the status text
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}, Status: {status}" # status text
    
    # Check out book
    def check_out(self):
        if not self.is_checked_out: # Checks if the book is available
            self.is_checked_out = True # Sets the book to checked out
            return f"{self.title} has been checked out." # Returns a message indicating the book has been checked out
        else:
            return f"{self.title} is already checked out."
        
    # Return book
    def return_book(self):
        if self.is_checked_out: # Checks if the book is checked out
            self.is_checked_out = False # Sets the book to available
            return f"{self.title} has been returned." 
        else:
            return f"{self.title} is already available."