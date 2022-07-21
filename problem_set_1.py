# 1
#Let’s start our code challenges with a function that counts how many numbers
# are divisible by ten from a list of numbers. This function will accept a list of
# numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is
# divisible by 10, a counter will be incremented and the final count will be returned.


def divisible_by_ten(lst):

    counter = 0
    for number in lst:
        if number % 10 == 0:
            counter+=1

    return counter


print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2
# You are invited to a social gathering, but you are tired of greeting everyone there. Luckily
# we can create a function to accomplish this task for us. In this challenge, we will take a
# list of names and prepend the string 'Hello, ' before each name. This will require a few steps:


def add_greetings(lst_of_names):
    return [f"Hello, {name}" for name in lst_of_names]


print(add_greetings(["Owen", "Max", "Sophie"]))

# 3
# Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly
# remove the first element of a list until it finds an odd number or runs out of elements. It will accept
# a list of numbers as an input parameter and return the modified list where any even numbers at the beginning
# of the list are removed.


def delete_starting_evens(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            return lst[i:]

    return []

# 4
# This next function will give us the values from a list at every odd index. We will need to accept
# a list of numbers as an input parameter and loop through the odd indices instead of the elements.


def odd_indices(lst):
    return [lst[i] for i in range(1, len(lst), 2)]


print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5
# In this challenge, we will be using nested loops in order to raise a list of numbers to the power
# of a list of other numbers. What this means is that for every number in the first list, we will raise that number
# to the power of every number in the second list. If you provide the first list with 2 elements and
# the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:


def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base**power)
    return new_lst


print(exponents([2, 3, 4], [1, 2, 3]))

# 1
# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum.
# We will iterate through each of the list and calculate the sums, afterwards we will compare the two
# and return which one has a greater sum. Here are the steps we need:


def larger_sum(lst1,lst2):
    return lst1 if sum(lst1) >= sum(lst2) else lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2 over 9000

# We are constructing a device that is able to measure the power level of our coding abilities and according
# to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through
# a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000.
# Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this,
# we will need the following steps:


def over_nine_thousand(lst):
    sums = 0
    for num in lst:
        if sums > 9000:
            return sums
        sums += num
    return sums

# 3 Max Num
# Here is a more traditional coding problem for you. This function will be used to find the maximum number
# in a list of numbers. This can be accomplished using the max() function in python, but as a challenge,
# we are going to manually implement this function. Here is what we need to do:


def max_num(nums):
    max_number = nums[0]
    for num in nums:
        if num > max_number:
            max_number = num
    return max_number


# 4 Same Values
# In this challenge, we need to find the indices in two equally sized lists where the numbers match.
# We will be iterating through both of them at the same time and comparing the values, if the numbers are equal,
# then we record the index. These are the steps we need to accomplish this:

def same_values(lst1, lst2):

    common_indices = []

    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            common_indices.append(i)

    return common_indices


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 5
# For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list.
# There are a few different ways to approach this, but we are going to try a method that iterates through each of
# the values in one direction for the first list and compares them against the values starting from
# the other direction in the second list. Here is what you need to do:


def reversed_list(lst1, lst2):
    max_ = len(lst2)
    for i in range(len(lst1)):
        max_ -= 1
        if lst1[i] != lst2[max_]:
            return False
    return True


print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))