# Criando uma tupla de exemplo
frutas = ("maçã", "banana", "laranja", "uva", "kiwi")

# Acessando elementos por índice
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Desempacotando a tupla
fruta1, fruta2, fruta3, fruta4, fruta5 = frutas
print("\nDesempacotando a tupla:")
print(f"Fruta 1: {fruta1}, Fruta 2: {fruta2}, Fruta 3: {fruta3}, Fruta 4: {fruta4}, Fruta 5: {fruta5}")

# Contando o número de vezes que um item aparece com count()
quantidade = frutas.count("uva")
print("\nQuantidade de uvas na tupla:", quantidade)

# Encontrando o índice de um item com index()
indice = frutas.index("kiwi")
print("\nÍndice da 'kiwi':", indice)

# Verificando se um item está na tupla
if "maçã" in frutas:
    print("\nA maçã está na tupla.")

# Tupla com um único item
tupla_unica = (42,)  # Note a vírgula para diferenciar de um valor entre parênteses
print("\nTupla com um único item:", tupla_unica)

# Concatenação de tuplas
novas_frutas = frutas + ("morango", "melancia")
print("\nTupla após concatenação:", novas_frutas)

# Repetindo uma tupla
tupla_repetida = frutas * 2
print("\nTupla após repetição:", tupla_repetida)

# Obtendo o tamanho de uma tupla com len()
tamanho = len(frutas)
print("\nTamanho da tupla:", tamanho)

# Convertendo tupla em lista
frutas_lista = list(frutas)
print("\nTupla convertida para lista:", frutas_lista)

# Convertendo lista em tupla
lista_frutas = ["maçã", "abacaxi", "pêssego"]
nova_tupla = tuple(lista_frutas)
print("\nLista convertida para tupla:", nova_tupla)

