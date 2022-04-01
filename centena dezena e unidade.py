"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input("Digite um número menor do que 1000:"))
frase = ""

if numero > 1000:
    print("Entrada invalida!")

elif numero < 0:
    print("Entrada invalida!")

else:
    centena = numero // 100
    dezena = (numero%100)//10
    unidade = numero -(centena*100 + dezena*10)
    if centena <= 1:
        if dezena <= 1:
            if unidade <= 1:
                print(numero," = ",centena," centena, ",dezena," dezena e ",unidade," unidade")
        else:
            if unidade <= 1:
                print(numero," = ",centena," centena, ",dezena," dezenas e ",unidade," unidade")
            else:
                print(numero," = ",centena," centena, ",dezena," dezenas e ",unidade," unidades")
    elif centena > 1:
        if dezena <= 1:
            if unidade <= 1:
                print(numero," = ",centena," centenas, ",dezena," dezena e ",unidade," unidade")
        else:
            if unidade <= 1:
                print(numero," = ",centena," centenas, ",dezena," dezenas e ",unidade," unidade")
            else:
                print(numero," = ",centena," centenas, ",dezena," dezenas e ",unidade," unidades")
        

