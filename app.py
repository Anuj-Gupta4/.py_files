# remove duplicates
numbers1 = [5,3,3,2,26,8]   
s = set(numbers1)
numbers1 = list(s)
print(numbers1)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
# matrix[0][1] = 20
# print(matrix)

# largest element in array
# numbers = [5,3,3,2,26,8]
# max_num = numbers[0]
# for i in numbers:
#     if i>max_num:
#         max_num = i
# print(max_num)

# second largest
# numbers.sort()
# print(numbers[-2])

# bubble sort
# numbers = [5, 2, 4, 1]
# for number in numbers:
#     for i in range(0, 3):
#         if numbers[i] > numbers[i+1]:
#             temp = numbers[i]
#             numbers[i] = numbers[i+1]
#             numbers[i+1] = temp
# print(numbers)
# print(numbers[-1])

# numbers = [5, 2, 4, 1]
# for number in numbers:
#     output = ''
#     for count in range(number):
#         output += "X"
#         print(output)
#     print('\n')

# for i in range(0, 3):
#     for j in range(0, 3):
#         print(f"({i}, {j})")

# this a guessing game where user gets to guess the secret number. they only get 3 guesses
# correct_num = 10
# i = 1
# while i <= 3:
#     guess = int(input("take a guess"))
#     i += 1
#     if guess == correct_num:
#         print("well done")
#         break
#     else:
#         print("you guessed wrong")
# else:
#     print("\nyou lose")

# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1

# weight = int(input("enter weight"))
# typ = (input("is it in (k)ilo or (p)ound?")).lower()
# print(typ, type(typ))
# if typ == "k":
#     new_weight = weight * 2.2
#     print(f"weight in pound is {new_weight}")
# else:
#     new_weight = weight * 0.45
#     print(f"weight in kilo is {new_weight}")

# name = "anuj"
# length = len(name)
# print(length)
# if length < 3:
#     print("must have at least 3 chars")
# elif length>50:
#     print("must have at most 50 chars")
# else:
#     print("looks good")

# credit_good = False
#
# if credit_good:
#     val = 1000000*(1+0.1)
# else:
#     val = 1000000 * (1 - 0.1)
#
# print(f"price is :Rs. {val}")

# import math
# x = 2.6
# print(math.ceil(x), math.pi, math.floor(x))
# print(round(x), abs(x))

# first, last = "anuj", "gupta"
# print(first.upper(), first.capitalize(), len(first), first.find('j'), first.replace('anuj', 'bhaatt'), first.title())
# first = first.replace('anuj', 'bhaatt')
# print(f'{first} is a {last}')

# intro = """
# my name is anuj
#
# i am god
# """
# intro1 = "anuj"
# print(intro1[2:-1])

# birth-year = int(input("enter birth year"))
# age = 2023 - birth-year
# print(age)

# name = input("enter your name")
# color = input("enter favourite color")
# print(name + " likes " + color)
#
# def name(names):
#     print(names)
#
# name("anuj" + "bhaerat")