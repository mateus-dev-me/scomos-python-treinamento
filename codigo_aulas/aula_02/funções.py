# Função simples sem parâmetros e sem retorno
def saudacao():
    print("Olá, bem-vindo ao mundo Python!")

# Chamando a função simples
saudacao()

# Função com parâmetros
def saudacao_personalizada(nome: str, idade: int) -> None:
    print(f"Olá {nome}, você tem {idade} anos!")

# Chamando a função com parâmetros
saudacao_personalizada("Mateus", 28)

# Função com valor de retorno
def soma(a: int, b: int) -> int:
    return a + b

# Chamando a função com retorno
resultado = soma(5, 3)
print(f"Soma de 5 e 3 é: {resultado}")

# Função com valor de retorno e valores padrão
def saudacao_anonima(nome: str = "Usuário") -> str:
    return f"Olá, {nome}!"

# Chamando a função com e sem parâmetro
print(saudacao_anonima())
print(saudacao_anonima("Mateus"))

# Função com número variável de argumentos (usando *args)
def listar_numeros(*numeros: int) -> None:
    print("Números fornecidos:", numeros)

# Chamando a função com número variável de argumentos
listar_numeros(1, 2, 3, 4, 5)

# Função com parâmetros nomeados (usando **kwargs)
def detalhes_usuario(**dados) -> None:
    print("Detalhes do usuário:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

# Chamando a função com parâmetros nomeados
detalhes_usuario(nome="Mateus", idade=28, profissao="Desenvolvedor")

# Função recursiva para calcular fatorial
def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Chamando a função recursiva
print(f"Fatorial de 5 é: {fatorial(5)}")

# Função lambda (função anônima)
quadrado = lambda x: x ** 2

# Chamando a função lambda
print(f"Quadrado de 4 é: {quadrado(4)}")

# Função que utiliza valores de referência e cópias (modificando listas)
def adicionar_elemento(lista: list, elemento: int) -> None:
    lista.append(elemento)
    print(f"Lista após adicionar elemento: {lista}")

# Chamando a função que modifica a lista
minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista, 4)
print("Lista final:", minha_lista)

