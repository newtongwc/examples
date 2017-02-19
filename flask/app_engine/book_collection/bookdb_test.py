from book import Book
from bookdb import InMemoryBookCollection

import pytest


@pytest.fixture
def collection():
    return InMemoryBookCollection()


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


def test_get_all_books(collection):
    a = Book("TitleA", "AuthorA")
    b = Book("TitleB", "AuthorB")
    collection.add_book(a)
    collection.add_book(b)
    books = collection.get_all_books()
    assert len(books) == 2
    assert a in books
    assert b in books


def test_get_books_by_author(collection):
    a = Book("TitleA", "AuthorA")
    b = Book("TitleB", "AuthorB")
    collection.add_book(a)
    collection.add_book(b)
    matches = collection.get_books_by_author("AuthorA")
    assert len(matches) == 1
    assert a in matches
    matches = collection.get_books_by_author("AuthorC")
    assert len(matches) == 0


def test_get_books_by_title(collection):
    a = Book("TitleA", "AuthorA")
    b = Book("TitleB", "AuthorB")
    collection.add_book(a)
    collection.add_book(b)
    matches = collection.get_books_by_title("TitleB")
    assert len(matches) == 1
    assert b in matches
    matches = collection.get_books_by_author("TitleC")
    assert len(matches) == 0


pytest.main()
