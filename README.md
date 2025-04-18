# python-oop

This project contains beginner-friendly Python programs that demonstrate Object-Oriented Programming (OOP) concepts like inheritance, encapsulation, and polymorphism. The repository includes two main activities: a Book/EBook class system and an Animal polymorphism challenge.

## Project Description
This repository showcases two Python programs designed to teach OOP principles:

### Book and EBook Classes (books.py):

Demonstrates inheritance and encapsulation.
Includes a Book parent class and an EBook child class.
Features methods to check out, return, and download books, with unique attributes for physical and digital books.


### Animal Polymorphism Challenge (animals.py):

Demonstrates polymorphism.
Includes an Animal parent class with Bird and Fish child classes.
Each class implements a move() method differently (e.g., flying for birds, swimming for fish).



### Files

`books.py`: Contains the Book and EBook classes, with methods for managing books (check out, return, download).
`animals.py`: Contains the Animal, Bird, and Fish classes, showcasing polymorphism with different move() implementations.
`README.md`: This file, providing an overview of the repository.

## Prerequisites

Python 3.x installed on your system.
No external libraries are required; both programs use only the Python standard library.

## How to Run

1. Clone the Repository:
```
git clone https://github.com/your-username/python_oop.git
cd python_oop
```

2. Run the Book Program:
`python books.py`

This will create a physical book and an eBook (both titled "Alice in Wonderland"), demonstrate checking out/returning the physical book, and show downloading/checking out the eBook.

3. Run the Animal Program:
`python animals.py`

This will create a bird ("Tweety"), a fish ("Nemo"), and a generic animal, then call their move() methods to show different behaviors.


## Expected Output
### For books.py
Running python books.py will produce:
Title: Alice in Wonderland, Author: Lewis Carroll, Pages: 200, Genre: Fantasy, Status: Available
Alice in Wonderland has been checked out.
Title: Alice in Wonderland, Author: Lewis Carroll, Pages: 200, Genre: Fantasy, Status: Checked out
Alice in Wonderland has been returned.
Title: Alice in Wonderland, Author: Lewis Carroll, Pages: 200, Genre: Fantasy, Status: Available, File Size: 5.2MB, Format: PDF
Downloading Alice in Wonderland (PDF, 5.2MB)...
Alice in Wonderland has been checked out.

### For animals.py
Running python animals.py will produce:
Tweety is flying 
Nemo is swimming 
Generic Animal is moving.

## Learning Objectives

Understand inheritance by seeing how EBook extends Book and Bird/Fish extend Animal.
Explore encapsulation with attributes like is_checked_out and methods to manage book status.
Learn polymorphism by observing how move() behaves differently for each animal class.

## Contributing
Feel free to fork this repository, add new OOP examples, or improve the existing code! Submit pull requests or open issues for suggestions or bug reports.

