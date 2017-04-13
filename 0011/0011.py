def filter_word(word):
    words = open('.//filtered_words.txt', 'r').read().split()
    if word in words:
        print('Freedom !')
    else:
        print('Human Rights !')


word = input('请输入词语：')
filter_word(word)