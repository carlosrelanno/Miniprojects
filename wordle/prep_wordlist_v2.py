file = 'palabras_todas.txt'

with open(file, encoding='UTF-8') as fp:
    words = list()
    words.extend([word.strip() for word in fp.readlines()])

print('Total words:', len(words))

# Get 5-letter words
words_5 = list(filter(lambda x: len(x) == 5, words))
print('5-letter words:', len(words_5))

# Get 4 letter words for plurals
words_4 = list(filter(lambda x: len(x) == 4, words))
words_4 = list(filter(lambda x: x.endswith('a') or x.endswith('e') or x.endswith('i') or x.endswith('o') or x.endswith('u'), words_4))
# Only words that end with vowels
words_4 = list(map(lambda x: x + 's', words_4))

# Add 4-letter plurals to 5-letter words
words_5.extend(words_4)
print('5-letter words after 4-letter plurals', len(words_5))
#  wtf
words_5 = list(filter(lambda x: '(' not in x, words_5))

# Remove accent mark
def remove_accent_marks(word):
    word = word.replace('á', 'a')
    word = word.replace('é', 'e')
    word = word.replace('í', 'i')
    word = word.replace('ó', 'o')
    word = word.replace('ú', 'u')
    return word

words_5 = list(map(remove_accent_marks, words_5))

# Sort and remove duplicates
words_5 = sorted(words_5)
print(len(words_5))
words_5 = sorted(list(set(words_5)))
print(len(words_5))

# Save
with open('words_5_extended.txt', 'w', encoding='UTF-8') as out:
    [out.write(word + '\n') for word in words_5]