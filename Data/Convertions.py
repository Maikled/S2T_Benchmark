import sys
import unicodedata


def convert_string(str):
    punctuation = "".join((chr(i) for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P')))
    remove_punctuation = "".join([str[i] for i in range(len(str)) if str[i] not in punctuation or (i > 1 and i < len(str) - 1 and str[i - 1] != " " and str[i] == "-" and str[i + 1] != " ")])
    return remove_punctuation.lower()
