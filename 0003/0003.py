import redis
import string
import random

rconn = redis.Redis(host='127.0.0.1', port=6379, db='0003')


def save_to_redis(result):
    rconn.sadd('0003', result)


def is_exist(result):
    return rconn.sismember('0003', result)


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
        save_to_redis(result)
        i += 1


if __name__ == '__main__':
    num = 200
    length = 16
    get_random_code(num, length)
    print(rconn.scard('0003'))