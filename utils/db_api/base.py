from psycopg2.extensions import cursor, connection
from psycopg2 import connect


class PostDb:
    conn: connection = connect(
        database='test_parse',
        user='postgres',
        password='sa12323100',
        host='localhost',
        port='5432'
    )

    curs: cursor = conn.cursor()

    def add_post(self, url: str, post_id: int):
        self.curs.execute(
            'INSERT INTO posts (url, post_id)'
            'VALUES (%s, %s)',
            (url, post_id)
        )
        self.conn.commit()

    def last_key(self) -> int:
        self.curs.execute(
            'SELECT post_id FROM posts'
        )
        keys_tuples: list = self.curs.fetchall()
        if keys_tuples is not None:
            keys: tuple = keys_tuples[-1]
            for key in keys:
                return key


