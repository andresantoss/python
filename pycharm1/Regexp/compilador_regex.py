import re
def mostra_tabela_simbolos():
    #print(f'Tabela de símbolos:\n{tabela_simbolos}')
    print('Tabela de símbolos - len e vetor:')
    for p in range(1, len(tabela_simbolos)):
        print(f"{p} - {tabela_simbolos[p]}")
if __name__ == '__main__':
    fluxo_tokens = ''
    posicao = 1
    tabela_simbolos = []
    tabela_simbolos.append('')
    lexema = ''
    numero = ''
    fluxo_caracteres = 'Nota02 = Bola * 456 - Folha7 + Bola #comentário'
    tamanho = len(fluxo_caracteres)
    inicio_lexema = r"^[A-Za-z_]$"
    digito_ponto = r"^[0-9]$"
    for i in range(0, tamanho):
        c_atual = fluxo_caracteres[i]
        if i < tamanho - 1:
            c_proximo = fluxo_caracteres[i + 1]
        else:
            c_proximo = ' '
        if len(lexema) == 0 and (bool(re.match(inicio_lexema, c_atual)) or c_atual == '') or len(lexema) > 0 and (bool(re.match(inicio_lexema, c_atual)) or c_atual == '' or bool(re.match(digito_ponto, c_atual))):
            lexema += c_atual
            if not bool(re.match(inicio_lexema, c_proximo)) and not bool(re.match(digito_ponto, c_proximo)) and c_proximo != '_':
                if tabela_simbolos.__contains__(lexema):
                    ind = tabela_simbolos.index(lexema)
                    fluxo_tokens += f'<id,{ind}>'
                else:
                    fluxo_tokens += f"<id,{posicao}>"
                    tabela_simbolos.append(lexema)
                    posicao += 1
                lexema = ''
        # implementar para aceitar número real com apenas um ponto.
        elif bool(re.match(digito_ponto, c_atual)):
            numero += c_atual
            if not bool(re.match(digito_ponto, c_proximo)):
                fluxo_tokens += f"<{numero}>"
                numero = ""
        elif c_atual == '=' or c_atual == '+' or c_atual == '*':
            fluxo_tokens += f"<{c_atual}>"
        elif c_atual.isspace():
            pass
        elif c_atual == '#':
            break
        else:
            fluxo_tokens += f'<Erro>'
    print(f'Entrada:\n{fluxo_caracteres}')
    print(f"Fluxo de tokens:\n{fluxo_tokens}")
    mostra_tabela_simbolos()
