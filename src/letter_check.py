import re


class LetterCheck:
    def __init__(self, *args, **kwargs):
        super(LetterCheck, self).__init__(*args, **kwargs)

    def check_if_valid(self, input_str, word_to_guess):
        if input_str != word_to_guess:
            if not re.match("^[a-z]*$", input_str):
                print("Error! Only letters a-z allowed!")
            elif len(input_str) > 1:
                print("Error! Only 1 character allowed!")
            else:
                result = input_str
        else:
            result = input_str
        return result

    def check_letter(self, guess ,word_to_guess):
        input_str = input("Enter a letter:")
        if input_str == word_to_guess:
            result = word_to_guess
            print("You win!")
        if input_str != word_to_guess:
            if input_str in word_to_guess:
                
        return result
