def ins_sort(a):
    for i in range(len(a)):
        j=i
        while (j>0 and a[j-1]>a[j]):
            a[j-1], a[i] = a[i], a[j-1]
            j-=1
    return a

list=[1,6,4,7,74,9]
z = ins_sort(list)
print(z)
