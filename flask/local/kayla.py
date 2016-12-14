from flask import Flask
import random
app = Flask("Extended HTML")

@app.route("/")
def extended_html():
    start_html = """
    <html>
    <body>

    <p>
"""
    choice = random.choice(["rock","scissors"])
    choice_html = None
    if choice == "rock":
        choice_html = """
    This is a rock:
    <img width="100" src="http://vectortoons.com/wp-content/uploads/2015/05/rock-emoji-collection-001.jpg">
"""
    else:
        choice_html = """
<p>
    This is scissors;
    <img width="100" src="http://thumb1.shutterstock.com/display_pic_with_logo/708322/708322,1298155513,18/stock-photo-scissors-cartoon-71556766.jpg">
   """

    end_html = """</body>
    </html>
"""
    return start_html + choice_html + end_html


app.run()
