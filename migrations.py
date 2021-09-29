from core import DB


def first():
    print('first migration')
    
    db_conn = DB.get_connection()
    query = """
    CREATE TABLE IF NOT EXISTS users
    (
        id BIGINTEGER NOT NULL,
        name VARCHAR
        email VARCHAR
    )
    """
    db_conn.execute(query)


def second():
    print('second migration')
