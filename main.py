from src.game_phase import GamePhase
from src.letter_check import LetterCheck
from src.word_to_guess import WordToGuess


mistake_count = 0

phases = GamePhase().phase

check = LetterCheck().check_letter

# word_to_guess = WordToGuess().pick_word()
word_to_guess = "burna"

current_guess = ""
for letter in word_to_guess:
    current_guess += "-"

while current_guess != word_to_guess:
    print(phases(mistake_count))
    check(word_to_guess)
    






# print(phases.phase(0))
print(word_to_guess)
print(current_guess)

