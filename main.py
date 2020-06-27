from tkinter import *
import random

root = Tk()
root.title("Sort Visualizer")

c = Canvas(root, width=1200, height=700)
c.grid()

def GenerateArray():
    c.delete("all")
    position = 0
    global array
    array = []
    for num in range(200):
        num = random.randrange(1,200)
        array.append(num)
    for num in array:
        c.create_line(150+position,1,150+position,num*3)
        position += 4
    #c.create_line(150, 1, 150, 200)

def SelectionSort():
    GenerateArray()


generate_b = Button(root, text="Generate new array", command=GenerateArray)
generate_b.grid(row=3, column=0)

selectionSort_b = Button(root, text="Selection Sort", command=SelectionSort)
selectionSort_b.grid(row=3, column=1)

# d = {}
#
# for x in range(10):
#     d[f"string{x}"] = "Hi"
#
# print(d["string5"])


root.mainloop()

