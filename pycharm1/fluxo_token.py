def mostra_tabela_simbolos():
   print('Tabela de símbolos - len e vetor:')
    for p in range(1, len(tabela_simbolos)):
        print(f"{p} - {tabela_simbolos[p]}")
fluxo_tokens = ''
posicao = 1
tabela_simbolos = list()
# tabela_simbolos = []
tabela_simbolos.append('')                  # Usando a posição 0
# fluxo_caracteres = input('Digite uma expressão: ')    # Testando com input
fluxo_caracteres = 'a = 243 +  r * 342 + 5'                        # Testando sem input
tamanho = len(fluxo_caracteres)
numero = ""
for i in range(0, tamanho):
    c = fluxo_caracteres[i]
    if c.isalpha():                         # Versão 2
        fluxo_tokens += "<id," + str(posicao) + ">"  # fluxo_tokens += f"<id,{posicao}>"
        tabela_simbolos.append(c)
        posicao += 1
        # if c == " ":
    elif c.isdigit():
        numero = numero+c   #concatenar número no mesmo token <243>
        try:
            proximo = fluxo_caracteres[i + 1]
            if not proximo.isdigit():
                fluxo_tokens += "<{}>".format(numero)
                numero=""
        except IndexError:
            fluxo_tokens += "<{}>".format(numero)
            numero = ""



    elif c == '=' or c == '+' or c == '*':
        fluxo_tokens += "<{}>".format(c)            # fluxo_tokens += f'<{c}>'
    # elif c == ' ':
    elif c.isspace():
        pass
    else:
        fluxo_tokens += '<erro>'                    # fluxo_tokens += f'<erro>'

print(f'Entrada (fluxo de caracteres):\n{fluxo_caracteres}')
print(f"Saída (fluxo de tokens):\n{fluxo_tokens}\n")
mostra_tabela_simbolos()
