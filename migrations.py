from core import DB


def migrate():
    print('migrate...')
    
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

