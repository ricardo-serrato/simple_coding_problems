# Define sum_to_one() below...
# a function that takes an integer as an input and returns the sum of all numbers from the input down to 1

def sum_to_one(n):
    if n == 1:
        return n
    print("Recursing with input: {0}".format(n))

    return n + sum_to_one(n-1)


print(sum_to_one(7))


