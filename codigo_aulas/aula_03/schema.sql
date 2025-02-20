CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

INSERT INTO produtos (nome, descricao, preco, quantidade, categoria) VALUES
('Notebook', 'Notebook com processador i7 e 16GB RAM', 4500.00, 10, 'Eletrônicos'),
('Smartphone', 'Smartphone com 128GB de armazenamento', 2500.00, 20, 'Eletrônicos'),
('Cadeira Gamer', 'Cadeira ergonômica para jogos', 1200.00, 5, 'Móveis'),
('Monitor', 'Monitor LED 27 polegadas', 1300.00, 8, 'Eletrônicos'),
('Teclado Mecânico', 'Teclado mecânico RGB', 350.00, 15, 'Periféricos');
