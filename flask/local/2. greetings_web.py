from flask import Flask
app = Flask("Greetings Web")

@app.route("/hello")
def hello():
    return "Hello Web!"


@app.route("/goodbye")
def goodbye():
    return "Goodbye Web!"


@app.route("/")
def root():
    return "Greetings! Try adding '/hello' or '/goodbye' to your URL"


app.run()
