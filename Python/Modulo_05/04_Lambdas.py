"""
                                Functions em iterables
        Segue a mesma lógica de list comprehensions, porem, pode ser considerada
    ainda mais simples.

        Basicamente alguns métodos e funções que já existem no Python podem rodar
    uma function para cada item, da mesma forma que fizemos com list comprehension

        Uma função que permite que a gente faça isso é o map function

    lista = list(map(função, iteravel_original))

"""

print()

# Digamos que tenhamos uma função, criada por nós para padronizar um texto, conforme
# código abaixo
def padronizar_texto(args):
    args = args.casefold().replace("  ", " ").strip()
    return args

# Esta é a lista que precisamos padronizar
produtos = ['  ABC12  ', 'abc34', 'AbC37', 'beb12', 'BSA151', 'BEB23']

# O código abaixo vai percorrer todos os elementos da lista de produtos, para cada
# elemento, irá passar a função personalizada de tratamento de texto onde nela, 
# será retirado os espaços entre as palavras, retirada qualquer espaço que possa
# ter nas frases e colocar todas as letras em minúsculas.
for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)

# Impressão da lista atualizada de produtos
print('Lista de produtos atualizada utilizando o for:\n{}'.format(produtos))

print()

# abaixo, faremos o mesmo acima, porem, útilizando a programação funcional e a
# função map

# Criação de uma nova lista de produtos, com os mesmos problemas de padronização
# contida no primeiro exemplo
produtos_2 = ['  ABC12  ', 'abc34', 'AbC37', 'beb12', 'BSA151', 'BEB23']

# Passamos como argumento para o map, primeiro a função que desejamos utilizar em
# todos os elementos da lista, depois, a lista que deverá ser tratada.

# Map é uma função do Python que percorrerá todos os elementos de um interavel e
# realizará uma ação definição pela função passada em seu argumento

# O retorno do map não pode ser útilizado diretamente, sendo necessário conversão
# para o tipo interavel que você deseja trabalhar, neste caso, convertemos o map
# para a lista, por isso, a utilização do list passando o map em seu argumento

produtos_2 = list(map(padronizar_texto, produtos_2))
print('Lista de produtos atulizada usando a função map:\n{}'.format(produtos_2))

# Abaixo, apenas uma demonstrção do que o map retorna caso não seja convertido
print()

produto_3 = map(padronizar_texto, produtos_2)
print('Demostração do tipo de retorno do map: {}'.format(type(produto_3)))

print()

# Uma observação importante é sobre o uso do sort ou do sorted como função para uma
# expressão lambda, até agora no programa, usamos várias vezes a função .sort() para
# ordenar listas. Mas o método sort tem um parâmetro que nunca usamos e que agora,
# com o uso das expressões lambdas, sera útil.

produtos = [
    'apple tv', 'mac', 'Iphone x', 'iphone 11', 'ipad', 'apple wathc', 'mac book',
    'airport', 'xbox series x', 'playstation 5', 'guitarra cort', 'amp marshall'
]

# A ordenação do comando .sort() não representa que ele colocará em ordem alfabética,
# na verdade ele utilzia a tabla 'ASCII' para realizara sua ordenação, ela nada mais
# é do que código que representam a ordem em que as letras serão consideradas para a
# ordenação, nesta tabela, tem prioridades ao números, em segundo lugar as letras 
# maiúsculas pra só depois as letras minúsculas. Sendo assim, a palavra 'Camelo' seria
# inserida na frente da palavra 'anaconta'. Sendo assim analisado, precisamos tratar
# todos os elementos da lista deixando todos eles com letras minusculas ou maiusculas,
# deixando assim, possível realizar a ordenação dos valres da lista devidamente em 
# ordenação alfabética

# Abaixo, passamos como parâmetro para a função sort, a chave "KEY" recebendo a
# função str.casefold, que passa todas as palavras para letras minúsculas.
produtos.sort(key=str.casefold)
print('Nova lista de produtos {}'.format(produtos))

print()

venda_produtos = {
    'vinho' : 100,
    'vafeteira': 150,
    'microondas': 300,
    'iphone': 5500
}

# Abaixo, retornamos a variavel uma tupla de cada elemento do dicinoário
def segund_item(args):
    return args[1]

lista_vendas = list(venda_produtos.items())

# Para realizar a ordenação em um dicionário, primeiro deveremos converte-lo conforme
# código acima, para uma lista de tuplas onde, cada elemento chave valor do
# dicionário será uma tupla.

# Foi criada uma função que básicamente retorna o elemento 1 da tupla, neste caso, 
# foi retornado o valor de venda, já que a chave seria o nome do produto.

# No código abaixo é passado a função que criamos no parâmetro do .sort() com
# o adicional de reverse=True, que ordena a lista do maior para o menor, ou, em 
# outras palavras, de trás pra frente.

lista_vendas.sort(key=segund_item, reverse=True)

print(dict(lista_vendas))