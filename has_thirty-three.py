"""
 FIND 33:
 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

 has_33([1, 3, 3]) → True
 has_33([1, 3, 1, 3]) → False
 has_33([3, 1, 3]) → False
"""


def has_33(nums):
    string = "".join(map(str, nums))
    b = string.count('33')
    return b > 0


print(has_33([1, 3, 4, 5, 6, 3, 3, 3, 3, 3, 5, 6, 7, 2, 1, 3, 6, 8, 4, 1]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print('')


def has_33(nums):
    for i in range(len(nums)-1):

        if nums[i:i+2] == [3,3]:
            return True
    return False


print(has_33([1, 3, 4, 5, 6, 3, 3, 3, 3, 3, 5, 6, 7, 2, 1, 3, 6, 8, 4, 1]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print('')


def has_33(nums):
    for i in range(1,len(nums)):
        if nums[i-1] == 3 and nums[i] == 3:
            return True
    return False


print(has_33([1, 3, 4, 5, 6, 3, 3, 3, 3, 3, 5, 6, 7, 2, 1, 3, 6, 8, 4, 1]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))