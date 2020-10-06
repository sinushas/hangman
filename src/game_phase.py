
class GamePhase:
    def __init__(self, *args, **kwargs):
        super(GamePhase, self).__init__(*args, **kwargs)

    def phase(self, mistake_count):
        current_mistakes = mistake_count
        picture = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
                   "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
                   "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
                   "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
                   "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
                   "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
                   "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
        return picture[current_mistakes]
