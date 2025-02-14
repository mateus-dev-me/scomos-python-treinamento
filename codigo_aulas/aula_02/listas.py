# Criando uma lista de exemplo
frutas = ["maçã", "banana", "laranja", "uva", "kiwi"]

# Acessando elementos por índice
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Adicionando elementos com append()
frutas.append("morango")
print("\nLista após append:", frutas)

# Inserindo um elemento em um índice específico com insert()
frutas.insert(2, "abacaxi")
print("\nLista após insert:", frutas)

# Removendo um elemento pelo valor com remove()
frutas.remove("banana")
print("\nLista após remove:", frutas)

# Removendo e retornando o último item com pop()
ultima_fruta = frutas.pop()
print("\nÚltima fruta removida:", ultima_fruta)
print("Lista após pop:", frutas)

# Usando pop() para remover um item pelo índice
fruta_removida = frutas.pop(1)
print("\nFruta removida pelo índice:", fruta_removida)
print("Lista após pop com índice:", frutas)

# Ordenando a lista com sort()
frutas.sort()
print("\nLista ordenada:", frutas)

# Invertendo a lista com reverse()
frutas.reverse()
print("\nLista invertida:", frutas)

# Encontrando o índice de um item com index()
indice = frutas.index("kiwi")
print("\nÍndice da 'kiwi':", indice)

# Verificando se um item está na lista com in
if "maçã" in frutas:
    print("\nA maçã está na lista.")

# Contando quantas vezes um item aparece com count()
quantidade = frutas.count("uva")
print("\nQuantidade de uvas na lista:", quantidade)

# Calculando o tamanho da lista com len()
tamanho = len(frutas)
print("\nTamanho da lista:", tamanho)

# Criando uma nova lista com elementos modificados usando list comprehension
novas_frutas = [fruta.upper() for fruta in frutas]
print("\nLista com frutas em maiúsculo:", novas_frutas)

# Unindo duas listas com extend()
outras_frutas = ["melancia", "cabeludo"]
frutas.extend(outras_frutas)
print("\nLista após extend:", frutas)

# Criando uma cópia da lista com copy()
frutas_copy = frutas.copy()
print("\nCópia da lista:", frutas_copy)

# Limpando a lista com clear()
frutas.clear()
print("\nLista após clear:", frutas)

