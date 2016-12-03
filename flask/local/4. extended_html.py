from flask import Flask
app = Flask("Extended HTML")

@app.route("/")
def extended_html():
    page_html = """
    <html>
    <body>
    This is a link to <a href="http://www.newtongwc.org">Newton GWC</a> website.
    <p>
    This is a list:
    <ul>
    <li>Item 1
    <li>Item 2
    <li>Item 3
    </ul>
    <p>
    This is a picture:<br>
    <img src="//m1.fluidreview.com/media/assets/reviewrooms/GirlsWhoCodeClubs/logo/gwc-clubs-logo-1221x234.jpg">
    </body>
    </html>
"""
    return page_html


app.run()
