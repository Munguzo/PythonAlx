#This program is based on converting digital numbers into words.
#I will use dictionnary and for loops.

phone = input("Phone Number: ")
number = {
    "+":"plus",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
result = ""
for characters in phone:
    result+=number[characters] + " "

print(result)