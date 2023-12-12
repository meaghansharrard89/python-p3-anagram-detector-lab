# your code goes here!
class Anagram:
    def __init__(self, word):
        self._word = word

    @property
    def word(self):
        """The word property"""
        return self._word

    @word.setter
    def word(self, word):
        self._word = word

    def match(self, options):
        """Return a list of words from the options"""
        list = []
        for word in options:
            if self.is_anagram(word):
                list.append(word)
        return list

    def is_anagram(self, option):
        """Check if option is an anagram of the initial word"""
        return sorted(self.word.lower()) == sorted(option.lower())
