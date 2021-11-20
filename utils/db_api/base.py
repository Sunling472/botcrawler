from psycopg2.extensions import cursor, connection
from psycopg2 import connect


class Db:
    conn: connection = connect(
        database='test_parse',
        user='postgres',
        password='sa12323100',
        host='localhost',
        port='5432'
    )

    curs: cursor = conn.cursor()


class PostUrlId(Db):

    def add_post(self, url: str, post_id: int):
        self.curs.execute(
            'INSERT INTO posts_url_id (url, post_id)'
            'VALUES (%s, %s)',
            (url, post_id)
        )
        self.conn.commit()

    def get_last_id(self) -> int:
        self.curs.execute(
            'SELECT post_id FROM posts_url_id'
        )
        keys_tuples: list = self.curs.fetchall()
        if keys_tuples is not None:
            keys: tuple = keys_tuples[-1]
            for key in keys:
                return key
        else:
            print('В базе ещё нет записей')

    def get_last_url(self) -> str:
        self.curs.execute(
            'SELECT url FROM posts_url_id'
        )
        urls_list: list = self.curs.fetchall()
        if urls_list is not None:
            url_t: tuple = urls_list[-1]
            for url in url_t:
                return url
        else:
            print('В базе ещё нет записей')


class FullPosts(Db):
    def add_full_post(self, title: str, body: str, url: str, post_id: int):
        self.curs.execute(
            'INSERT INTO full_posts (title, body, url, post_id) '
            'VALUES (%s, %s, %s, %s)', (title, body, url, post_id)
        )
        self.conn.commit()

    def get_last_fpost_id(self) -> int:
        self.curs.execute(
            'SELECT post_id FROM full_posts'
        )
        last_fposts_id: list = self.curs.fetchall()
        if last_fposts_id is not None:
            last_fposts_id_t: tuple = last_fposts_id[-1]
            for last_fpost_id in last_fposts_id_t:
                return last_fpost_id
        else:
            print('В базе ещё нет записей')


class UserDb(Db):

    def add_user(self, user_id: int):
        self.curs.execute(
            'INSERT INTO users (user_id)'
            'VALUES (%s)', (user_id,)
        )
        self.conn.commit()

    def is_reg(self, user_id: int) -> bool:
        self.curs.execute(
            'SELECT user_id FROM users '
            'WHERE user_id = %s', (user_id,)
        )
        users: list = self.curs.fetchall()
        if user_id in users:
            return True
        else:
            return False

    def set_sub_status(self, status: bool, user_id: int):
        self.curs.execute(
            'UPDATE users SET is_sub=%s '
            'WHERE user_id=%s', (status, user_id)
        )
        self.conn.commit()

    def is_sub(self, user_id: int) -> bool:
        self.curs.execute(
            'SELECT is_sub FROM users '
            'WHERE user_id=%s', (user_id,)
        )
        sub_t: tuple = self.curs.fetchone()
        if sub_t is not None:
            for is_sub in sub_t:
                return is_sub
        else:
            print('Такого пользователя не существует.')

