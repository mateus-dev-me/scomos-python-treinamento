# Criando um dicionário de exemplo
usuario = {
    "nome": "Mateus",
    "idade": 28,
    "profissao": "Desenvolvedor Backend",
    "linguagens": ["Python", "Go", "JavaScript"]
}

# Usando o método keys() para obter todas as chaves
print("Chaves do dicionário:", list(usuario.keys()))

# Usando o método values() para obter todos os valores
print("Valores do dicionário:", list(usuario.values()))

# Usando o método items() para obter chave-valor
print("\nPares chave-valor:")
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# Usando get() para acessar valores sem gerar erro
print("\nE-mail:", usuario.get("email", "Não informado"))

# Usando setdefault() para definir um valor padrão caso a chave não exista
usuario.setdefault("email", "mateus@email.com")
print("E-mail atualizado:", usuario["email"])

# Atualizando múltiplos valores com update()
usuario.update({"idade": 29, "cidade": "São Paulo"})
print("\nDicionário atualizado:", usuario)

# Copiando um dicionário com copy()
copia_usuario = usuario.copy()
print("\nCópia do dicionário:", copia_usuario)

# Removendo um item com pop()
profissao = usuario.pop("profissao")
print(f"\nProfissão removida: {profissao}")
print("Dicionário após remoção:", usuario)

# Removendo o último item com popitem()
ultimo_item = usuario.popitem()
print(f"\nÚltimo item removido: {ultimo_item}")
print("Dicionário após popitem:", usuario)

# Limpando o dicionário com clear()
usuario.clear()
print("\nDicionário após clear():", usuario)

