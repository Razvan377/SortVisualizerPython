
def BubbleSort(arr):
    n = len(arr)
    for i in range( n -1):
        for j in range(0, n- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5,3,7,4,8]

BubbleSort(arr)

print(arr)