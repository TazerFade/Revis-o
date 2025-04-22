
while ask = S:

num =  float(input("Digiite seu número :"))

if num >0:
    if num%2==0:
         print("o número descrito é par e positivo.")
    else:
        print("O número descrito é impar e positivo.")
else:
    if num%2==1:
        if num < 0:
            print(" O número descrito é ímpar e negativo.")
        else:
            print("O número descrito é par e negativo ")

ask = input("cê quer fazer denovo S/N : ?")