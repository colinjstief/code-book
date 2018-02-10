"""
psycopg2 snippets
"""

from psycopg2_database import CursorFromConnectionFromPool
from psycopg2_database import Database


Database.initialize(
    host='localhost',
    database='learning',
    user='postgres',
    password='1234',
)

class User:
    """Creates a new user instance"""

    def __init__(self, email, first_name, last_name, identifier):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.identifier = identifier

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        """Save new user to database"""
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'INSERT INTO users (email, firs_name, last_name) VALUES (%s, %s, %s)',
                (self.email, self.first_name, self.last_name)
            )

    @classmethod
    def load_from_db_by_email(cls, email):
        """Load user using an email"""
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'SELECT * FROM users WHERE email=%',
                (email,)
            )
            user_data = cursor.fetchone()
            return cls(
                email=user_data[1],
                first_name=user_data[2],
                last_name=user_data[3],
                identifier=user_data[0]
            )

# Alternative
# CONNECTION = psycopg2.connect(
#     user='postgres',
#     password='1234',
#      database='learning',
#     host='localhost'
# )

# with CONNECTION.cursor() as cursor:
#     cursor.execute('INSERT INTO users (email, firs_name, last_name) VALUES (%s, %s, %s)',
#                   (self.email, self.first_name, self.last_name))
#     CONNECTION.commit()
#     CONNECTION.close()


# CONNECTION = CONNECTION_POOL.getconn()
# with CONNECTION.cursor() as cursor:
#     cursor.execute('...')
# CONNECTION_POOL.putconn(CONNECTION)


# def save_to_db(self):
#     """Save new user to database"""
#     with psycopg2.connect(
#         user='postgres',
#         password='1234',
#         database='learning',
#         host='localhost'
#     ) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 'INSERT INTO users (email, firs_name, last_name) VALUES (%s, %s, %s)',
#                 (self.email, self.first_name, self.last_name)
#             )
