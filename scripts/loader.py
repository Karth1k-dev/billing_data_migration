from database.db_connection import connect_db

def load_to_database(data):

    conn = connect_db()
    cursor = conn.cursor()

    # create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        customer_id INTEGER,
        name TEXT,
        email TEXT,
        plan TEXT,
        price INTEGER
    )
    """)

    # insert each record
    for record in data:

        cursor.execute("""
        INSERT INTO customers VALUES (?,?,?,?,?)
        """,
        (
            record['customer_id'],
            record['name'],
            record['email'],
            record['plan'],
            record['price']
        ))

    conn.commit()
    conn.close()

"""
What this does

Creates table:

customers

Example record stored:

1 | John | john@email.com | Basic | 10
"""