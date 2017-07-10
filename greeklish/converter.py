# -*- coding: utf-8 -*-

from .generator import Generator


class Converter(object):

    def __init__(self, max_expansions=4):
        self.generator = Generator(max_expansions)

    def convert(self, input_token):
        self.greek_words = input_token

        return self.generator.generate_greeklish_words(self.greek_words)
