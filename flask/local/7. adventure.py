from flask import Flask

app = Flask('Static HTML', static_url_path='')


#@app.route('/')
#def adventure():
#    return app.send_static_file('adventure.html')


app.run()
