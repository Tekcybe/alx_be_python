class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} (E-Book, {self.file_size}KB)"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} (Print, {self.page_count} pages)"


class Library:
    def __init__(self):
        self.books = []  # Composition: Library has a list of books

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Only Book objects can be added to the library.")

    def list_books(self):
        print("\nLibrary Collection:")
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(book)
