
pos = 0
array = [3,1,5,2,8,6]

def SelectionSort():
    # global arr
    global pos
    # while(True):
    #     test_array = array[:]
    #     test_array.sort()
    #     if (test_array == array):
    #         break
    # smallest_index = findSmallest(array[pos:]) + pos
    #
    # smallest = array[smallest_index]
    #
    # array.pop(smallest_index)
    #
    # array.insert(pos, smallest)
    while (True):
        test_array = array[:]
        test_array.sort()
        if (test_array == array):
            break

        smallest_index = findSmallest(array[pos:]) + pos

        smallest = array[smallest_index]

        array.pop(smallest_index)

        array.insert(pos, smallest)

        pos += 1
        print(array)


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# while(True):
#     test_array = array[:]
#     test_array.sort()
#     if (test_array == array):
#         break
#     SelectionSort()
#     pos += 1
#     print(array)

SelectionSort()