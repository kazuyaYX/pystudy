import hashlib


if __name__ == '__main__':
    hash_object = hashlib.md5('刘琰翔'.encode())
    print(hash_object.hexdigest())