#Day 3 - Challenge 1
#Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")

#Day 3 - Challenge 2
#Create a BMI Calculator 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round( weight / height**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")

#Day 3 - Challenge 3 
#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400
#e.g. The year 2000:
#2000 ÷ 4 = 500 (Leap)
#2000 ÷ 100 = 20 (Not Leap)
#2000 ÷ 400 = 5 (Leap!)
#So the year 2000 is a leap year.


year = int(input("Which year do you want to check? "))
if year % 4 > 0:
    print("Not leap year")
else:
    if year % 100 > 0 :
        print("Leap year")
    else: 
        if year % 400 == 0:
            print("Leap year")
        else: 
            print("Not leap year")

#Day 3 - Challenge 4
#Create a treasure island game.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

pergunta1 = input("Voce foi sequestrado, vendado e mantido em cativeiro. No segundo dia tiraram sua venda e fizeram-lhe optar entre a pílula azul ou a vermelha. Qual você escolhe?\n").lower()
if pergunta1 == "vermelha":
    print("Você foi envenenado. Fim do jogo.")
elif pergunta1 == "azul":
    print("\nVocê foi liberto do cativeiro, porém agora você está em um jogo. Você precisa passar de mais 3 etapas para ser completamente livre. Fique atento às instruções.\n ")
pergunta2 = input('\nVocê estava dentro de uma bar e recebeu um bilhete com a seguinte mensagem: "PEGUE UMA MOEDA E JOGUE CARA OU COROA". Qual foi o resultado do girar da moeda?\n').lower()
if pergunta2 == "coroa" :
    print("Você foi assassinado com um tiro pelas costas")
elif pergunta2 == "cara":
    print("\nHoje é seu dia de sorte, você escapou de uma emboscada. Entre na parte interior do bar. \n")

pergunta3 = input("Ao adentrar o bar , você avistou três portas. Escolha uma delas: 1 2 ou 3.\n")
if pergunta3 == "1":
    print('''\n
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
\n''')
    print("\nVocê sobreviveu ao jogo Prova da Morte, abra a caixa e pegue seus 10 milhões em Bitcoin\n")
elif pergunta3 == "2":
    print("Você acionou um explosivo e foi deletado. ")
elif pergunta3 == "3":
    print("Você foi eletrocutado e virou churrasco. ")



