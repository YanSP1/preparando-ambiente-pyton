# 
print("=" * 40)
print("Testando ambiente Python")
print("=" * 40)

none = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

anos_para_100 = 100 - idade

print("\n--- Resultado ---")
print(f"Olá,{none}!")
print(f"você tem {idade} anos.")

if anos_para_100 > 0:
    print(f"Faltam {anos_para_100} anos para você completar 100 anos.")
elif anos_para_100 == 0:
    print("Parabéns! Você tem exatamente 100 anos.")
else:
    print(f"Você já passou dos 100 anos há {-anos_para_100} anos.")

print("\n Seu ambiente Python está funcionando corretamente!")