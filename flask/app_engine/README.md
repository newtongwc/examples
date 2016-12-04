This directory contains simple web applications written using the
[Flask framework](http://flask.pocoo.org/docs/0.11/quickstart/).

They are suitable for running on Google AppEngine, either using AppEngine's
dev_appserver.py script or via deployment on Google Cloud Platform. These files closely
track the ones in ../local, with slight modification that make them able to run
in AppEngine.


Before running or deploying one of these applications, you must install the dependencies named
in its "requirements.txt" file using [pip](http://pip.readthedocs.io/en/stable/):
    pip install -t lib -r requirements.txt

Contents:

* hello_web.py: starts a server which says hello in response to a
  browser request to /. This is intended to illustrate the basic anatomy of a
  Flask application.

* extended_html.py: Returns a longer HTML marked-up text.

* static_html: Returns various HTML pages served as static files, rather than being
  hard-coded inside the Python file. Uses files in the static/ subdirectory.

