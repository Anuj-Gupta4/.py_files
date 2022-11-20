n=int(input("Enter any number: "))
a=list(map(int,str(n)))
print(a)
b=list(map(lambda x: x**3, a))
print(b)
if sum(b)==n:
    print("armstrong")
else:
    print("not armstrong")