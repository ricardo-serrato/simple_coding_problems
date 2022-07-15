"""
 MASTER YODA: Given a sentence, return a sentence with the words reversed
 master_yoda('I am home') --> 'home am I'
 master_yoda('We are ready') --> 'ready are We'
"""


def master_yoda(sentence):
    return " ".join(sentence.split()[::-1]).capitalize()


print(master_yoda("I am home"))
print(master_yoda("We are ready"))


def master_yoda(sentence):
    lst_of_words = sentence.split()
    # word = ''
    # for i in range(len(sentence)):
    #     if sentence[i] == ' ' or i+1 > len(sentence)-1:
    #         lst_of_words.append(word)
    #         word = ''
    #     else:
    #         word += sentence[i]
    #
    # print(lst_of_words)


    i = 0
    j = len(lst_of_words) - 1
    while i <= j:
        lst_of_words[i], lst_of_words[j] = lst_of_words[j], lst_of_words[i]
        i += 1
        j -= 1

    return " ".join(lst_of_words).capitalize()



print(master_yoda("I am home"))
print(master_yoda("We are ready"))