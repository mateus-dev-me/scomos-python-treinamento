import os
from sqlalchemy import create_engine, text
import pandas as pd

# Criando a URL de conexão
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///database.db')
engine = create_engine(DATABASE_URL)

# Função para buscar produtos do banco de dados
def fetch_products():
    """
    Conecta ao banco de dados, executa uma consulta SQL para buscar todos os produtos,
    converte os resultados em um DataFrame Pandas e retorna os dados.
    """
    try:
        with engine.connect() as conn:
            query = text("SELECT * FROM produtos")
            result = conn.execute(query)
            
            # Covertendo os resultados para um DataFrame Pandas
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
    except Exception as e:
        print(f"Erro ao buscar produtos: {e}")
        return None

if __name__ == "__main__":
    # Executando a consulta e exibindo os resultados
    df_produtos = fetch_products()
    if df_produtos is not None:
        print("Produtos disponíveis no banco de dados:")
        print(df_produtos.head())  # Mostra as primeiras linhas do DataFrame
    else:
        print("Nenhum dado retornado.")

