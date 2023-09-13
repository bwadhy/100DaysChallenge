#Day 5 - Challenge 1 
#You are going to write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height = total_height + height 


number_students = 0
for student in student_heights:
    number_students += 1


avg_height = round(total_height/number_students)
print(avg_height)

#Day 5 - Challenge 2
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#You are going to write a program that calculates the highest score from a List of scores.

highest_score = 0
for score in student_scores:
    if score > highest_score:
       highest_score = score
print(f"The highest score in the class is: {highest_score}")

#Day 5 - Challenge 3
#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

total = 0
for number in range(2, 101, 2):
    total = total + number
print(total)

#Day 5 - Challenge 4  
#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

contador = 0
for number in range (1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else: 
        print(number)

#Day 5 - Challenge 5
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#(I erased the code, will retry later)

#Hard Level - Order of characters randomised:

password_list = []
for char in range (1 , nr_letters +1):
    password_list.append(random.choice(letters))
for char in range (1 , nr_numbers +1):
    password_list.append(random.choice(numbers))

for char in range (1, nr_symbols +1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password_string = ""
for char in password_list:
    password_string += char
print(password_string)
  
