#  pattern = r"^ \d $"
#  pattern = r"^ \D $"
#  pattern = r"^ [0-9] $"
#  pattern = r"^ [^0-9] $"
#  pattern = r"^ \d\d $"  ou    r"^ [0-9][0-9] $"    ou     r"^ \d{2} $"   ou    r"^ [0-9]{2} $"
#  pattern = r"^ \d{3} "        # $ representa o final da função regular.
#  pattern = r"^ \d{3,} "        # Pelo menos 3 dígitos.
#  pattern = r"^ \d{2,4} "       # Entre 2 e 4 Dígitos.

import re                                   # Biblioteca para usar expressões regulares
def valida_pattern(entrada):
    pattern = r"^\d$"                       # Somente um dígito
    b = bool(re.match(pattern, entrada))
    return b


"""

- Exercícios 1:
a. Crie a função valida_pattern e crie a função main
b. Implementar uma estrutura de repetição e use o "s" minúsculo como condição de saída. 
c. Refaça o item anterior e use "S" maiúsculo ou "s" minúsculo como condição de saída.
d. Aceitar somente um dígito qualquer. 2 maneiras.
e. Aceitar qualquer caractere não dígitos. Apenas 1 caractere. Resolva de 2 maneiras.
f. Aceitar qualquer dígito com exceção do zero. Apenas 1 dígito. Inválido: a, \, 0 
g. Aceitar somente 2 dígitos quaisquer. Resolva de 3 maneiras.            
h. Aceitar pelo menos 3 dígitos quaisquer. 2 maneiras.
i. Aceitar entre 2 e 4 dígitos quaisquer. 2 maneiras.                 
j. Aceitar 1 ou 2 dígitos quaisquer. Resolva de 4 maneiras.
k. Aceitar 0 ou 1 dígito (a quantidade de dígitos). Resolva de 3 maneiras.
l. Aceitar 0 ou qualquer quantidade de dígitos.
m. Aceitar 1 ou qualquer quantidade de dígitos.  Resolva de 2 maneiras.
n. Aceitar 0 ou qualquer quantidade de não dígitos.
o. Aceitar 3 dígitos quaisquer sendo o primeiro diferente de zero. Resolver de 3 maneiras.
   Inválido: a12                                                 
p. Aceitar 0 ou qualquer quantidade de qualquer caractere word (palavra).  // 2 maneiras.
q. Aceitar 0 ou qualquer quantidade de não qualquer caractere word (palavra). 
r. Aceitar 0 ou qualquer quantidade de qualquer caractere de espaço em branco.
s. Aceitar 0 ou qualquer quantidade de não qualquer caractere de espaço em branco.
u. Aceitar somente duas letras: a primeira maiúscula e a segunda minúscula.
v. Aceitar somente uma letra, pode ser maiúscula ou minúscula. Resolva de 2 maneiras.
w. Aceitar somente uma vogal minúscula.
x. Aceitar somente uma consoante minúscula. Teste com dígitos e com outros símbolos(falso). 4 maneiras
y. Aceitar somente uma consoante minúscula ou maiúscula. 
z. Aceitar o primeiro nome de uma pessoa. Só letras, a primeira maiúscula e as outras minúsculas.

"""



