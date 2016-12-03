from flask import Flask
app = Flask("Static HTML", static_url_path='')

@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/hello")
def hello():
    return app.send_static_file('hello.html')


@app.route("/goodbye")
def goodbye():
    return app.send_static_file('goodbye.html')


app.run()
