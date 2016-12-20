from flask import Flask
app = Flask("Static HTML", static_url_path='')

if __name__ == "__main__":
    app.run()
