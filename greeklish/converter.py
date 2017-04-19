# -*- coding: utf-8 -*-

import itertools

from .reverse_stemmer import ReverseStemmer
from .generator import Generator

class Converter(object):
    GREEK_CHARACTERS = u"αβγδεζηθικλμνξοπρσςτυφχψω"

    def __init__(self, max_expansions, generate_greek_variants):
        self.reverse_stemmer = ReverseStemmer()
        self.generator = Generator(max_expansions)
        self.generate_greek_variants = generate_greek_variants


    def convert(self, input_token):
        self.greek_words = []

        if not self.is_greek_word(input_token):
            return None

        if self.generate_greek_variants:
            self.greek_words = self.reverse_stemmer.generate_greek_variants(input_token)
        else:
            self.greek_words.append(input_token)

        return self.generator.generate_greeklish_words(self.greek_words)


    def convert_phrase(self, phrase):
        """
        Converts a phrase to greeklish and returns all possible combinations.
        e.g. If it is a phrase with 3 words and 1st word generates 2 greeklish tokens,
        2nd word 4 greeklish tokens and 3rd word 1 greeklish token,
        then 2 * 4 * 1 greeklish phrases will be generated.

        Using this with generate_greek_variants on will produce significantly larger lists of variations.

        :param phrase:      Phrase to be converted. Should contain only greek not-accented words,
                            and no punctuation.
        :return:            Greeklish phrases generated.
        """
        self.phrase_words = phrase.split(sep=' ')

        for word in self.phrase_words:
            if not self.is_greek_word(word):
                return None

        self.converted_phrase_words = []
        if self.generate_greek_variants:
            for word in self.phrase_words:
                converted_stemmed_words = []
                stemmed_words = self.reverse_stemmer.generate_greek_variants(word)

                for stemmed_word in stemmed_words:
                    converted_stemmed_words.extend(self.generator.generate_greeklish_words(stemmed_word))

                self.converted_phrase_words.append(converted_stemmed_words)

        else:
            for word in self.phrase_words:
                self.converted_phrase_words.append(self.generator.generate_greeklish_words(word))

        return [" ".join(tuple)
                for tuple in list(itertools.product(*self.converted_phrase_words))]



    def is_greek_word(self, input_token):
        for char in input_token:
            if char not in self.GREEK_CHARACTERS:
                return False

        return True
