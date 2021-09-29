import sqlite3


class DB():
    __instance = None

    @classmethod
    def get_connection(cls, db_name=None):
        if not cls.__instance:
            cls.__instance = DB(db_name)

        return cls.__instance

    @classmethod
    def has_instance(cls) -> bool:
        return bool(cls.__instance)

        
    def __init__(self, db_name) -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()


    def execute(self, query_str): 
        """
        for example:
            db_instance = DB.get_connection()
            db_instance.query("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
        """

        self.cursor.execute(query_str)

        
    def close(self):
        self.connection.close()