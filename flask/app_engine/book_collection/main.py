from flask import Flask
from flask import render_template
from flask import request

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return "{title: \"%s\", author: \"%s\"}" % (self.title, self.author)


class BookCollection:
    """An abstraction that provides the interface of a book collection"""

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
        for book in self.books:
            if author in book.author:
                return True
        return False


    def get_books_by_title(self, title):
        for book in self.books:
            if title in book.title:
                return True
        return False


# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask(__name__, static_url_path='')
collection = InMemoryBookCollection()
collection.add_book(Book("Title1", "Author1"))
collection.add_book(Book("Title2", "Author2"))


def footer_text():
    html = """
    """
    return html

# Tell Flask to point users to the home page if no path is given.
@app.route("/")
@app.route("/home")
def show_home_page():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("book_query.html", footer=footer_text())
    else:
        preamble = "Here are the books matching your search:"
        return render_template("list_view.html", preamble_text=preamble)


@app.route("/browse")
def browse():
    books = collection.get_all_books()
    for book in books:
        print book
    if len(books) > 0:
        author = books[0].author
        title = books[0].title
        preamble = "There are %d books in the collection." % len(collection)
    else:
        preamble = "The collection is empty."
        author = None
        title = None
    return render_template("list_view.html", preamble_text=preamble, title=title, author=author)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add_book.html")
    else:
        title = request.args.get("title", "")
        author = request.args.get("author", "")
        collection.add_book(Book(title, author))
        preamble = "You have successfully added a book to the collection. There are now %d books in it." % len(collection)
        return render_template("add_book.html", preamble_text=preamble)


if __name__ == "__main__":
    app.run()
