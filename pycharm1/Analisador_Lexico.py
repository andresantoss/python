import re
entrada = input("Digite um lexema: ")
operadores = ["=", "+", "*"]
lexema = []
lexema2 = []
lexema_sem_repeticao = []
entrada = re.sub(r'#.*','',entrada)
#print(entrada)
for i in entrada:
    if i != " ":
        lexema2.append(i)
        x = "".join(lexema2)
#print(x)
for i in x:
    if i.isalpha():
        if i in lexema_sem_repeticao:
            lexema.append(f"<id,{lexema_sem_repeticao.index(i) + 1}>")
        else:
            lexema_sem_repeticao.append(i)
            lexema.append(f"<id,{lexema_sem_repeticao.index(i) + 1}>")
    elif i.isdigit():
        if i in lexema:
            lexema.append(f"<{i}>")
        else:
            lexema.append(f"<{i}>")
    elif i in operadores:
        lexema.append(f"<{i}>")
    else:
        lexema.append("<erro>")
print("\nTabela de Simbolos:")
for i in lexema_sem_repeticao:
    print(f'{lexema_sem_repeticao.index(i)+1} {i}')
print(*lexema, sep="")
#print(*lexema2, sep="")
#print(*lexema_sem_repeticao, sep="")
