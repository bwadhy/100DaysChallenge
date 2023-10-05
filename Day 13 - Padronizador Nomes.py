# Projeto para padronizar os nomes , deixando sempre a primeira letra maiúscula e o restante minúscula para cada nome.

def consertador(nome,sobrenome):
    nome_formatado = nome.title()
    sobrenome_formatado = sobrenome.title()
    print(f"{nome_formatado} {sobrenome_formatado} ")
consertador("TcheruLynNa", "tRENZAO")

#Alternativamente podemos fazer (observar a troca de print por return)

def consertador(nome,sobrenome):
    nome_formatado = nome.title()
    sobrenome_formatado = sobrenome.title()
    return f"{nome_formatado} {sobrenome_formatado}"
string_formatado = consertador("TcheruLynNa", "tRENZAO")
print(string_formatado)
### OU MAIS DIRETO AINDA
print(consertador("TcheruLynNa", "tRENZAO"))
