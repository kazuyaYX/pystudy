import pymysql
import string
import random

conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='0002'
    )


def save_to_mysql(result):
    cur = conn.cursor()
    sql = 'INSERT INTO code VALUES(null,"'+result+'");'
    cur.execute(sql)
    conn.commit()
    cur.close()


def is_exist(result):
    cur = conn.cursor()
    sql = 'SELECT COUNT(1) FROM code WHERE code="'+result+'"'
    cur.execute(sql)
    flag = cur.fetchone() != (0,)
    cur.close()
    return flag


def get_random_code(num, length):
    random_map = list(string.ascii_uppercase)
    for i in range(0, 10):
        random_map.append(str(i))
    i = 0
    while i < num:
        result = ''
        for j in range(0, length):
            result += random.choice(random_map)
        if is_exist(result):
            continue
        save_to_mysql(result)
        i += 1


if __name__ == '__main__':
    num = 200
    length = 16
    get_random_code(num, length)
    conn.close()

