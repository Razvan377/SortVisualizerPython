from tkinter import *
import random
import time

root = Tk()
root.title("Sort Visualizer")

c = Canvas(root, width=1200, height=700)
c.grid()

pos = 0
array = []
notSorted = True
for num in range(201):
    num = random.randrange(1, 201)
    array.append(num)


def GenerateArray():
    c.delete("all")
    position = 0
    global array
    array = []
    global pos
    global notSorted
    notSorted = True
    pos = 0
    for num in range(200):
        num = random.randrange(1,200)
        array.append(num)
    for num in array:
        c.create_line(150+position,1,150+position,num*3)
        position += 4
    #c.create_line(150, 1, 150, 200)


def SelectionSort():
    global pos
    global notSorted
    while (notSorted):
        test_array = array[:]
        test_array.sort()
        if (test_array == array):
            notSorted = False

        smallest_index = findSmallest(array[pos:]) + pos

        smallest = array[smallest_index]

        array.pop(smallest_index)

        array.insert(pos, smallest)

        pos += 1
        repaint(array, smallest, notSorted)
        c.update_idletasks()
        print(array)
        time.sleep(0.05)


def BubbleSort():
    global notSorted
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
                test_array = array[:]
                test_array.sort()
                if (test_array == array):
                    notSorted = False
                bubbleRepaint(array, notSorted, array[j], array[j+1])
                c.update_idletasks()


# def MergeSort():
#     global notSorted
#     global array
#     if len(array) >1:
#         m = len(array)//2
#         left = array[:m]
#         right = array[m:]
#         left = mergesort1(left)
#         right = mergesort1(right)
#
#         array =[]
#
#         while len(left) > 0 and len(right) > 0:
#             if left[0] < right[0]:
#                 array.append(left[0])
#                 left.pop(0)
#                 mergepaint(array)
#                 c.update_idletasks()
#
#             else:
#                 array.append(right[0])
#                 right.pop(0)
#                 mergepaint(array)
#                 c.update_idletasks()
#
#
#         for i in left:
#             array.append(i)
#         for i in right:
#             array.append(i)
#
#         print(array)
#
# def mergesort1(array):
#     if len(array) > 1:
#         m = len(array) // 2
#         left = array[:m]
#         right = array[m:]
#         left = mergesort1(left)
#         right = mergesort1(right)
#
#         array = []
#
#         while len(left) > 0 and len(right) > 0:
#             if left[0] < right[0]:
#                 array.append(left[0])
#                 left.pop(0)
#             else:
#                 array.append(right[0])
#                 right.pop(0)
#
#         for i in left:
#             array.append(i)
#         for i in right:
#             array.append(i)
#
#     return array


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def repaint(array, smallest, listSorted):
    c.delete("all")
    position = 0
    if(listSorted != True):
        for num in array:
            c.create_line(150 + position, 1, 150 + position, num * 3, fill='green')
            position += 4
    else:
        for num in array:
            if(num == smallest):
                c.create_line(150 + position, 1, 150 + position, num * 3, fill='red')
            else:
                c.create_line(150+position,1,150+position,num*3)
            position += 4


def bubbleRepaint(array, listSorted, n1, n2):
    c.delete("all")
    position = 0
    if (listSorted != True):
        for num in array:
            c.create_line(150 + position, 1, 150 + position, num * 3, fill='green')
            position += 4
    else:
        for num in array:
            if (num == n1 or num == n2):
                c.create_line(150 + position, 1, 150 + position, num * 3, fill='red')
            else:
                c.create_line(150 + position, 1, 150 + position, num * 3)
            position += 4

# def mergepaint(array):
#     c.delete("all")
#     position = 0
#     for num in array:
#         c.create_line(150 + position, 1, 150 + position, num * 3)
#         position += 4


generate_b = Button(root, text="Generate new array", command=GenerateArray)
generate_b.grid(row=3, column=0)

selectionSort_b = Button(root, text="Selection Sort", command=SelectionSort)
selectionSort_b.grid(row=3, column=1)

# mergeSort_b = Button(root, text="Merge Sort", command=MergeSort)
# mergeSort_b.grid(row=3, column=2)

bubbleSort_b = Button(root, text="Bubble Sort", command=BubbleSort)
bubbleSort_b.grid(row=3, column=2)


root.mainloop()