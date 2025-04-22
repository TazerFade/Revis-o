cont,x = 0,1

while x != 500:
    for x in range(1, 501):
        if x % 2 == 1 and cont < 1:
            print(x, end=" ")
            cont += 1
        elif x % 2 == 1 and cont == 1:
            print(x, end= " ")