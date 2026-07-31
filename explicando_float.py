# Explicando o tipo float

#Errado
valor = 1, 44

print(valor)
print(type(valor))
print('Formatação incorreta do número decimal\n')

#Certo
valor = 1.44

print(valor)
print(type(valor))
print('Formatação correta do número decimal\n')

#É possível
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
print('É possível atribuir múltiplos valores a múltiplas variáveis, mas não é a forma correta de representar um número decimal\n')

#Convertendo float para int
res = int(valor)
print(res)
print(type(res))

# Números complexos
variavel = 5j
print(variavel)
print(type(variavel))