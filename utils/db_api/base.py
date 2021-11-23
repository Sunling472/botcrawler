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


class FullPosts(Db):
    def add_full_post(self, title: str, body: str, url: str, post_id: int):
        self.curs.execute(
            'INSERT INTO full_posts (title, body, url, post_id) '
            'VALUES (%s, %s, %s, %s)', (title, body, url, post_id)
        )
        self.conn.commit()

    def get_last_fpost_id(self) -> str | None:
        self.curs.execute(
            'SELECT post_id FROM full_posts'
        )
        last_fposts_id: list = self.curs.fetchall()
        if len(last_fposts_id) != 0:
            last_fposts_id_t: tuple = last_fposts_id[-1]
            for last_fpost_id in last_fposts_id_t:
                return last_fpost_id
        else:
            return None


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
        users: list = self.curs.fetchone()
        try:
            for user in users:
                if user_id == user:
                    return True
            else:
                return False
        except TypeError:

            return False

    def set_sub_status(self, status: bool, user_id: int):
        self.curs.execute(
            'UPDATE users SET is_sub=%s '
            'WHERE user_id=%s', (status, user_id)
        )
        self.conn.commit()

    def is_sub(self, user_id: int) -> bool | None:
        self.curs.execute(
            'SELECT is_sub FROM users '
            'WHERE user_id=%s', (user_id,)
        )
        sub_t: tuple = self.curs.fetchone()
        if sub_t is not None:
            for is_sub in sub_t:
                return is_sub
        else:
            return None

    def get_subs_id(self) -> list | None:
        subs_id: list = []
        self.curs.execute(
            'SELECT user_id FROM users WHERE is_sub = True'
        )
        result: list = self.curs.fetchall()
        if len(result) != 0:
            for r in result:
                for id in r:
                    subs_id.append(id)
            return subs_id
        else:
            return None
