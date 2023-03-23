def quick_sort(list):
    if len(list)<=1:
        return list

    pivot = list[0]
    left = []
    right = []

    for i in range(1, len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

list=[1,6,4,7,74,9]
z = quick_sort(list)
print(z)