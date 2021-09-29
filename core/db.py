import sqlite3


class DB():
    __instance = None

    @classmethod
    def get_connection(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = DB(args, kwargs)

        return cls.__instance

        
    def __init__(self) -> None:
        self.connection = sqlite3.connect('Chinook_Sqlite.sqlite')
        self.cursor = self.connection.cursor()
        self.connection.close()


    def query(self, query_str): 
        """
        for example:
            db_instance = DB.get_connection()
            db_instance.query("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
        """

        self.cursor.execute(query_str)

        
    def close(self):
        self.connection.close()