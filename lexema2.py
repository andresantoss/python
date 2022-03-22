lexemas = []
tokens=[]
ct=1
ids=[]
lista_f = []
operadores = ['+','*','=']
while True:
    entrada = str(input('DIGITE UM LEXEMA'))
    lista = list(entrada)
    #print(lista)
    for i in lista:
        if i == ' ':
            lista.remove(i)
        else:
            continue
    #print(lista)

    for i in lista:
        if i.isalpha() == True and i not in lexemas:
            lista_f.append(f'<id,{ct}>')
            lexemas.append(i)
            ids.append(ct)
            ct += 1
        elif i.isdigit() == True:
            lista_f.append(f'<{i}>')
        elif i.isascii() == True and i in operadores:
           lista_f.append(f'<{i}>')
        elif i in lexemas:
            lista_f.append(f'<id,{lexemas.index(i)+1}>')
            continue
        else:
            lista_f.append('<erro>')
    break
for i in lista_f:
    print(i, end='')
