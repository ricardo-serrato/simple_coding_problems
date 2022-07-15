"""
 PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
 paper_doll('Hello') --> 'HHHeeellllllooo'
 paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(text):
    new_string = ''

    for char in text:
        new_string += char*3

    return new_string



print(paper_doll('Mississippi'))