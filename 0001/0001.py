import string
import random


def get_random_code(num, length):
    random_map = list(string.ascii_uppercase)
    for i in range(0, 10):
        random_map.append(str(i))
    i = 0
    results = []
    while i < num:
        result = ''
        for j in range(0, length):
            result += random.choice(random_map)
        if result in results:
            continue
        results.append(result)
        i += 1
    return results


if __name__ == '__main__':
    num = 200
    length = 16
    results = get_random_code(num, length)
    print(results)