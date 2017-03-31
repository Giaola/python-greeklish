# -*- coding: utf-8 -*-

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