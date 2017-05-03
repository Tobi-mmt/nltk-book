# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 43 detect language
# -----------------
import nltk, re
from nltk import word_tokenize

languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']


def word_frequency(text):
    tokens = text
    if type(text) == type(str('')):
        tokens = word_tokenize(text)
    freq = nltk.FreqDist(w.lower() for w in tokens)
    return freq


def get_lang_list():
    language_list = {}
    for language in languages:
        reference_text = nltk.corpus.udhr.words(language + '-Latin1')
        language_words = word_frequency(reference_text).most_common()
        language_list[language] = [word[0] for word in language_words if re.findall(r'\w',  word[0])]
    return language_list


def which_lang(string):
    input_text = word_frequency(string).most_common()
    input_text_list = [word[0] for word in input_text if re.findall(r'\w',  word[0])]

    language_list = get_lang_list()
    result = {}
    for lang in languages:
        result[lang] = len(list(set(input_text_list) & set(language_list[lang])))
    return 'Your Text is written in "{}"'.format(max(result, key=result.get))

input_txt = {
    'german': 'Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können. Um ein triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um Vorteile daraus zu ziehen? Aber wer hat irgend ein Recht, einen Menschen zu tadeln, der die Entscheidung trifft, eine Freude zu genießen, die keine unangenehmen Folgen hat, oder einen, der Schmerz vermeidet, welcher keine daraus resultierende Freude nach sich zieht? Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können. Um ein triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um Vorteile daraus zu ziehen?',
    'english': 'A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me.'
}
print(which_lang(input_txt['english']))


