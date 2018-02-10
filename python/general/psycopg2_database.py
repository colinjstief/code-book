"""
Create connection pool
"""

from psycopg2 import pool


class Database:
    """Create a new database class"""
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        """Create a new connection pool"""
        cls.__connection_pool = pool.SimpleConnectionPool(
            1,
            10,
            **kwargs
        )

    @classmethod
    def get_connection(cls):
        """Grab a new connection"""
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        """Put a connection back"""
        cls.__connection_pool.putconn(connection)

    @classmethod
    def close_connections(cls):
        """Close all connections"""
        cls.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    """Create a new connection pool"""

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
