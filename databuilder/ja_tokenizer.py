import spacy


class Tokenizer:
    def __init__(self):
        self.tokenizer = spacy.load('ja_ginza')

    def tokenize(self, sentence):
        return [token.text for token in self.tokenizer(sentence)]