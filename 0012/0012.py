import re


def filter_word(sentence):
    words = open('.//filtered_words.txt', 'r').read().split()
    for word in words:
        if re.search(word,sentence) is not None:
            replaceword = ''
            for i in range(len(word)):
                replaceword += '*'
            sentence = sentence.replace(word, replaceword)
    print(sentence)


sentence = input('请输入语句：')
filter_word(sentence)