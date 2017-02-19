from book import Book
from bookdb import BookCollection

import sqlite3
import os


class SQLiteBookCollection(BookCollection):
    """An implementation of BookCollection that uses an SQLite database."""

    def __init__(self, dir_name, db_name, new):
        # Create a BookCollection with the backing database named. If the database
        # doesn't exist, start a new empty one to back this collection.
        BookCollection.__init__(self)
        if dir_name:
            self.db = os.path.join(dir_name, db_name)
        else:
            self.db = db_name
        connection = sqlite3.connect(self.db)
        if new:
            connection.execute("drop table Books")
        connection.execute("""create table if not exists Books
            (title text not null,
            author text not null);""")
        connection.commit()
        # From here on out, use this connection only for reading; make new ones for writing.
        self.read_connection = connection

    def __len__(self):
        connection = self.read_connection
        cursor = connection.execute("select count(*) from Books;")
        length = cursor.fetchone()[0]
        return length

    def __contains__(self, item):
        connection = self.read_connection
        cursor = connection.execute(
            """select count(*) from Books where title="%s" and author="%s";""" %
            (item.title, item.author))
        count = cursor.fetchone()[0]
        return count > 0

    def add_book(self, book):
        if book not in self:
            connection = sqlite3.connect(self.db)
            connection.execute(
                """insert into Books (title, author) values("%s", "%s");""" %
                (book.title, book.author))
            connection.commit()
            connection.close()

    def get_all_books(self):
        connection = self.read_connection
        cursor = connection.execute("select * from Books;")
        for row in cursor:
            yield Book(row[0], row[1])

    def get_books_by_author(self, author):
        connection = self.read_connection
        cursor = connection.execute("""select * from Books where author="%s";""" % author)
        for row in cursor:
            yield Book(row[0], row[1])

    def get_books_by_title(self, title):
        connection = self.read_connection
        cursor = connection.execute("""select * from Books where title="%s";""" % title)
        for row in cursor:
            yield Book(row[0], row[1])
