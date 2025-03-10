"""
    Calculadora de IMC
"""

altura = int(input('Qual sua Altura? '))
peso = int(input('Qual seu peso? '))

altura_metros = altura/100
imc = peso/(altura_metros*altura_metros)

if imc >= 40:
    print(f'Seu imc é de:{imc}, OBESIDADE GRAVE')
elif imc >= 30:
    print(f'Seu imc é de:{imc}, OBESIDADE')
elif imc >= 25:
    print(f'Seu imc é de:{imc}, SOBREPESO')
elif imc >= 18.5:
    print(f'Seu imc é de:{imc}, NORMAL')
else:
    print(f'Seu imc é de:{imc}, MAGRESA')
