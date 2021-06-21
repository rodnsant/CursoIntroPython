print ("Vamos calcular o seu IMC (ìndice de Massa Corpotal)?")

peso = float(input ("Qual o seu peso? (Kg): "))

altura = (float(input("Qual a sua altura? (cm): "))/100)

imc = peso/(altura*altura)

if imc < 18.5:
    classificacaoIMC = "Abaixo do Peso"

if imc >= 18.5 and imc < 25:
    classificacaoIMC = "Peso Normal"

if imc >=25 and imc < 30:
    classificacaoIMC = "Sobrepeso"
    
if imc >=30 and imc < 35:
    classificacaoIMC = "Obesidade Grau I"

if imc >=35 and imc < 40:
    classificacaoIMC = "Obesidade Grau II"

if imc >=40:
    classificacaoIMC = "Obesidade Mórbida"

print ("O seu IMC é de", imc)

print ("A classificação de seu IMC é:", classificacaoIMC)