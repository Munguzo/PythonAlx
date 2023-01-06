#Find a largest number in a list.

numbers = [4, 5 , 3, 2, 8, 200, 340, 6]
#I assume that the largest number in my list is the first number.
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
print(max)