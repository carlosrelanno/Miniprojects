import random, emoji

class Wordle:
    def __init__(self):
        # Load 5-letter word database
        file = 'words_5.txt'
        with open(file, encoding='UTF-8') as fp:
            words = list()
            words.extend([word.strip() for word in fp.readlines()])

        # Select a random word
        guess = words[random.randint(0, len(words))]

        # Try to guess the word
        print('W O R D L E')
        for attempt in range(6):
            print(f'Intento {attempt+1}/6')
            candidate = input()
            while not self.check(candidate, words):
                candidate = input()
            comparing = self.compare(guess, candidate)
            if comparing == emoji.emojize(':green_square:')*5:
                print('La acertaste!')
                exit()
            print(comparing)
        print(guess)


    def compare(self, guess, candidate):
        guess_l = list(guess)
        candidate_l = list(candidate)

        # Set emojis for colored squares
        white = emoji.emojize(':white_large_square:')
        green = emoji.emojize(':green_square:')
        yellow = emoji.emojize(':yellow_square:')

        color_out = ''
        for index in range(len(guess)):
            if guess_l[index] == candidate_l[index]:
                color_out += green
            elif candidate_l[index] not in guess:
                color_out += white
            elif guess_l[index] != candidate_l[index] and candidate_l[index] in guess:
                color_out += yellow
        return color_out

    def check(self, candidate, words):
        if len(candidate) != 5:
            print('La palabra debe tener 5 letras')
            return False
        if candidate not in words:
            print('La palabra no está en el diccionario')
            return False
        return True

game = Wordle()