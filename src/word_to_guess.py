from string import digits
import random


class WordToGuess:
    def __init__(self, *args, **kwargs):
        super(WordToGuess, self).__init__(*args, **kwargs)

    def pick_word(self):
        pick = random.choice(open(r'data\word_list.raw').readlines())
        result = pick[:-1]
        return result