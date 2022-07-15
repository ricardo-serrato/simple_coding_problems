
"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def animal_crackers(text):
    first_letter = text.split()[0][0].lower()
    for word in text.split():
        if word[0].lower() != first_letter:
            return False
    return True


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def animal_crackers(text):
    words = text.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
