from psycopg2.extensions import cursor, connection
from psycopg2 import connect

conn: connection = connect(
    host='localhost', port=5432, database='test_parse', user='postgres', password='sa12323100'
)

curs: cursor = conn.cursor()


def list_base() -> list:
    curs.execute(
        'SELECT link_news FROM employee'
    )
    list_news: list = curs.fetchall()

    return list_news


def add_news(title: str, link_news: str, post_number: int):
    curs.execute(
        'INSERT INTO employee (title, link_news, post_number)'
        'VALUES (%s, %s, %s)',
        (title, link_news, post_number)
    )
    conn.commit()


def get_last_post_number() -> int:
    curs.execute(
        'SELECT post_number FROM employee'
    )
    post_number_list: list = curs.fetchall()
    post_number_tuple: tuple = post_number_list[-1]
    for post_number in post_number_tuple:
        return post_number








