
# 1 Check Name:
# You are creating an app that allows users to interact and share their
# coding project ideas online. The first step is to provide your name in the application and a greeting for other
# people to see which contains your name. Let’s create a function that is able to check if a user’s name is located
# within their greeting. We need a function that accepts two parameters, a string for our sentence and a string
# for a name. The function should return True if the name exists within
# the string (ignoring any differences in capitalization). Here is what we need to do:


def check_for_name(sentence, name):
    return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))


# 2 - Every Other Letter

# For this next function, we are going to create a function that extract every other letter from a string and returns
# the resulting string. There are a few different ways you can solve this problem.

def every_other_letter(word):
    return word[::2]

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

# 3 - Reverse

# This one is similar to the last challenge. Instead of selecting every other letter,
# we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify
# the range we are using.


def reverse_string(word):
    return word[::-1]


# 4 - Make Spoonerism
# A Spoonerism is an error in speech when the first syllables of two words are switched.
# For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.
# We are going to make a function that is similar, but instead of using the first syllable,
# we are going to switch the first character of two words. Here is what we need to do:


def make_spoonerism(word1, word2):
    new_word_1 = word2[0] + word1[1:]
    new_word_2 = word1[0] + word2[1:]

    return f"{new_word_1} {new_word_2}"


print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))


# 5 Add exclamation
# Let’s say we are writing a program that displays a large message on a blimp
# and we need to fill in any missing space if a short phrase is provided.
# Our function will accept a string and if the size is less than 20, it will fill in the remaining space
# with exclamation marks until the size reaches 20. If the provided string already has a length greater than 20,
# then we will simply return the original string. Here are the steps:


def add_exclamation(word):
    if len(word) >= 20:
        return word

    x = 20 - len(word)

    return f"{word}{'!'*x}"


print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))