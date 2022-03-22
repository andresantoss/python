lexema = input("digite um lexema:")
operadores = ['+', '*', '=']
idx = 1
saida = []
for char in lexema:
    if char.isalpha():
        saida.append("<id,{0}>".format(idx))
        idx += 1
    elif char.isdigit():
        #saida.append("<num,{0}>".format(char))
        saida.append("<{0}>".format(char))
    elif char in operadores:
        saida.append("<{0}>".format(char))

print(*saida, sep="")

