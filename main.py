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


generate_b = Button(root, text="Generate new array", command=GenerateArray)
generate_b.grid(row=3, column=0)

selectionSort_b = Button(root, text="Selection Sort", command=SelectionSort)
selectionSort_b.grid(row=3, column=1)


root.mainloop()