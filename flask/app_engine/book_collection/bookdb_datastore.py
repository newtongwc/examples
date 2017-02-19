import sys

sys.path.insert(1, '/Users/drm/Downloads/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/Users/drm/Downloads/google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, '/Users/drm/PycharmProjects/examples/flask/app_engine/book_collection/lib')


from google.appengine.ext import ndb
from book import Book
from bookdb import BookCollection

class DatastoreBook(ndb.Model):
    """A main model for representing a Book as a Datastore entity"""
    title = ndb.StringProperty()
    author = ndb.StringProperty()

class DatastoreBookCollection(BookCollection):
    """An implementation of BookCollection that uses Google's Datastore"""
    def __init__(self):
        BookCollection.__init__(self)
        return

    def __len__(self):
        book_query = DatastoreBook.query()
        return book_query.count(1000000)

    def __contains__(self, item):
        book_query = DatastoreBook.query(DatastoreBook.title == item.title,
                                         DatastoreBook.author == item.author)

    def add_book(self, book):
        """Adds a book to the collection"""
        datastore_book = DatastoreBook()
        datastore_book.title = book.title
        datastore_book.author = book.author
        datastore_book.put()
        return

    def get_all_books(self):
        """Returns an sequence of all the books in the collection"""
        query = DatastoreBook.query()
        for book in query:
            yield Book(book.title, book.author)

    def get_books_by_author(self, author):
        """Returns a sequence of all books with a matching author"""
        query = DatastoreBook.query(DatastoreBook.author == author)
        for book in query:
            yield Book(book.title, book.author)

    def get_books_by_title(self, title):
        """Returns a sequence of all books with a matching title"""
        query = DatastoreBook.query(DatastoreBook.title == title)
        for book in query:
            yield Book(book.title, book.author)
