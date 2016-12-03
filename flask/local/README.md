This directory contains simple web applications written using the
[Flask framework](http://flask.pocoo.org/docs/0.11/quickstart/).

They are not suitable for running over the internet, and are only intended to run
on a local machine and under PyCharm. This constraint allows them to be super simple
and avoid noisy boiler-plate or complexity that obscures what's going on.

To run one, open it in PyCharm and hit the "Run" icon (the green triangle).

Contents:


* hello_web.py: starts a server on localhost:5000 which says hello in response to a
  browser request to http://localhost:5000. This is intended to illustrate the basic
  anatomy of a Flask application.

* greetings_web.py: starts a server on localhost:5000 and provides different greetings
  on http://localhost:5000/hello and http://localhost:5000/goodbye. This is intended to
  illustrate basic routing functionality with route().

* hello_html.py: Adds HTML markup to the returned text so the browser renders it nicely.

* extended_html.py: Returns a longer HTML marked-up text.

* static_html.py: Returns various HTML pages served as static files, rather than being
  hard-coded inside the Python file. Uses files in the static/ subdirectory.

* echo_web.py: Illustrates how to use Flask's variable rules in routing URLs to handlers
  that act differently depending on the URL.
