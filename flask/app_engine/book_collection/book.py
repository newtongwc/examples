class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{title: \"%s\", author: \"%s\"}" % (self.title, self.author)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __ne__(self, other):
        return self.title != other.title or self.author != other.author
