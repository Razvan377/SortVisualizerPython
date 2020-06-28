
def merge_sort(values):

    if len(values ) >1:
        m = len(values )//2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        values =[]

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
                print(values)
            else:
                values.append(right[0])
                right.pop(0)
                print(values)

        for i in left:
            values.append(i)
            print(values)
        for i in right:
            values.append(i)
            print(values)

    return values

array = [5,1,7,3,8,4]
print(array)

array = merge_sort(array)
print(array)