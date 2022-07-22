# 1 Sum values
# For the first code challenge, we are going to look at only the values in a dictionary.
# This function should sum up all the values from the key-value pairs in the dictionary. Here are the steps we need:


def sum_values(my_dictionary):
    total = 0
    for key in my_dictionary:
        total += my_dictionary.get(key,0)
    return total


print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))


# 2 Even Keys

# Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values.
# Additionally, we are going to only look at every even key within the dictionary.


def sum_even_keys(my_dictionary):
    total = 0
    for value in my_dictionary.keys():
        if not value%2:
            total += my_dictionary.get(value)
    return total

print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))


# 3 Add Ten
# Let’s loop through the keys again, but this time let’s modify the values within the dictionary.
# Our function should add 10 to every value in the dictionary and return the modified dictionary.
# Here is what we need to do:

def add_ten(my_dictionary):
    for k in my_dictionary:
        my_dictionary[k] += 10
    return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))


# 4 Values That Are Keys
# We are making a program that will create a family tree. Using a dictionary, we want to return a list of all
# the children who are also parents of other children. Using dictionaries we can consider those people to be
# values which are also keys in our dictionary of family data. Here is what we need to do:


def values_that_are_keys(my_dictionary):
    temp = []

    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            temp.append(value)

    return temp


print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))



# 5 Largest Value

# For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary
# and return the associated key. This is a twist on the max algorithm since it is using a dictionary rather than a list
# .

def max_key(my_dictionary):
    key = None
    largest_value = None

    for k,v in my_dictionary.items():
        if largest_value is None:
            key = k
            largest_value = v

        if v > largest_value:
            key = k
            largest_value = v

    return key


print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))