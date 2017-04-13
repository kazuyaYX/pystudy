import re
from collections import Counter


def couter(path):
    with open(path, encoding='utf-8') as file:
        # article = file.read().replace('\"|.|,|:', '')
        txt = file.read()
        article = re.sub('\W', ' ', txt).lower()
        words = article.split(' ')
        results = Counter(words)
        return results


if __name__ == '__main__':
    path = 'article.txt'
    results = couter(path)
    print(results)