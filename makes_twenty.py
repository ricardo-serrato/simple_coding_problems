"""
 MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not,
 return False
 makes_twenty(20,10) --> True
 makes_twenty(12,8) --> True
 makes_twenty(2,3) --> False
"""


def makes_twenty(num1,num2):
    if 20 in (num1, num2):
        return True
    else:
        return num1 + num2 == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


def makes_twenty(num1,num2):
    return (num1+num2) == 20 or num1 == 20 or num2 == 20

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))