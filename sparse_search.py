# implementation of a modified version of iterative binary search to search through a sparsely sorted dataset.

# ["Arthur", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"]


def sparse_search(data,search_val):
    print(f'Data: {data}')
    print(f'Data & Index: {list(enumerate(data))}')
    print(f'Search Value: {search_val}')

    # set up the index
    first = 0
    last = len(data) - 1

    while first <= last:
        # set up the mid values
        mid = (first + last) // 2

        # deal with possible empty sapces
        if data[mid] == "":
            left = mid - 1
            right = mid + 1

            while True:
                if left < first and right > last:
                    print(f'{search_val} is not in the dataset')
                    return

                elif right <= last and data[right] != "":
                    mid = right
                    break
                elif left >= first and data[left] != "":
                    mid = left
                    break

                left -= 1
                right += 1

        # test case
        if search_val == data[mid]:
            print(f'{search_val} found at position {mid}')
            return

        # splitting the list
        if search_val > data[mid]:
            first = mid + 1
        if search_val < data[mid]:
            last = mid - 1

    print(f'{search_val} is not in the list')


test_1 = ["A", "", "", "", "B", "", "", "", "C", "", "", "D"]
test_1_value = 'C'

test_2 = ["A", "B", "", "", "E"]
test_2_value = 'A'

test_3 = ["", "X", "", "Y", "Z"]
test_3_value = 'Z'

test_4 = ["A", "", "", "", "B", "", "", "", "C"]
test_4_value = 'D'

test_5 =["Apple", "", "Banana", "", "", "", "", "Cow"]
test_5_value = 'Banana'

test_6 = ["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "",
           "", "", "Zachary"]
test_6_value = 'Parth'

sparse_search(test_1, test_1_value)
sparse_search(test_2,test_2_value)
sparse_search(test_3,test_3_value)
sparse_search(test_4,test_4_value)
sparse_search(test_5,test_5_value)
sparse_search(test_6,test_6_value)


