-- Criação da tabela principal de clientes
CREATE TABLE cliente (
  cliente_id INT PRIMARY KEY,
  nome VARCHAR2(50),
  email VARCHAR2(50),
  senha VARCHAR(20),
  celular char(11),
  endereco VARCHAR(70)
);

-- Criação da tabela de clientes pessoa física
CREATE TABLE usuario (
  cliente_id INT PRIMARY KEY,
  cpf char(11),
  nascimento varchar2(8),
  FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

-- Criação da tabela de instituições (clientes pessoa jurídica)
CREATE TABLE instituicoes (
  cliente_id INT PRIMARY KEY,
  cnpj char(14),
  FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

-- Selecionar todos os registros da tabela "cliente"
SELECT * FROM cliente;

-- Selecionar todos os registros da tabela "usuario"
SELECT * FROM usuario;

-- Selecionar todos os registros da tabela "instituicoes"
SELECT * FROM instituicoes;

-- Remoção da tabela de usuários pessoa física
DROP TABLE cliente;

-- Remoção da tabela de usuários pessoa jurídica
DROP TABLE usuario;

-- Remoção da tabela principal de usuários
DROP TABLE instituicoes;

commit;

