file = 'spanish.lst'

with open(file, encoding='UTF-8') as fp:
    words = list()
    words.extend([word.strip() for word in fp.readlines()])

print(len(words))

words_5 = list(filter(lambda x: len(x) == 5, words))
print(len(words_5))

with open('words_5.txt', 'w', encoding='UTF-8') as out:
    [out.write(word + '\n') for word in words_5]