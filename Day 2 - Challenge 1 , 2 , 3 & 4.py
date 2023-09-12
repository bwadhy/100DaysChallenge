#Day 2 - Challenge 1 
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first_number = two_digit_number[0]
second_number = two_digit_number[1]

sum = int(first_number) + int(second_number)
print(sum)

#Day 2 - Challenge 2
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h = float(height)
w= float(weight)
IMC = float(w/h**2)
print(IMC)

#Day 2 - Challenge 3 
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
intage = int(age)
timeleft = 90 - intage
weeks = timeleft * 52
months = timeleft * 12
days = timeleft * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#Day 2 - Challenge 4 
#Build a tip calculator. 
#Ex: If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
total = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tippercentage = (1+tip/100)

each = (total*tippercentage)/people
final = round(each,2)
print(f"Each people should pay {final}")

