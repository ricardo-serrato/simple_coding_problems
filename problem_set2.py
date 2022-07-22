

# 1
# Write a function called unique_english_letters that takes the string word as a parameter. The function should
# return the total number of unique letters in the string.Uppercase and lowercase letters should
# be counted as different letters.
# We’ve given you a list of every uppercase and lower case letter in the English alphabet.
# It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:


def unique_english_letters(word):
    unique_letters = []

    for char in word:
        if char in unique_letters:
            continue
        unique_letters.append(char)

    return len(unique_letters)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))

# 2 Count X

# Next, we are going to try something a bit different. This time we are going to count the number
# of occurrences of a certain letter within a string. Our function will accept a parameter for a string
# and another for the character which we are going to count. For example, providing the word "mississippi"
# and the character 's' would result in an answer of 4. These are the steps we need to take:


def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count
    # return word.count(x)


print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))


# count Multi X

# Now let’s change our function to compare against an entire string instead of a single character.
# This function should accept a string and a substring to compare against. The number of occurrences of
# the second parameter within the first parameter string are returned. What this means is that we are checking the
# number of occurrences of the shorter string (second parameter) within the longer string (first parameter).
# One way to accomplish this is using the split function. Here is how to do that:

def count_multi_char_x(word,x):
    lst = word.split(x)
    return len(lst) - 1


print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# 4 Substring Between

# Here is a challenging problem. We need a function that is able to extract a portion of a
# string between two characters. The function will take three parameters where the first parameter
# is the string we are going to extract the substring from, the second input is the starting character
# of our substring and the third character is the ending character of our substring. Here are the steps we can use:

def substring_between_letters(word,s,e):
    if s not in word or e not in  word:
        return word

    Start = word.index(s)
    End = word.index(e)

    return word[Start+1:End]


print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))


# 5 X Length:
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters.
# This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence,x):
    for word in sentence.split():
        if len(word) < x:
            return False
    return True

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))
