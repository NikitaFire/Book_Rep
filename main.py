from dataclasses import dataclass
import unittest

@dataclass(frozen=True)
class Author:
    author_id: int
    name: str
    country: str

@dataclass(frozen=True)
class Publisher:
    publisher_id: int
    name: str
    address: str

@dataclass(frozen=True)
class Genre:
    genre_id: int
    name: str
    description: str

class Book:
    def __init__(self, isbn, title, publication_year, author, publisher, genres):
        self.isbn = isbn
        self.title = title
        self.publication_year = publication_year
        self.author = author
        self.publisher = publisher
        self.genres = genres

    def __eq__(self, other):
        return self.isbn == other.isbn

class Library:
    def __init__(self, library_id, name, address):
        self.library_id = library_id
        self.name = name
        self.address = address
        self.books = []

    def __eq__(self, other):
        return self.library_id == other.library_id

class Reader:
    def __init__(self, reader_id, name, address):
        self.reader_id = reader_id
        self.name = name
        self.address = address
        self.borrowed_books = []

    def __eq__(self, other):
        return self.reader_id == other.reader_id

# Добавленные бизнес-правила и тесты
def rule_1_check_books_limit(reader):
    return len(reader.borrowed_books) <= 5

def rule_2_check_book_availability(book, all_readers):
    return all(book not in reader.borrowed_books for reader in all_readers)

def rule_3_check_unique_book(book, library):
    return book not in library.books

def rule_4_check_user_name(reader):
    return bool(reader.name)

def rule_5_search_books_by_author(author, all_books):
    return [book for book in all_books if book.author == author]

def rule_6_return_book(reader, book):
    reader.borrowed_books.remove(book)

class TestLibraryFunctions(unittest.TestCase):
    def test_rule_1_check_books_limit(self):
        # Тестирование функции rule_1_check_books_limit
        reader = Reader(reader_id=1, name="John Doe", address="123 Main St")
        reader.borrowed_books = [Book(isbn="1234567890", title="Test Book", publication_year=2023, author=Author(1, "Test Author", "Test Country"), publisher=Publisher(1, "Test Publisher", "Test Address"), genres=[Genre(1, "Test Genre", "Test Description")])]
        self.assertTrue(rule_1_check_books_limit(reader))

    def test_rule_2_check_book_availability(self):
        # Тестирование функции rule_2_check_book_availability
        book = Book(isbn="0987654321", title="New Book", publication_year=2023, author=Author(2, "Another Author", "Another Country"), publisher=Publisher(2, "Another Publisher", "Another Address"), genres=[Genre(2, "Another Genre", "Another Description")])
        all_readers = [
            Reader(reader_id=1, name="John Doe", address="123 Main St", borrowed_books=[book]),
            Reader(reader_id=2, name="Jane Doe", address="456 Side St", borrowed_books=[]),
        ]
        self.assertFalse(rule_2_check_book_availability(book, all_readers))

    def test_rule_3_check_unique_book(self):
        # Тестирование функции rule_3_check_unique_book
        library = Library(library_id=1, name="Central Library", address="456 Library Ave")
        book = Book(isbn="0987654321", title="New Book", publication_year=2023, author=Author(2, "Another Author", "Another Country"), publisher=Publisher(2, "Another Publisher", "Another Address"), genres=[Genre(2, "Another Genre", "Another Description")])
        library.books = [book]
        self.assertFalse(rule_3_check_unique_book(book, library))

    def test_rule_4_check_user_name(self):
        # Тестирование функции rule_4_check_user_name
        reader = Reader(reader_id=1, name="John Doe", address="123 Main St")
        self.assertTrue(rule_4_check_user_name(reader))

    def test_rule_5_search_books_by_author(self):
        # Тестирование функции rule_5_search_books_by_author
        author = Author(author_id=1, name="Test Author", country="Test Country")
        all_books = [
            Book(isbn="1234567890", title="Test Book 1", publication_year=2023, author=author, publisher=Publisher(1, "Test Publisher", "Test Address"), genres=[Genre(1, "Test Genre", "Test Description")]),
            Book(isbn="0987654321", title="Test Book 2", publication_year=2023, author=author, publisher=Publisher(2, "Another Publisher", "Another Address"), genres=[Genre(2, "Another Genre", "Another Description")]),
        ]
        result = rule_5_search_books_by_author(author, all_books)
        self.assertEqual(len(result), 2)

    def test_rule_6_return_book(self):
        # Тестирование функции rule_6_return_book
        reader = Reader(reader_id=1, name="John Doe", address="123 Main St")
        book = Book(isbn="1234567890", title="Test Book", publication_year=2023, author=Author(1, "Test Author", "Test Country"), publisher=Publisher(1, "Test Publisher", "Test Address"), genres=[Genre(1, "Test Genre", "Test Description")])
        reader.borrowed_books = [book]
        rule_6_return_book(reader, book)
        self.assertEqual(len(reader.borrowed_books), 0)

if __name__ == '__main__':
    unittest.main()


