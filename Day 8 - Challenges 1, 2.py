#Day 8 - Challenge 1 
#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
#Given a random height and width of wall, calculate how many cans of paint you'll need to buy. PS: You can't buy half a can ;)

number of cans = (wall height x wall width) ÷ coverage per can.
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

import math
def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

#Day 8 - Challenge 2 
#Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#You need to write a function that checks whether if the number passed into it is a prime number or not.

n = int(input("Check this number: "))
prime_checker(number=n)

is_prime = True
def prime_checker(number):
    for i in range (2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
      
        



    


