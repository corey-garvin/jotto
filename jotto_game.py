

class JottoGame(object):
    """Represents the non-biased middleman in a game of Jotto"""
    def __init__(self, word_length=4):
        super(JottoGame, self).__init__()

        self.word_length = word_length
        self.turn_limit = None

        # Read in our words list, keep only n-unique-letter words
        with open("words.txt") as input_file:
            self.word_list = [
                w for w in input_file.read().splitlines()
                if len(w) == self.word_length and
                len(set(w)) == self.word_length]

    @staticmethod
    def compare_words(word1, word2):
        """Returns number of common characters between 2 words"""
        return len(set(word1).intersection(set(word2)))

    def start(self, p1, p2):
        """Starts the game with players p1 & p2"""

        # Players are given their word list & select their secret words
        p1_secret = p1.select_a_secret_word(self.word_list[:])
        p2_secret = p2.select_a_secret_word(self.word_list[:])
        print("{} selected {}".format(p1.name, p1_secret))
        print("{} selected {}".format(p1.name, p2_secret))

        # Define some aliases.  "guesser" is the player whose turn it is
        guesser = p1
        sleeper = p2
        guesser_secret = p1_secret
        sleeper_secret = p2_secret

        turn = 1

        # Start the game loop
        while True:
            # Player guesses a word
            guess = guesser.guess_a_word()
            score = JottoGame.compare_words(guess, sleeper_secret)
            print("{})\t{} guessed '{}' - {}".format(
                turn, guesser.name, guess, score))

            # Player won?
            if guess == sleeper_secret:
                print("{} WINS after {} turn(s)".format(guesser.name, turn))
                return guesser
            else:
                # Inform the player of the match value
                guesser.store_word_result(guess, score)

            # Swap roles
            guesser, sleeper = sleeper, guesser
            guesser_secret, sleeper_secret = sleeper_secret, guesser_secret

            # Track our turns
            turn += 1
            if self.turn_limit and turn > self.turn_limit:
                print("Turn limit exceeded.")
                return None
