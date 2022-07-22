# 1 Word Length Dict

# Let’s start by writing a function that creates a new dictionary based on a list of strings.
# The keys of our dictionary will be every string in our list of strings, while the values will be the length of each
# of the words in the string list.


def word_length_dictionary(words):
    return {word : len(word) for word in words}


print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))


# 2 Frequency Count

# This next function is similar, but instead of counting the length of each string in the list of strings,
# we will be counting the frequency of each string. This function will also accept a list of strings
# as input and return a new dictionary. Here is what we need to do:


def frequency_dictionary(words):
    return {word : words.count(word) for word in words}


# 3 Unique Values

# Now let’s try reading a dictionary as input and finding how many values are unique.
# The function should return a number which is the count of all values from the dictionary without including duplicates.
# These are the steps:


def unique_values(my_dictionary):
    unique = []

    for value in my_dictionary.values():
        if value not in unique:
            unique.append(value)

    return len(unique)


print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))


# 4 - Count First Letter

# This function accepts a dictionary where the keys are last names and the values are lists of first names of people
# who have that last name. We need to calculate the number of people who have the same first letter in their last name.
# Here are the steps we need:


def count_first_letter(names):
    letters = {}
    for key in names:
        first_char = key[0]
        if first_char not in letters:
            letters[first_char] = 0
        letters[first_char] += len(names[key])
    return letters



print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))