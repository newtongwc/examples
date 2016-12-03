from flask import Flask
app = Flask("Echo Web")


@app.route("/<message>")
def echo_message(message):
    return "You said: %s" % message


@app.route("/")
def index():
    return "I can echo things. Try adding any message to your " \
           "url, e.g. '/howdy' or '/maria'"


app.run()
