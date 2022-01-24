import math

a = int(input("Digite um valor para a:"))
b = int(input("Digite um valor para b:"))
c = int(input("Digite um valor para c:"))

if  math.sqrt(b**2 - 4*a*c) < 0:
    print("Não tem raízes reais")

if  math.sqrt(b**2 - 4*a*c)==0:
    print("Só possui uma raiz real")

else:
    print("Possui duas raizes reais")