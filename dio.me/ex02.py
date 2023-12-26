# Inverta uma string

print("Digite o seu nome: ")
name = input()

length = len(name)
newName = ""

for i in range(length):
    length = length - 1
    newName = newName + name[length]

print("O seu nome ao contrario é: " + newName)
