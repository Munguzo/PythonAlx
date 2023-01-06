# colors = ['blue', 'navy', 'red', 'pink', 'yellow']
# for color in colors:
#     colors.append('green')
#     print(colors)

#the list gets longer and longer as the loop continues.

#To avoid this issue, I create a new list to hold the modified values,
colors = ['blue', 'navy', 'red', 'pink', 'yellow']
modified_colors = []
for color in colors:
    modified_colors.append('green')
    print(modified_colors)