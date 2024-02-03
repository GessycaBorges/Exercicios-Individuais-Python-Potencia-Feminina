import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# Insira pelo menos 5 registros de alunos na tabela anterior.
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Ana", 23, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "João", 26, "Nutrição")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Maria", 21, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "José", 28, "Ciências da Computação")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Marta", 25, "Direito")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Renato", 19, "Nutrição")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Alana", 20, "Engenharia")')

# Consultas Básicas
# a) Selecionar todos os registros da tabela "alunos".
# dados = cursor.execute('SELECT * FROM alunos')
# for aluno in dados:
#     print(aluno)
# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# for aluno in dados:
#     print(aluno)
# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
# for aluno in dados:
#     print(aluno)
# d) Contar o número total de alunos na tabela.
# contar = cursor.execute('SELECT COUNT(*) FROM alunos')
# print(contar.fetchone()[0])

# Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
# cursor.execute('UPDATE alunos SET idade = 20 WHERE id = 3')
# b) Remova um aluno pelo seu ID.
# cursor.execute('DELETE FROM alunos where id = 4')

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Ana", 23, 874.98)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "João", 26, 1365.36)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Maria", 31, 1489.75)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "José", 28, 1598.75)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Marta", 35, 975.42)')

# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# for cliente in dados:
#     print(cliente)
# b) Calcule o saldo médio dos clientes.
# saldo = cursor.execute('SELECT AVG(saldo) FROM clientes')
# print(saldo.fetchone()[0])
# c) Encontre o cliente com o saldo máximo.
# maximo = cursor.execute('SELECT MAX(saldo) FROM clientes')
# print(maximo.fetchone()[0])
# d) Conte quantos clientes têm saldo acima de 1000.
# contar = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
# print(contar.fetchone()[0])

# Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
# cursor.execute('UPDATE clientes SET saldo = 1320.56 WHERE id = 3')
# b) Remova um cliente pelo seu ID.
# cursor.execute('DELETE FROM clientes where id = 5')

# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
# cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')
# Insira algumas compras associadas a clientes existentes na tabela "clientes".
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Calça Jeans", 149.99)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 1, "Tênis", 145.90)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 4, "Camiseta", 49.99)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 3, "Cinto", 39.90)')
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
dados = cursor.execute('SELECT cli.nome, com.produto, com.valor FROM compras com INNER JOIN clientes cli ON com.cliente_id = cli.id')
for compra in dados:
    print(compra)

# dados = cursor.execute('SELECT * FROM compras')
# for item in dados:
#     print(item)

conexao.commit()
conexao.close()