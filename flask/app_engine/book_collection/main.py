from flask import Flask
from flask import render_template
from flask import request

# The parameter static_url_path tells Flask where to look for the "static" directory.
# Requests for paths not explicitly listed with @app.route() directives below will be
# interpreted as requests for files from the "static" directory.
app = Flask(__name__, static_url_path='')

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
        return render_template("list_view.html", preamble_text=preamble, footer=footer_text())


@app.route("/browse")
def browse():
    preamble = "Here are all the books in the collection"
    return render_template("list_view.html", preamble_text=preamble, footer=footer_text())


@app.route("/add")
def add():
    return render_template("add_book.html", footer=footer_text())


if __name__ == "__main__":
    app.run()
