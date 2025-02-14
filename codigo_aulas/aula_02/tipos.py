# Trabalhando com inteiros (int)
numero_inteiro = 42
print("Número inteiro:", numero_inteiro)
print("Tipo de número inteiro:", type(numero_inteiro))

# Operações com inteiros
soma_inteiros = numero_inteiro + 8
subtracao_inteiros = numero_inteiro - 10
multiplicacao_inteiros = numero_inteiro * 2
divisao_inteiros = numero_inteiro / 5  # Retorna float
divisao_inteiros_inteiro = numero_inteiro // 5  # Divisão inteira
modulo_inteiros = numero_inteiro % 5  # Resto da divisão

print("\nOperações com inteiros:")
print(f"Soma: {soma_inteiros}, Subtração: {subtracao_inteiros}, Multiplicação: {multiplicacao_inteiros}")
print(f"Divisão (float): {divisao_inteiros}, Divisão inteira: {divisao_inteiros_inteiro}, Módulo: {modulo_inteiros}")

# Trabalhando com números de ponto flutuante (float)
numero_float = 3.14159
print("\nNúmero de ponto flutuante:", numero_float)
print("Tipo de número float:", type(numero_float))

# Operações com float
soma_float = numero_float + 2.5
produto_float = numero_float * 2
divisao_float = numero_float / 2

print("\nOperações com floats:")
print(f"Soma: {soma_float}, Produto: {produto_float}, Divisão: {divisao_float}")

# Trabalhando com strings (str)
nome = "Mateus"
sobrenome = "Martins"
print("\nNome completo:", nome + " " + sobrenome)

# Manipulação de strings
nome_completo = nome + " " + sobrenome
comprimento_nome = len(nome_completo)
primeira_letra = nome[0]

print("\nManipulação de strings:")
print(f"Nome completo: {nome_completo}, Comprimento: {comprimento_nome}, Primeira letra: {primeira_letra}")

# Métodos de string
nome_em_maiusculo = nome.upper()
nome_em_minusculo = nome.lower()

print("\nMétodos de string:")
print(f"Nome em maiúsculo: {nome_em_maiusculo}, Nome em minúsculo: {nome_em_minusculo}")

# Trabalhando com valores booleanos (bool)
eh_maior_de_idade = True
tem_ano_de_experiencia = False

print("\nValores booleanos:")
print(f"É maior de idade? {eh_maior_de_idade}")
print(f"Tem ano de experiência? {tem_ano_de_experiencia}")

# Usando booleanos em operações lógicas
maior_que_18 = numero_inteiro > 18
experiencia_ou_idade = eh_maior_de_idade or tem_ano_de_experiencia

print("\nOperações com booleanos:")
print(f"Maior que 18? {maior_que_18}, Maior de idade ou experiência? {experiencia_ou_idade}")

# Convertendo tipos
numero_convertido = float(numero_inteiro)  # Convertendo int para float
texto_convertido = str(numero_inteiro)     # Convertendo int para str
booleano_convertido = bool(numero_inteiro) # Convertendo int para bool (0 é False, outros são True)

print("\nConversão de tipos:")
print(f"Conversão de int para float: {numero_convertido}, int para str: {texto_convertido}, int para bool: {booleano_convertido}")

