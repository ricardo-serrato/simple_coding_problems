"""
 ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
 almost_there(90) --> True
 almost_there(104) --> True
 almost_there(150) --> False
 almost_there(209) --> True
"""


def almost_there(number):

    if abs(100-number) <= 10 or abs(200-number) <= 10:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))