# -*- coding: utf-8 -*-

from .reverse_stemmer import ReverseStemmer
from .generator import Generator

class Converter(object):
    GREEK_CHARACTERS = u"αβγδεζηθικλμνξοπρσςτυφχψω"

    def __init__(self, max_expansions, generate_greek_variants):
        self.greek_words = []
        self.reverse_stemmer = ReverseStemmer()
        self.generator = Generator(max_expansions)
        self.generate_greek_variants = generate_greek_variants


    def convert(self, input_token):

        if not self.is_greek_word(input_token):
            return None

        if self.generate_greek_variants:
            self.greek_words = self.reverse_stemmer.generate_greek_variants(input_token)
        else:
            self.greek_words.append(input_token)

        return self.generator.generate_greeklish_words(self.greek_words)


    def is_greek_word(self, input_token):
        print(self.GREEK_CHARACTERS)
        for char in input_token:
            print(char)
            if char not in self.GREEK_CHARACTERS:
                return False

        return True
