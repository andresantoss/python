from regex import *

if __name__ == '__main__':
    entrada = input('Entrada: ')
    vl_retorno = valida_pattern(entrada)
    if vl_retorno:
        print('Entrada válida')
    else:
        print('Entrada inválida')