def mostra_tabela_simbolos():
    print('Tabela de símbolos - len e vetor:')          # Solução 6
    for p in range(1, len(tabela_simbolos)):
        print(f"{p} - {tabela_simbolos[p]}")
if __name__ == '__main__':
    fluxo_tokens = ''
    posicao = 1
    tabela_simbolos = list()                    # tabela_simbolos = []
    tabela_simbolos.append('')                  # Usando a posição 0
    # fluxo_caracteres = input('Digite uma expressão: ')
    fluxo_caracteres = 'nota = 243 +  nota * 342 + 5'               # Testando sem input
    # fluxo_caracteres = 'a = b = 234'
    tamanho = len(fluxo_caracteres)
    lexema = ''                                 # Lexema com 1 ou mais caractere
    for i in range(0, tamanho):
        c_atual = fluxo_caracteres[i]
        if c_atual.isalpha():
            lexema+=c_atual
            if i < tamanho-1:
                c_proximo = fluxo_caracteres[i+1]
            else:
                c_proximo = " "
            if not c_proximo.isalpha():
                if lexema in tabela_simbolos:
                    posicao_atual = tabela_simbolos.index(f"{lexema}")
                    fluxo_tokens += f"<id, {posicao_atual}>"
                    posicao +=1
                    lexema=""
                else:
                    fluxo_tokens += f'<id, {posicao}>'  # fluxo_tokens += "<"+lexema+">"
                    posicao += 1
                    tabela_simbolos.append(lexema)
                    lexema = ""
        elif c_atual.isdigit():
            lexema += c_atual
            if i < tamanho-1:
                c_proximo = fluxo_caracteres[i+1]
            else:
                c_proximo = " "
            if not c_proximo.isdigit():
                fluxo_tokens += f'<{lexema}>'  # fluxo_tokens += "<"+lexema+">"
                lexema = ""

        elif c_atual == '=' or c_atual == '+' or c_atual == '*':
            fluxo_tokens += f'<{c_atual}>'  # fluxo_tokens += "<{}>".format(c)
        elif c_atual.isspace():                             # elif c == ' ':
            pass
        else:
            fluxo_tokens += '<erro>'
    print(f'Entrada (fluxo de caracteres):\n{fluxo_caracteres}')
    print(f"Saída (fluxo de tokens):\n{fluxo_tokens}")
    mostra_tabela_simbolos()
