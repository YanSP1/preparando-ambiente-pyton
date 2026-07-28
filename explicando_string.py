print("Insira um nome: ")
nome = input()

print('\nNome inserido: %s' % nome)
print('Aqui você viu a forma 2.x antiga de formatar strings, que ainda funciona, mas não é a mais recomendada atualmente.\n')

print("Nome inserido: {0}".format(nome))
print("Aqui você viu a forma 3.x de formatar strings, que é mais recomendada atualmente.\n")

print(f'Nome inserido: {nome}')
print("Aqui você viu a forma 3.6+ de formatar strings, que é a mais recomendada atualmente.\n")

print("""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas.

Exemplos:

- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
- Aspas duplas triplas -> \"\"\"Angelina Jolie\"\"\"
""")