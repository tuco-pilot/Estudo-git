"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif a > c:
    if a > b:
        print(a)
    else:
        print(b)
elif b > a:
    if b > c:
        print(b)
    else:
        print(c)
elif b > c:
    if b > a:
        print(b)
    else:
        print(a)
elif c > a:
    if c > b:
        print(c)
    else:
        print(b)
elif c > b:
    if c > a:
        print(c)
    else:
        print(a)
