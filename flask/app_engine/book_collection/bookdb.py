from book import Book


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
