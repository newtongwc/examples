from flask import Flask
app = Flask("Hello Web")

@app.route("/")
def index():
    return "Hello Web!"


app.run()
