-- Cria��o da tabela principal de clientes
CREATE TABLE cliente (
  cliente_id INT PRIMARY KEY,
  nome VARCHAR2(50),
  email VARCHAR2(50),
  senha VARCHAR(20),
  celular char(11),
  endereco VARCHAR(70)
);

-- Cria��o da tabela de clientes pessoa f�sica
CREATE TABLE usuario (
  cliente_id INT PRIMARY KEY,
  cpf char(11),
  nascimento varchar2(8),
  FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

-- Cria��o da tabela de institui��es (clientes pessoa jur�dica)
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

-- Remo��o da tabela de usu�rios pessoa f�sica
DROP TABLE cliente;

-- Remo��o da tabela de usu�rios pessoa jur�dica
DROP TABLE usuario;

-- Remo��o da tabela principal de usu�rios
DROP TABLE instituicoes;

commit;

