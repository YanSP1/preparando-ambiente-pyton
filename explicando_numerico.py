print("""
Conversão de tipos

Todo valor recebido por input() é uma string.
Para realizar operações matemáticas, é necessário converter o valor.

Funções mais comuns:
- int()   -> inteiro
- float() -> decimal
- str()   -> texto
- bool()  -> booleano (True ou False)
""")

num = input("Digite um número: ")

print(f"\nValor recebido: {num}")
print(f"Tipo original: {type(num)}")

num = int(num)

print(f"\nApós converter com int(): {num}")
print(f"Novo tipo: {type(num)}")