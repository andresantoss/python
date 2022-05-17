import re                                                                                       # Impote biblioteca regexp 
def mostra_tabela_simbolos():                                                                   # Função para mostrar a tabela de simbolos
    print('\nTabela de símbolos - len e vetor:')                                                # Print Tabela de símbolos - len e vetor:
    for p in range(1, len(tabela_simbolos)):                                                    # For para ajustar a formatação do print
        print(f"{p} - {tabela_simbolos[p]}")                                                    # Print da tabela de simbolos
if __name__ == '__main__':                                                                      # Main
    fluxo_tokens = ''                                                                           # Definição de variavel vasia
    posicao = 1                                                                                 # Definição de variavel posição
    lista_fluxo_caracteres = []                                                                 # Definição da lista de lista_fluxo_caracteres vasia
    tabela_simbolos = []                                                                        # Definição da lista de tabela_simbolos vasia
    tabela_simbolos.append('')                                                                  # Usando a posição 0
    fluxo_caracteres = 'valor4 = nota33 + valor4 * 23 # Comentários ...'                        # Teste sem input
    fluxo_caracteres = re.sub(r'#.*', '', fluxo_caracteres)                                     # Retirando comentarios do input
    tamanho = len(fluxo_caracteres)                                                             # Definindo o tamanho da input 
    lexema = ''                                                                                 # Lexema com 1 ou mais caractere
    for i in range(0, tamanho):                                                                 # Looping de acordo com o tamanho do fluxo_caracteres
        lista_fluxo_caracteres.append(fluxo_caracteres[i])                                      # Lista_fluxo_caracteres aprendendo fluxo_caracteres da posição i
        c_atual = fluxo_caracteres[i]                                                           # Definindo c_atual como o caracter do fluxo_caracteres
        if c_atual.isdigit() or c_atual.isalpha():                                              # Verifica se o caracter atual e digito ou nuimerico
            lexema += c_atual                                                                   # Adiciona no lexema o caracter
        if c_atual.isdigit():                                                                   # Verifica se o caracter atual e digito
            if i < tamanho-1:                                                                   # Caso o tamanho - 1 for menor que a posição i
                c_proximo = fluxo_caracteres[i+1]                                               # Define c_proximo como fluxo_caracteres proximo
            else:                                                                               # Do contrario
                c_proximo = " "                                                                 # Define como espaço
            if not c_proximo.isdigit():                                                         # Verifica se o proximo caracter e não e digito
                if not lexema.isdigit():                                                        # Verifica se o lexema atual não e digito
                    if lexema in tabela_simbolos:                                               # Verifica se o lexema atual esta na tabela_simbolos
                        posicao_atual = tabela_simbolos.index(f"{lexema}")                      # Define a posicao_atual como tabela_simbolos com a posição do lexema para gerar o fluxo de tokens
                        fluxo_tokens += f'<id,{posicao_atual}>'                                 # Fluxo_tokens += "<"+lexema+">"
                        posicao += 1                                                            # Proxima posição
                        lexema = ""                                                             # Lexema vasio
                    else:                                                                       # Do contrario
                        fluxo_tokens += f'<id,{posicao}>'                                       # Fluxo_tokens += "<"+lexema+">"
                        posicao += 1                                                            # Proxima posição
                        tabela_simbolos.append(lexema)                                          # Aprendeno o lexema atual
                        lexema = ""                                                             # Lexema vasio
                else:                                                                           # Do contrario
                    fluxo_tokens += f'<{lexema}>'                                               # Fluxo_tokens += "<"+lexema+">"
                lexema = ""                                                                     # Lexema vasio
        elif c_atual.isalpha():                                                                 # Verifica se o caracter atual e numerico
            if i < tamanho-1:                                                                   # Caso o tamanho - 1 for menor que a posição i
                 c_proximo = fluxo_caracteres[i+1]                                              # Define c_proximo como fluxo_caracteres proximo
            else:                                                                               # Do contrario
                 c_proximo = " "                                                                # Define como espaço
            if c_proximo == " ":                                                                # Caso c_proximo seja espaço
                if lexema in tabela_simbolos:                                                   # Verifica se o lexema atual esta na tabela_simbolos
                    posicao_atual = tabela_simbolos.index(f"{lexema}")                          # Define a posicao_atual como tabela_simbolos com a posição do lexema para gerar o fluxo de tokens
                    fluxo_tokens += f"<id,{posicao_atual}>"                                     # Fluxo_tokens += "<"+lexema+">"
                    posicao +=1                                                                 # Proxima posição
                    lexema=""                                                                   # Lexema vasio
            else:                                                                               # Do contrario
                    fluxo_tokens += f'<id,{posicao}>'                                           # Fluxo_tokens += "<"+lexema+">"
                    posicao += 1                                                                # Proxima posição
                    tabela_simbolos.append(lexema)                                              # Aprendeno o lexema atual
                    lexema = ""                                                                 # Lexema vasio
        elif c_atual == '=' or c_atual == '+' or c_atual == '*':                                # Verifica se o caracter atual e referente a alguma operação matematica
            fluxo_tokens += f'<{c_atual}>'                                                      # Fluxo_tokens += "<{}>".format(c)
        elif c_atual.isspace():                                                                 # Caso c_atual seja espaço                        # elif c == ' '
            pass                                                                                # Continua
        else:                                                                                   # Do contrario
            fluxo_tokens += '<erro>'                                                            # Define fluxo_tokens  como erro
print(f'Entrada (fluxo de caracteres):\n{fluxo_caracteres}')                                    # Print Entrada (fluxo de caracteres)
print(f"Saída (fluxo de tokens):\n{fluxo_tokens}")                                              # Print Saída (fluxo de tokens)
mostra_tabela_simbolos()                                                                        # Chama a função mostra_tabela_simbolos para apresentar a tabela formatada 
