from book import Book
from bookdb_memory import InMemoryBookCollection
from bookdb_sqlite import SQLiteBookCollection
from bookdb_datastore import DatastoreBookCollection

import pytest
import tempfile


@pytest.fixture(params=["in_memory", "sqlite"])
def collection(request):
    if request.param == "in_memory":
        return InMemoryBookCollection()
    elif request.param == "sqlite":
        return SQLiteBookCollection(tempfile.gettempdir(), "test.db", new=True)


def test_empty_collection(collection):
    assert len(collection) == 0


def test_add_book(collection):
    a = Book("TitleA", "AuthorA")
    collection.add_book(a)
    assert len(collection) == 1
    assert a in collection

    a_copy = Book("TitleA", "AuthorA")
    assert a_copy in collection

    b = Book("TitleB", "AuthorB")
    collection.add_book(b)
    assert len(collection) == 2
    assert b in collection
    assert a in collection

    collection.add_book(a_copy)
    assert len(collection) == 2  # Hasn't changed, book already present


def test_get_all_books(collection):
    a = Book("TitleA", "AuthorA")
    b = Book("TitleB", "AuthorB")
    collection.add_book(a)
    collection.add_book(b)
    books = collection.get_all_books()
    num_books = 0
    for book in books:
        num_books = num_books + 1
        assert book in [a, b]
    assert num_books == 2


def test_get_books_by_author(collection):
    a = Book("TitleA", "AuthorA")
    b = Book("TitleB", "AuthorB")
    collection.add_book(a)
    collection.add_book(b)
    matches = collection.get_books_by_author("AuthorA")
    num_matches = 0
    for book in matches:
        num_matches = num_matches + 1
        assert book in [a]
    assert num_matches == 1
    matches = collection.get_books_by_author("AuthorC")
    num_matches = 0
    for book in matches:
        num_matches = num_matches + 1
    assert num_matches == 0


def test_get_books_by_title(collection):
    a = Book("TitleA", "AuthorA")
    b = Book("TitleB", "AuthorB")
    collection.add_book(a)
    collection.add_book(b)
    matches = collection.get_books_by_title("TitleB")
    num_matches = 0
    for book in matches:
        num_matches = num_matches + 1
        assert book in [b]
    assert num_matches == 1
    matches = collection.get_books_by_title("TitleC")
    num_matches = 0
    for book in matches:
        num_matches = num_matches + 1
    assert num_matches == 0


pytest.main()
