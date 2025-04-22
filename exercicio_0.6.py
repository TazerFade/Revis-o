peso = float(input("Informe seu peso :"))
alt = float(input("Informe sua altura :"))
imc = peso/(alt*alt)
if imc < 18.6:
    print(" Você encontra-se abaixo do peso.")
elif imc >= 18.6 and imc <=24.9:
    print("Você encontra-se no peso ideal (parabéns)")
elif imc >= 25.0 and  imc <29.9:
    print("Você está levemente acima do peso")
elif imc >= 30.0 and imc <= 34.9:
    print("Você encontra-se no nível de obesidade grau |")
if imc >= 35.0 and imc <=39.9:
    print("Você encontra-se no nível de obesidade grau ||(severa)")
if imc >= 40:
    print("Você está no nível de obesidade grau ||| (mórbido)")