"""Example code for how to talk to the SQLite database from python.

In this example, we do something trivial, just to show that the
connection worked. In this case, the trivial thing is asking SQLite
what version of the software it is.

You might think that SQLite would be able to tell you this version
information without having an actual database that it is connecting
to, and that may be true. But here we create an empty database (with no
defined schema) just so that we can connect to it and ask it for the version.
"""

import sqlite3
import tempfile
import os

# Create a new database (in the form of a single file "temp.db") and put it
# somewhere out of the way. The act of connecting to a non-existent file
# causes SQLite to create the file, and initialize it as an empty database.
# If the file happened to exist, then connect() would open a real connection
# from this python program to that database.
temp_dir = tempfile.gettempdir()
temp_db = os.path.join(temp_dir, 'temp.db')
connection = sqlite3.connect(temp_db)

# A cursor in a database is similar to a cursor controlled by a mouse. It
# let's you point to a particular part of the database, select things from a
# certain point, insert things, etc. An interesting difference is that
# with a database cursor you can select things that you can describe, but
# don't necessarily know in advance what will come back that matches that
# description.
cursor = connection.cursor()
# This makes a list of records and positions the cursor at the start of
# the list.
cursor.execute("SELECT SQLITE_VERSION()")
# Grab the first item from the list and print it.
data = cursor.fetchone()
print "SQLite version: %s" % data

# All done; let's clean up after ourselves.
connection.close()
