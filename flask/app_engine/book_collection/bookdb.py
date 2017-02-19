from book import Book

class BookCollection:
    """An abstraction that provides the interface of a book collection"""
    def __init__(self):
        return

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
