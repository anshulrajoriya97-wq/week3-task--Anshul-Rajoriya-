# library.py
import json
from pathlib import Path

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title, "author": self.author,
            "isbn": self.isbn, "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"], data["available"])

class Library:
    def __init__(self, storage_file="books.json"):
        self.storage_file = Path(storage_file)
        self.books = self.load_books()

    def load_books(self):
        if self.storage_file.exists():
            with open(self.storage_file, "r") as f:
                data = json.load(f)
            return [Book.from_dict(b) for b in data]
        return []

    def save_books(self):
        with open(self.storage_file, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_books()

    def list_books(self):
        return self.books

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                self.save_books()
                return True
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                self.save_books()
                return True
        return False

if __name__ == "__main__":
    lib = Library()
    while True:
        print("\n1: List | 2: Add | 3: Borrow | 4: Return | 5: Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            for b in lib.list_books():
                status = "Available" if b.available else "Borrowed"
                print(f"{b.title} by {b.author} (ISBN: {b.isbn}) — {status}")
        elif choice == "2":
            t, a, i = input("Title: "), input("Author: "), input("ISBN: ")
            lib.add_book(t, a, i)
            print("Book added.")
        elif choice == "3":
            if lib.borrow_book(input("ISBN to borrow: ")):
                print("Borrowed.")
            else:
                print("Not available or not found.")
        elif choice == "4":
            if lib.return_book(input("ISBN to return: ")):
                print("Returned.")
            else:
                print("Return failed.")
        else:
            break
      
