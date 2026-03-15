import sqlite3

def connect_db():
    # create or connect database
    conn = sqlite3.connect("billing.db")
    return conn

"""
What happens

If database doesn't exist:

billing.db

It will be created automatically.
"""