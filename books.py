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
        
# Subclass 1
class Ebook(Book):
    def __init__(self, title, author, pages, genre, file_size_mb):
        super().__init__(title, author, pages, genre) # Calls the constructor of the base class
        self.file_size_mb = file_size_mb # File size of the ebook

    # Show ebook details by overriding parent's get_details method
    def get_details(self):
        details = super().get_details() # Calls the get_details method of the base class
        return f"{details}, File Size: {self.file_size_mb}MB" # Returns the details of the ebook with file size
    
    def download(self):
        return f"Downloading {self.title} ({self.file_size_mb}MB)" # Returns a message indicating the ebook is being downloaded
    
if __name__ == "__main__":
    novel = Book("Alice in Wonderland", "Lewis Carroll", 200, "Fantasy") # Creates an instance of the Book class
    print(novel.get_details()) # Prints the details of the book
    print(novel.check_out()) # Checks out the book
    print(novel.get_details()) # Prints the details of the book after checking out
    print(novel.return_book()) # Returns the book

    ebook = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 180, "Classic", 2) # Creates an instance of the Ebook class    
    print(ebook.get_details()) # Prints the details of the ebook
    print(ebook.download()) # Downloads the ebook
    print(ebook.check_out()) # Checks out the ebook
