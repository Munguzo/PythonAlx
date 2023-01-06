#Write a program with a variable called age assigned to an integer that prints different
#strings depending on what integer age is.

age = 22

if age < 18:
    print("You are a minor. go back to school")
elif age >= 18 and age < 21:
    print("You are an adult but not yet able to legally drink alcohol.")
else:
    print("You are an adult and able to legally drink alcohol. Enjoy😂")
