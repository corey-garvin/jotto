import random


class JottoBot(object):
    """A bot for playing Jotto"""

    def __init__(self, name):
        """Bot receives a name and a copy of the word list"""
        self.name = name
        self.word_list = []
        super(JottoBot, self).__init__()

    def select_a_secret_word(self, word_list):
        """Select word at beginning of game"""
        self.word_list = word_list
        return random.SystemRandom().choice(self.word_list)

    def guess_a_word(self):
        """Invoked during the bot's turn."""
        # Choose a random word
        return random.SystemRandom().choice(self.word_list)

    def store_word_result(self, word, value):
        """Invoked when receiving a word result"""
        pass
