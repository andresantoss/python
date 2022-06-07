"""
- Testes:
Fluxo de caracteres: nota1 = 85          nota = nota + valor23 + 34            5nota = v
Fluxo de tokens:     <id,1><=><85>       <id,1><=><id,1><+><id,2><+><34>       <5><id,1><=><id,2>
Tabela de símbolos:  nota1                nota                                 nota
                                          valor23                              v
"""
def mostra_tabela_simbolos():
    print(f'Tabela de símbolos:\n{tabela_simbolos}')    # Solução 1
    # print('Tabela de símbolos - in:')                   # Solução 2
    # for simbolo in tabela_simbolos:
    #     print(simbolo)
    # print('Tabela de símbolos - in:')                   # Solução 3
    # ct = 0
    # for simbolo in tabela_simbolos:
    #     print(f"{ct} - {simbolo}")
    #     ct += 1
    # print('Tabela de símbolos - enumerate - com 0:')    # Solução 4
    # for posicao, simbolo in enumerate(tabela_simbolos):
    #     print(f"{posicao} - {simbolo}")
    # print('Tabela de símbolos - enumerate - sem 0:')    # Solução 5
    # for posicao, simbolo in enumerate(tabela_simbolos):
    #     if posicao == 0:
    #         ...                             # pass
    #     else:
    #         print(f"{posicao} - {simbolo}")
    print('Tabela de símbolos - len e vetor:')          # Solução 6
    for p in range(1, len(tabela_simbolos)):
        print(f"{p} - {tabela_simbolos[p]}")
if __name__ == '__main__':
    fluxo_tokens = ''
    posicao = 1
    # tabela_simbolos = list()
    tabela_simbolos = []
    tabela_simbolos.append('')
    # tabela_simbolos = ['']
    lexema = ''
    numero = ''
    fluxo_caracteres = input('Digite uma expressão: ')
    # fluxo_caracteres = 'nota = 8'
    # fluxo_caracteres = 'nota = valor + 3'
    # fluxo_caracteres = 'nota = 234'
    # fluxo_caracteres = 'nota = valor + 234'
    # fluxo_caracteres = 'nota = nota + 345'
    # fluxo_caracteres = 'nota =     nota + ; 345 + trabalho'
    # fluxo_caracteres = 'nota =     nota + 345 + trabalho     # comentários ... '
    # fluxo_caracteres = 'nota1 = 852     # comentários ... '
    # fluxo_caracteres = 'nota = nota + valor23 + 34     # comentários ... '
    # fluxo_caracteres = '5nota = v2      # comentários ... '
    # fluxo_caracteres = 'nota_3 = v_ + 34      # comentários ... '
    # fluxo_caracteres = 'nota_3 = v_ + 34 * v_      # comentários ... '
    tamanho = len(fluxo_caracteres)

    inicio_identificador = ''
    resto_identificador = ''
    digito_ponto = ''
    for i in range(0, tamanho):
        c_atual = fluxo_caracteres[i]
        if i < tamanho - 1:       # if (i != tamanho - 1)
            c_proximo = fluxo_caracteres[i + 1]
        else:                        # Se for o último caractere do fluxoCaracteres
            c_proximo = ' '
        # lexema está vazio && é letra ou lexema não vazio && (é letra ou é dígito)
        if len(lexema) == 0 and (c_atual.isalpha() or c_atual == '_') \
                or \
                len(lexema) > 0 and (c_atual.isalpha() or c_atual == '_' or c_atual.isdigit()):
            # len(lexema) > 0 and c_atual.isalnum():
            lexema += c_atual
            #  Próximo caractere é diferente letra  &&  próximo caractere é diferente de dígito
            if not c_proximo.isalpha() and not c_proximo.isdigit() and c_proximo != '_':
                if tabela_simbolos.__contains__(lexema):
                # if lexema in tabela_simbolos:
                    ind = tabela_simbolos.index(lexema)
                    fluxo_tokens += f'<id,{ind}>'
                else:
                    fluxo_tokens += f"<id,{posicao}>"
                    tabela_simbolos.append(lexema)
                    posicao += 1
                lexema = ''
        # implementar para aceitar número real com apenas um ponto.
        elif c_atual.isdigit():
            # fluxo_tokens += "<{}>".format(c_atual)        # fluxo_tokens += f'<{c_atual}>'
            numero += c_atual
            if not c_proximo.isdigit():
                fluxo_tokens += "<" + numero + ">"
                numero = ""
        elif c_atual == '=' or c_atual == '+' or c_atual == '*':
            fluxo_tokens += "<{}>".format(c_atual)        # fluxo_tokens += f'<{c_atual}>'
        # elif c == ' ':
        elif c_atual.isspace():
            pass
        elif c_atual == '#':        # Ignora comentário de mesma linha
            break
        # elif (Quebra de linha)    ???
        #     pass
        else:
            fluxo_tokens += f'<Erro>'
    print(f'Entrada:\n{fluxo_caracteres}')
    print(f"Fluxo de tokens:\n{fluxo_tokens}")
    mostra_tabela_simbolos()
