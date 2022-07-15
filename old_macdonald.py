"""
    OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    old_macdonald('macdonald') --> MacDonald
"""


def old_macdonald(name):
    if len(name) > 3:
        return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    else:
        return name[0].upper() + name[1:]


print(old_macdonald('macdonald'))


def old_macdonald(name):
    name_modified = ""
    for i in range(len(name)):
        if i == 0 or i == 3:
            
            name_modified += name[i].upper()
        else:
            name_modified += name[i]

    return name_modified


print(old_macdonald('macdonald'))



