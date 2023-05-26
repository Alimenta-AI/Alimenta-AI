CREATE TABLE cliente (
    nome varchar2(50) NOT NULL,
    email varchar2(50) UNIQUE NOT NULL,
    senha varchar2(20) NOT NULL,
    celular CHAR(11) UNIQUE NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    clienteId CHAR(20) PRIMARY KEY,
    tipoCliente NUMBER(1) NOT NULL
);

CREATE TABLE usuario (
  clienteId CHAR(20) PRIMARY KEY, 
  cpf CHAR(11) UNIQUE NOT NULL,
  nascimento varchar2(8) NOT NULL, --DDmmYYYY
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE instituicao (
  clienteId CHAR(20) PRIMARY KEY,
  cnpj CHAR(14) UNIQUE NOT NULL,
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE alimento (
  alimentoId CHAR(20) PRIMARY KEY,
  nome VARCHAR2(50) NOT NULL,
  descricao VARCHAR2(200),
  validade DATE,
  quantidade NUMBER(10, 2) NOT NULL,
  clienteId CHAR(20) NOT NULL,
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);



