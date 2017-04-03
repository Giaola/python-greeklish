# -*- coding: utf-8 -*-

class Generator(object):
    # α, ε, ι, η, υ, ο, ω
    ACCENTS = {
        u'ά': u'α',
        u'έ': u'ε',
        u'ή': u'η',
        u'ί': u'ι',
        u'υ': u'υ',
        u'ό': u'ο',
        u'ώ': u'ω'
    }

    # Constant variables that represent the character that substitutes
    # a digraph.
    AI = u"Α"
    EI = u"Ε"
    OI = u"Ο"
    OY = u"Υ"
    EY = u"Φ"
    AY = u"Β"
    MP = u"Μ"
    GG = u"Γ"
    GK = u"Κ"
    NT = u"Ν"

    # The possible digraph cases.
    DIGRAPH_CASES = [
        [u"αι", AI], [u"ει", EI], [u"οι", OI], [u"ου", OY],
        [u"ευ", EY], [u"αυ", AY], [u"μπ", MP], [u"γγ", GG],
        [u"γκ", GK], [u"ντ", NT]
    ]

    # The possible string conversions for each case.
    CONVERT_STRINGS = [
        [AI, u"ai", u"e"], [EI, u"ei", u"i"], [OI, u"oi", u"i"],
        [OY, u"ou", u"oy", u"u"], [EY, u"eu", u"ef", u"ev", u"ey"],
        [AY, u"au", u"af", u"av", u"ay"], [MP, u"mp", u"b"],
        [GG, u"gg", u"g"], [GK, u"gk", u"g"], [NT, u"nt", u"d"],
        [u"α", u"a"], [u"β", u"b", u"v"], [u"γ", u"g"], [u"δ", u"d"],
        [u"ε", u"e"], [u"ζ", u"z"], [u"η", u"h", u"i"], [u"θ", u"th"],
        [u"ι", u"i"], [u"κ", u"k"], [u"λ", u"l"], [u"μ", u"m"],
        [u"ν", u"n"], [u"ξ", u"ks", u"x"], [u"ο", u"o"], [u"π", u"p"],
        [u"ρ", u"r"], [u"σ", u"s"], [u"ς", u"s"], [u"τ", u"t"], [u"υ", u"y", u"u", u"i"],
        [u"φ", u"f", u"ph"], [u"χ", u"x", u"h", u"ch"], [u"ψ", u"ps"],
        [u"ω", u"w", u"o", u"v"]
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