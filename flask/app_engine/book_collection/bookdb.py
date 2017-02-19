from book import Book
import sqlite3
import os


class BookCollection:
    """An abstraction that provides the interface of a book collection"""
    def __init__(self):
        return

    def __len__(self):
        return 0

    def __contains__(self, item):
        return False

    def add_book(self, book):
        """Adds a book to the collection"""
        return

    def get_all_books(self):
        """Returns an sequence of all the books in the collection"""
        return []

    def get_books_by_author(self, author):
        """Returns a sequence of all books with a matching author"""
        return []

    def get_books_by_title(self, title):
        """Returns a sequence of all books with a matching title"""
        return []


class InMemoryBookCollection(BookCollection):
    """An implementation of BookCollection that keeps the books in local memory

    All the operations are slow. There's no facility for storing data between runs.
    """
    def __init__(self):
        BookCollection.__init__(self)
        self.books = []

    def __contains__(self, item):
        return item in self.books

    def __len__(self):
        return len(self.books)

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return True
        return False

    def get_all_books(self):
        return self.books

    def get_books_by_author(self, author):
        matches = []
        if author is not None and author != "":
            author = author.lower()
            for book in self.books:
                if author in book.author.lower():
                    matches.append(book)
        return matches

    def get_books_by_title(self, title):
        matches = []
        if title is not None and title != "":
            title = title.lower()
            for book in self.books:
                if title in book.title.lower():
                    matches.append(book)
        return matches


class SQLiteBookCollection(BookCollection):
    """An implementation of BookCollection that uses an SQLite database."""

    def __init__(self, dir_name, db_name):
        # Create a BookCollection with the backing database named. If the database
        # doesn't exist, start a new empty one to back this collection.
        BookCollection.__init__(self)
        if dir_name:
            temp_db = os.path.join(dir_name, db_name)
        else:
            temp_db = db_name
        self.connection = sqlite3.connect(temp_db, timeout=100)
        cursor = self.connection.cursor()
        cursor.execute("""create table if not exists Books
            (title text not null,
            author text not null);""")

    def __len__(self):
        cursor = self.connection.execute("select count(*) from Books;")
        return cursor.fetchone()[0]

    def __contains__(self, item):
        cursor = self.connection.execute(
            """select count(*) from Books where title="%s" and author="%s";""" %
            (item.title, item.author))
        return cursor.fetchone()[0] > 0

    def add_book(self, book):
        if book not in self:
            self.connection.cursor().execute(
                """insert into Books (title, author) values("%s", "%s");""" %
                (book.title, book.author))

    def get_all_books(self):
        cursor = self.connection.execute("select * from Books;")
        for row in cursor:
            yield Book(row[0], row[1])

    def get_books_by_author(self, author):
        cursor = self.connection.execute("""select * from Books where author="%s";""" % author)
        for row in cursor:
            yield Book(row[0], row[1])

    def get_books_by_title(self, title):
        cursor = self.connection.execute("""select * from Books where title="%s";""" % title)
        for row in cursor:
            yield Book(row[0], row[1])
