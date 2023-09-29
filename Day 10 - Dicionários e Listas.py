#Vejamos como podemos utilizar listas para criar tabelas! Desta forma , utilizando essa lógica criarei um simples dicionário.

programming_dictionary = { 
  "Bug" : "An error in a program that prevents it from running as expected. ",
  "Function" : "A piece of code that you can easily call over and over again.",
  "Loop" : "The action of doing something over and over again.",
}
#Observar a padronização de boas práticas de leitura. Identação , quebra de linha e vírgula separando.

#Para consultar 👇🏻
print(programming_dictionary["Bug"])

#Para adicionar 👇🏻
programming_dictionary["Server"] = "A powerful computer, used to host and share data. Servers also generally support a far greater quantity of memory than most desktop computers."
print(programming_dictionary["Server"])

# Exercicio 2 
#Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that
# should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
#DO NOT modify lines 1-7 to change the existing student_scores dictionary.
#DO NOT write any print statements.
#This is the scoring criteria:
#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to covert scores into grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    

#Don't change the code below 👇
print(student_grades)

#Dicionario de apelidos (zueira)
dicionário_comum = {
    "Bruno": "Cabuloso",
    "Calite": "Brabo",
    "Betânia": "Betinha do meu coração",
    "Thiago": "Thiaga Vit",
    "Thais": "Zaíza",
    "Carolina": "Kiss", 
}

dicionario_apelidos = {
    {"nome": "Bruno", "Apelidos":["Brunex", "Bruneko", "Tirilo", "Pai", "Gostiozu"], "total_apelidos": 5},
    {"nome": "Calite", "Apelidos": ["Calitex", "Zehoscar", "Ocara"], "total_apelidos": 3}
}

lista_apelidos = [
    {"nome": "Bruno", "Apelidos":["Brunex", "Bruneko", "Tirilo", "Pai", "Gostiozu"], "total_apelidos": 5},
    {"nome": "Calite", "Apelidos": ["Calitex", "Zehoscar", "Ocara"], "total_apelidos": 3}

]
#Podemos organizar assim tb: 
lista_apelidos = [
    {
    "nome": "Bruno",
    "Apelidos":["Brunex", "Bruneko", "Tirilo", "Pai", "Gostiozu"], 
    "total_apelidos": 5
    },
    {
    "nome": "Calite", 
    "Apelidos": ["Calitex", "Zehoscar", "Ocara"], 
    "total_apelidos": 3
    },
]

