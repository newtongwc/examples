from flask import Flask

app = Flask('Static HTML', static_url_path='')

app.run()
