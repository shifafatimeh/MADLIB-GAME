class Book:
    def __init__(self, book_id, title, author, total_pages):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1

    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.total_pages}")
        print(f"Current Page: {self.current_page}")
        print()

class Library:
    def __init__(self):
        self.books = {}
        self.active_book_id = None
        self.last_pages_read = {}

    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added to the library.")
            self.last_pages_read[book.book_id] = 1  # Initialize last page read to 1
            if self.active_book_id is None:
                self.set_active_book(book.book_id)
        else:
            print(f"Book with ID {book.book_id} already exists in the library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Book '{removed_book.title}' removed from the library.")
            if book_id == self.active_book_id:
                self.active_book_id = None
        else:
            print(f"Book with ID {book_id} not found in the library.")

    def display_books(self):
        print("Books in the Library:")
        for book_id, book in self.books.items():
            print(f"Book ID: {book_id}, Title: {book.title}")
        print()

    def set_active_book(self, book_id):
        if book_id in self.books:
            self.active_book_id = book_id
            print(f"Book '{self.books[book_id].title}' is now the active book.")
        else:
            print(f"Book with ID {book_id} not found in the library.")

    def get_active_book(self):
        if self.active_book_id is not None:
            return self.books[self.active_book_id]
        else:
            print("No active book selected.")
            return None

    def update_current_page(self, page_number):
        active_book = self.get_active_book()
        if active_book:
            active_book.current_page = page_number
            self.last_pages_read[self.active_book_id] = page_number
            print(f"Current page for '{active_book.title}' set to {page_number}.")

    def get_last_page_read(self):
        active_book_id = self.active_book_id
        if active_book_id is not None:
            return self.last_pages_read.get(active_book_id, 1)
        else:
            print("No active book selected.")
            return None


# Example Usage:
library = Library()

book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book(3, "1984", "George Orwell", 328)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.set_active_book(2)
library.get_active_book().display_info()

library.update_current_page(56)

last_page_read = library.get_last_page_read()
print(f"Last page read for the active book: {last_page_read}")

library.remove_book(1)

library.display_books()
