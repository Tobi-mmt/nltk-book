# -----------------
# 25 - find language
# -----------------
import nltk
from nltk.corpus import udhr
search_term = "right"


def find_language(search_word):
    languages = []
    for lang_id in udhr.fileids():
        if 'Latin1' in lang_id:
            for word in udhr.words(lang_id):
                if search_word.lower() == word.lower():
                    languages.append(lang_id.split("-")[0])
                    break
    languages = set(languages)
    if languages:
        print("The word '", search_term, "' is in the following ", len(languages), "languages:", languages)
    else:
        print("no results found")


find_language(search_term)
