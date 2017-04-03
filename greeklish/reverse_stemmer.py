# -*- coding: utf-8 -*-

import re

class ReverseStemmer(object):

    # Constant variable that represents suffixes for pluralization
    # of greeklish tokens.
    SUFFIX_MATOS = u"ματος"
    SUFFIX_MATA = u"ματα"
    SUFFIX_MATWN = u"ματων"
    SUFFIX_AS = u"ασ"
    SUFFIX_EIA = u"εια"
    SUFFIX_EIO = u"ειο"
    SUFFIX_EIOY = u"ειου"
    SUFFIX_EIWN = u"ειων"
    SUFFIX_IOY = u"ιου"
    SUFFIX_IA = u"ια"
    SUFFIX_IWN = u"ιων"
    SUFFIX_OS = u"ος"
    SUFFIX_OI = u"οι"
    SUFFIX_EIS = u"εις"
    SUFFIX_ES = u"ες"
    SUFFIX_HS = u"ης"
    SUFFIX_WN = u"ων"
    SUFFIX_OY = u"ου"
    SUFFIX_O = u"ο"
    SUFFIX_H = u"η"
    SUFFIX_A = u"α"
    SUFFIX_I = u"ι"

    # The possible suffix strings.
    SUFFIX_STRINGS = [
        [SUFFIX_MATOS, u"μα", u"ματων", u"ματα"],
        [SUFFIX_MATA, u"μα", u"ματων", u"ματος"],
        [SUFFIX_MATWN, u"μα", u"ματα", u"ματος"],
        [SUFFIX_AS, u"α", u"ων", u"ες"],
        [SUFFIX_EIA, u"ειο", u"ειων", u"ειου", u"ειας"],
        [SUFFIX_EIO, u"εια", u"ειων", u"ειου"],
        [SUFFIX_EIOY, u"εια", u"ειου", u"ειο", u"ειων"],
        [SUFFIX_EIWN, u"εια", u"ειου", u"ειο", u"ειας"],
        [SUFFIX_IOY, u"ι", u"ια", u"ιων", u"ιο"],
        [SUFFIX_IA, u"ιου", u"ι", u"ιων", u"ιας", u"ιο"],
        [SUFFIX_IWN, u"ιου", u"ια", "ι", "ιο"],
        [SUFFIX_OS, u"η", u"ους", u"ου", u"οι", u"ων"],
        [SUFFIX_OI, u"ος", u"ου", u"ων"],
        [SUFFIX_EIS, u"η", u"ης", u"εων"],
        [SUFFIX_ES, u"η", u"ας", u"ων", u"ης", u"α"],
        [SUFFIX_HS, u"ων", u"ες", u"η", u"εων"],
        [SUFFIX_WN, u"ος", u"ες", u"α", u"η", u"ης", u"ου", u"οι", u"ο", u"α"],
        [SUFFIX_OY, u"ων", u"α", u"ο", u"ος"],
        [SUFFIX_O, u"α", u"ου", u"εων", u"ων"],
        [SUFFIX_H, u"ος", u"ους", u"εων", u"εις", u"ης", u"ων"],
        [SUFFIX_A, u"ο", u"ου", u"ων", u"ας", u"ες"],
        [SUFFIX_I, u"ιου", u"ια", u"ιων"]
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
                break

        return self.greek_words

    def generate_more_greek_words(self, token_string, suffix_key):
        regex = re.compile(r'{0}$'.format(suffix_key))
        for suffix in self.suffixes[suffix_key]:
            self.greek_words.append(regex.sub(suffix, token_string))