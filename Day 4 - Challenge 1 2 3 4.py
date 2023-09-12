#Day 4 - Challenge 1 
#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

import random

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

#Day 4 - Challenge 2
#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
numero_pessoas= len(names)
random_number = random.randint(0, numero_pessoas-1)
print(names[random_number] + " is going to buy the meal today!" )

#Day 4 - Challenge 3
#You are going to write a program that will mark a spot with an X in the 3x3 map.
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#Day 4 - Challenge 4
