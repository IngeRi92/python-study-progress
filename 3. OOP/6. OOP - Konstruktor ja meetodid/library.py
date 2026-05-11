"""Library."""


class Book:
    """Class representing a single book with title, author, and year."""

    def __init__(self, title, author, year):
        """
        Initialize a new Book instance.

        :param title: The title of the book.
        :param author: The author of the book.
        :param year: The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the book.

        :return: String like '"Title" by Author (Year)'.
        """
        return f'"{self.title}" by {self.author} ({self.year})'

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the book.

        :return: Representation like
                 Book(title='...', author='...', year=...).
        """
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __eq__(self, other) -> bool:
        """
        Compare two Book objects for equality.

        :param other: Another book to compare.
        :return: True if books have the same title and author, else False.
        """
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __hash__(self) -> int:
        """
        Compute a hash value for the book.

        :return: Hash based on the book's title and author.
        """
        return hash((self.title, self.author))

    def __lt__(self, other) -> bool:
        """
        Compare two Book objects by year for sorting.

        :param other: Another book to compare.
        :return: True if this book's year is less than the other's year.
        """
        if not isinstance(other, Book):
            return False
        return self.year < other.year

    def __len__(self) -> int:
        """
        Return the length of the book's title.

        :return: Number of characters in the book's title.
        """
        return len(self.title)


class Library:
    """Class representing a collection of books."""

    def __init__(self, name):
        """
        Initialize a new Library instance.

        :param name: The name of the library.
        """
        self.name = name
        self.books = []

    def __str__(self) -> str:
        """
        Return a string representation of the library.

        :return: String like 'Library "Name" has X books'.
        """
        return f'Library "{self.name}" has {len(self.books)} books'

    def __len__(self) -> int:
        """
        Return the number of books in the library.

        :return: Count of books.
        """
        return len(self.books)

    def __contains__(self, book) -> bool:
        """
        Check if a book is in the library.

        :param book: The book to check.
        :return: True if the book is in the library, else False.
        """
        return book in self.books

    def __getitem__(self, index) -> Book:
        """
        Retrieve a book by index.

        :param index: Position of the book.
        :return: Book object at the given index.
        """
        return self.books[index]

    def __add__(self, other) -> "Library":
        """
        Merge two libraries into a new library without duplicate books.

        The resulting library will contain all unique books from both libraries.
        Its name will follow the format: {lib1 + lib2}.

        :param other: Another library to merge with.
        :return: New library containing books from both.
        """
        new_library = Library(f"{{{self.name} + {other.name}}}")
        new_library.books = list(set(self.books) | set(other.books))
        return new_library

    def add_book(self, book):
        """
        Add a book to the library if it is not already present.

        :param book: The book to add.
        :type book: Book
        """
        if book not in self.books:
            self.books.append(book)

    def remove_book(self, book):
        """
        Remove a book from the library if it exists.

        :param book: The book to remove.
        """
        if book in self.books:
            self.books.remove(book)

    def find_books_by_author(self, author) -> list[Book]:
        """
        Find all books in the library by a given author.

        :param author: Author's name to search for.
        :return: List of books by the given author.
        """
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)
        return books_by_author


if __name__ == "__main__":
    # Näidisraamatud
    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("Animal Farm", "George Orwell", 1945)
    b3 = Book("Python Crash Course", "Eric Matthes", 2015)

    # Näidisraamatukogud
    lib1 = Library("Keskraamatukogu")
    lib2 = Library("Ülikooli raamatukogu")

    lib1.add_book(b1)
    lib1.add_book(b3)
    lib2.add_book(b2)

    print(b1)  # __str__
    print(repr(b1))  # __repr__
    print(len(b1))  # __len__
    print(sorted([b1, b2, b3]))  # __lt__

    print(lib1)  # __str__ of Library
    print(len(lib1))  # __len__ of Library
    print(b1 in lib1)  # __contains__

    print(lib1[0])  # __getitem__
    lib3 = lib1 + lib2  # __add__
    print(lib3)

    print(lib1.find_books_by_author("George Orwell"))
