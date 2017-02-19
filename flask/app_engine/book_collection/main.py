from flask import Flask
from flask import render_template
from flask import request
from book import Book
from bookdb import InMemoryBookCollection

# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask(__name__, static_url_path='')
collection = InMemoryBookCollection()
collection.add_book(Book("Title1", "Author1"))
collection.add_book(Book("Title2", "Author2"))


# Tell Flask to point users to the home page if no path is given.
@app.route("/")
@app.route("/home")
def show_home_page():
    return render_template("home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("book_query.html")
    else:
        preamble = "Here are the books matching your search:"
        title = request.form.get("title", "")
        author = request.form.get("author", "")
        author_matches = collection.get_books_by_author(author)
        title_matches = collection.get_books_by_title(title)
        if title == "":
            matches = author_matches
        elif author == "":
            matches = title_matches
        else:
            matches = list(set(author_matches) & set(title_matches))
        return render_template("list_view.html", preamble_text=preamble, books=matches)


@app.route("/browse")
def browse():
    books = collection.get_all_books()
    preamble = "There are %d books in the collection." % len(collection)
    return render_template("list_view.html", preamble_text=preamble, books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add_book.html")
    else:
        title = request.form.get("title", "")
        author = request.form.get("author", "")
        collection.add_book(Book(title, author))
        preamble = "You have successfully added a book to the collection. There are now %d books in it." % len(collection)
        return render_template("add_book.html", preamble_text=preamble)


if __name__ == "__main__":
    app.run()
