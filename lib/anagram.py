# your code goes here!
class Anagram :
    def __init__(self, word):
        self.word = word.lower()

    def match (self, word_list):
        original_word_sorted = sorted(self.word)
        return [w for w in word_list if sorted(w) == original_word_sorted and w.lower() != self.word]
