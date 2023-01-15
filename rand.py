# f=lambda x:bool(x%2)
# print(f(20), f(21))

# a = 4+3%5
# print(a)

# __init__=1

# 1st_string=1

# def f1():
#     global x 
#     x+=1
#     print(x) 
#     x=12 
#     print('x')

# print(type(type(int)))

# s = '\t\twelcome\n'
# print(s.strip())

# a = [1,3,5,7]
# b = {1:1, 2:4, 3:9, 4:1, 5:25}
# for i in zip(a, b):
#     print(i)

# rotate list by k towards right
# head = [1,2,3,4,5]
# k = 2
# head = (head[len(head) - k:len(head)] + head[0:len(head) - k])
# print(head)

# check palindrome
# s="A man, a plan, a canal: Panama"
# a = ""
# for i in s:
#     if i.isalnum():
#         a = a + i

# print(a.lower())
# ans = a[::-1]
# print(ans)
# if a==ans:
#     print(True)
# else:
#     print(False)


# baseball game
# ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
# list= []
# for i in ops:
#     if i=="C":
#         list.pop()
#     elif i=="D":
#         list.append(list[-1]*2)
#     elif i=="+":
#         list.append(list[-1] + list[-2])
#     else:
#         list.append(int(i))

# print(sum(list))


# a = [1,2,3,4]
# b = [sum(a[0:x+1]) for x in range(0, len(a))]
# print(b)

# x = "abcdef"
# i = "a"
# while i in x[:-1]:
#     print(i, end="")

# import re
# reslt = re.findall('welcome ')

# open(file=scor.txt)

# z = set('abc')
# z.add('san')
# z.update(set(['p', 'q']))
# print(z)

# y = [2, 5J, 6]
# y.sort()
# print(y)

# print("jvjyh kguk".capitalize())

# a = [1,2]
# n= [1,3,4]
# print(a==n)
# print(set(a)==set(n))
# # # a.append(n)

# f = None
# for i in range(5):
#     with open("app.log","w") as f:
#         if i>2:
#             break
# print(f.closed)