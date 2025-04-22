soma = 0

num_A = float(input("Informe o valor A: "))
num_B = float(input("Informe o valor B: "))
num_C = float(input("Informe o valor C: "))

soma = num_A + num_B

if soma < num_C:
    print(f" A soma dos valores informados foi de {soma}\n sendo menor que que C. ")
else:
    print("O valor informado é maior que C.")