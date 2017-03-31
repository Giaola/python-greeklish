# -*- coding: utf-8 -*-

import re

class Generator(object):
    # α, ε, ι, η, υ, ο, ω
    ACCENTS = {
        'ά': 'α',
        'έ': 'ε',
        'ή': 'η',
        'ί': 'ι',
        'υ': 'υ',
        'ό': 'ο',
        'ώ': 'ω'
    }

    # Constant variables that represent the character that substitutes
    # a digraph.
    AI = "Α"
    EI = "Ε"
    OI = "Ο"
    OY = "Υ"
    EY = "Φ"
    AY = "Β"
    MP = "Μ"
    GG = "Γ"
    GK = "Κ"
    NT = "Ν"

    # The possible digraph cases.
    DIGRAPH_CASES = [
        ["αι", AI], ["ει", EI], ["οι", OI], ["ου", OY],
        ["ευ", EY], ["αυ", AY], ["μπ", MP], ["γγ", GG],
        ["γκ", GK], ["ντ", NT]
    ]

    # The possible string conversions for each case.
    CONVERT_STRINGS = [
        [AI, "ai", "e"], [EI, "ei", "i"], [OI, "oi", "i"],
        [OY, "ou", "oy", "u"], [EY, "eu", "ef", "ev", "ey"],
        [AY, "au", "af", "av", "ay"], [MP, "mp", "b"],
        [GG, "gg", "g"], [GK, "gk", "g"], [NT, "nt", "d"],
        ["α", "a"], ["β", "b", "v"], ["γ", "g"], ["δ", "d"],
        ["ε", "e"], ["ζ", "z"], ["η", "h", "i"], ["θ", "th"],
        ["ι", "i"], ["κ", "k"], ["λ", "l"], ["μ", "m"],
        ["ν", "n"], ["ξ", "ks", "x"], ["ο", "o"], ["π", "p"],
        ["ρ", "r"], ["σ", "s"], ["ς", "s"], ["τ", "t"], ["υ", "y", "u", "i"],
        ["φ", "f", "ph"], ["χ", "x", "h", "ch"], ["ψ", "ps"],
        ["ω", "w", "o", "v"]
    ]

    def __init__(self, max_expansions):
        self.max_expansions = max_expansions
        self.greeklish_list = []
        self.per_word_greeklish = []
        self.digraphs = { }
        self.conversions = { }

        for case in self.DIGRAPH_CASES:
            self.digraphs[case[0]] = case[1]

        for string in self.CONVERT_STRINGS:
            self.conversions[string[0]] = string[1:]


    def remove_accent_chars(self, word):
        for accent_char in self.ACCENTS:
            word = word.replace(accent_char, self.ACCENTS[accent_char])
        return word

    def generate_greeklish_words(self, greek_words):
        self.greeklish_list = []

        if not isinstance(greek_words, list):
            greek_words = [greek_words]

        for greek_word in greek_words:
            self.per_word_greeklish = []

            greek_word = self.remove_accent_chars(greek_word)

            initial_token = greek_word

            for key in self.digraphs:
                greek_word = greek_word.replace(key, self.digraphs[key])

            for greek_char in greek_word:
                self.add_character(self.conversions[greek_char])

            for word in self.per_word_greeklish:
                self.greeklish_list.append(word)

        return self.greeklish_list

    def add_character(self, convert_strings):
        # list is empty
        if not self.per_word_greeklish:
            for string in convert_strings:

                if len(self.per_word_greeklish) >= self.max_expansions:
                    break

                self.per_word_greeklish.append(string)
        else:
            new_tokens = []

            for convert_string in convert_strings:
                for token in self.per_word_greeklish:
                    if len(new_tokens) >= self.max_expansions:
                        break
                    new_tokens.append(token+convert_string)

            self.per_word_greeklish = new_tokens


class ReverseStemmer(object):

    # Constant variable that represents suffixes for pluralization
    # of greeklish tokens.
    SUFFIX_MATOS = "ματος"
    SUFFIX_MATA = "ματα"
    SUFFIX_MATWN = "ματων"
    SUFFIX_AS = "ασ"
    SUFFIX_EIA = "εια"
    SUFFIX_EIO = "ειο"
    SUFFIX_EIOY = "ειου"
    SUFFIX_EIWN = "ειων"
    SUFFIX_IOY = "ιου"
    SUFFIX_IA = "ια"
    SUFFIX_IWN = "ιων"
    SUFFIX_OS = "ος"
    SUFFIX_OI = "οι"
    SUFFIX_EIS = "εις"
    SUFFIX_ES = "ες"
    SUFFIX_HS = "ης"
    SUFFIX_WN = "ων"
    SUFFIX_OY = "ου"
    SUFFIX_O = "ο"
    SUFFIX_H = "η"
    SUFFIX_A = "α"
    SUFFIX_I = "ι"

    # The possible suffix strings.
    SUFFIX_STRINGS = [
        [SUFFIX_MATOS, "μα", "ματων", "ματα"],
        [SUFFIX_MATA, "μα", "ματων", "ματος"],
        [SUFFIX_MATWN, "μα", "ματα", "ματος"],
        [SUFFIX_AS, "α", "ων", "ες"],
        [SUFFIX_EIA, "ειο", "ειων", "ειου", "ειας"],
        [SUFFIX_EIO, "εια", "ειων", "ειου"],
        [SUFFIX_EIOY, "εια", "ειου", "ειο", "ειων"],
        [SUFFIX_EIWN, "εια", "ειου", "ειο", "ειας"],
        [SUFFIX_IOY, "ι", "ια", "ιων", "ιο"],
        [SUFFIX_IA, "ιου", "ι", "ιων", "ιας", "ιο"],
        [SUFFIX_IWN, "ιου", "ια", "ι", "ιο"],
        [SUFFIX_OS, "η", "ους", "ου", "οι", "ων"],
        [SUFFIX_OI, "ος", "ου", "ων"],
        [SUFFIX_EIS, "η", "ης", "εων"],
        [SUFFIX_ES, "η", "ας", "ων", "ης", "α"],
        [SUFFIX_HS, "ων", "ες", "η", "εων"],
        [SUFFIX_WN, "οσ", "ες", "α", "η", "ης", "ου", "οι", "ο", "α"],
        [SUFFIX_OY, "ων", "α", "ο", "ος"],
        [SUFFIX_O, "α", "ου", "εων", "ων"],
        [SUFFIX_H, "ος", "ους", "εων", "εις", "ης", "ων"],
        [SUFFIX_A, "ο", "ου", "ων", "ασ", "ες"],
        [SUFFIX_I, "ιου", "ια", "ιων"]
    ]

    def __init__(self):
        self.suffixes = {}
        self.greek_words = []

        for suffix in self.SUFFIX_STRINGS:
            self.suffixes[suffix[0]] = suffix[1:]

    def generate_greek_variants(self, token_string):
        self.greek_words = [token_string]

        for key in self.suffixes.keys():
            if token_string.endswith(key):
                self.generate_more_greek_words(token_string, key)

        return self.greek_words

    def generate_more_greek_words(self, token_string, suffix_key):
        regex = re.compile(r'{0}$'.format(suffix_key))
        for suffix in self.suffixes[suffix_key]:
            self.greek_words.append(regex.sub(suffix, token_string))


class Converter(object):
    GREEK_CHARACTERS = "αβγδεζηθικλμνξοπρσςτυφχψω"

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
        for char in input_token:
            if char not in self.GREEK_CHARACTERS:
                return False

        return True
