from flask import Flask
app = Flask("Hello HTML")

@app.route("/")
def pretty_hello():
    header = '<html>' \
             '<body style="background-color:LightBlue;">' \
             '<font color="Gold" size="36">'
    content = 'Hello, world!'
    footer = '</font>' \
             '</body>' \
             '</html>'

    page = header + content + footer
    return page


app.run()
