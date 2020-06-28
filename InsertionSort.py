

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        while(j >= 0 and key < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

arr = [3,2,5,4,9,7]

insertionSort(arr)

print(arr)