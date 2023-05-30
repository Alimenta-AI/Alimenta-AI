CREATE TABLE cliente (
  clienteId CHAR(20) PRIMARY KEY,
  nome VARCHAR2(50) NOT NULL,
  email VARCHAR2(50) UNIQUE NOT NULL,
  senha VARCHAR2(20) NOT NULL,
  celular CHAR(11) UNIQUE NOT NULL,
  endereco VARCHAR2(200) NOT NULL,
  tipoCliente NUMBER(1) NOT NULL
);

CREATE TABLE usuario (
  clienteId CHAR(20) PRIMARY KEY,
  cpf CHAR(11) UNIQUE NOT NULL,
  nascimento VARCHAR2(8) NOT NULL,
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE instituicao (
  clienteId CHAR(20) PRIMARY KEY,
  website VARCHAR2(150),
  tipo VARCHAR2(15),
  cnpj CHAR(14) UNIQUE NOT NULL,
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE alimento (
  alimentoId CHAR(20) PRIMARY KEY,
  nome VARCHAR2(50) NOT NULL,
  validade varchar2(6),
  quantidade NUMBER(10) NOT NULL,
  clienteId CHAR(20) NOT NULL,
  CONSTRAINT fk_cliente_clienteId FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE movimentacao (
  clienteIdUsuario CHAR(20),
  clienteIdInstituicao CHAR(20),
  num_solicitacao CHAR(10) PRIMARY KEY,
  data_movimentacao VARCHAR2(8) NOT NULL,
  descricao VARCHAR2(150) NOT NULL,
  categoria VARCHAR2(20) NOT NULL,
  FOREIGN KEY (clienteIdUsuario) REFERENCES cliente(clienteId),
  FOREIGN KEY (clienteIdInstituicao) REFERENCES cliente(clienteId)
);

CREATE TABLE alimento (
  alimentoId CHAR(20) PRIMARY KEY,
  nome VARCHAR2(50) NOT NULL,
  validade varchar2(6),
  quantidade NUMBER(10) NOT NULL,
  clienteId CHAR(20) NOT NULL,
  CONSTRAINT fk_cliente_clienteId FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

-- Inserts cliente
INSERT INTO cliente VALUES ('CLT001', 'João Silva', 'joao.silva@email.com', 'senha123', '9876543210', 'Rua A, 123', 0);
INSERT INTO cliente VALUES ('CLT002', 'Maria Santos', 'maria.santos@email.com', 'senha456', '9876543211', 'Rua B, 456', 1);
INSERT INTO cliente VALUES ('CLT003', 'Pedro Almeida', 'pedro.almeida@email.com', 'senha789', '9876543212', 'Rua C, 789', 1);
INSERT INTO cliente VALUES ('CLT004', 'Ana Oliveira', 'ana.oliveira@email.com', 'senhaabc', '9876543213', 'Rua D, 321', 1);
INSERT INTO cliente VALUES ('CLT005', 'Carlos Pereira', 'carlos.pereira@email.com', 'senhaxyz', '9876543214', 'Rua E, 654', 1);
INSERT INTO cliente VALUES ('CLT006', 'Laura Costa', 'laura.costa@email.com', 'senha123', '9876543215', 'Rua F, 987', 0);
INSERT INTO cliente VALUES ('CLT007', 'Fernando Santos', 'fernando.santos@email.com', 'senha456', '9876543216', 'Rua G, 654', 1);
INSERT INTO cliente VALUES ('CLT008', 'Camila Ribeiro', 'camila.ribeiro@email.com', 'senha789', '9876543217', 'Rua H, 321', 1);
INSERT INTO cliente VALUES ('CLT009', 'Rafaela Lima', 'rafaela.lima@email.com', 'senhaabc', '9876543218', 'Rua I, 654', 0);
INSERT INTO cliente VALUES ('CLT010', 'Marcos Oliveira', 'marcos.oliveira@email.com', 'senhaxyz', '9876543219', 'Rua J, 321', 1);

-- Inserts usuario
INSERT INTO usuario VALUES ('CLT001', '12345678901', '20000101');
INSERT INTO usuario VALUES ('CLT002', '23456789012', '20010202');
INSERT INTO usuario VALUES ('CLT003', '34567890123', '20020303');
INSERT INTO usuario VALUES ('CLT004', '45678901234', '20030404');
INSERT INTO usuario VALUES ('CLT005', '56789012345', '20040505');
INSERT INTO usuario VALUES ('CLT006', '67890123456', '20050606');
INSERT INTO usuario VALUES ('CLT007', '78901234567', '20060707');
INSERT INTO usuario VALUES ('CLT008', '89012345678', '20070808');
INSERT INTO usuario VALUES ('CLT009', '90123456789', '20080909');
INSERT INTO usuario VALUES ('CLT010', '01234567890', '20091010');

-- Inserts instituicao --
INSERT INTO instituicao VALUES ('CLT001', 'www.instituicao1.com', 'Tipo 1', '12345678901234');
INSERT INTO instituicao VALUES ('CLT002', 'www.instituicao2.com', 'Tipo 2', '23456789012345');
INSERT INTO instituicao VALUES ('CLT003', 'www.instituicao3.com', 'Tipo 1', '34567890123456');
INSERT INTO instituicao VALUES ('CLT004', 'www.instituicao4.com', 'Tipo 3', '45678901234567');
INSERT INTO instituicao VALUES ('CLT005', 'www.instituicao5.com', 'Tipo 2', '56789012345678');
INSERT INTO instituicao VALUES ('CLT006', 'www.instituicao6.com', 'Tipo 1', '67890123456789');
INSERT INTO instituicao VALUES ('CLT007', 'www.instituicao7.com', 'Tipo 3', '78901234567890');
INSERT INTO instituicao VALUES ('CLT008', 'www.instituicao8.com', 'Tipo 2', '89012345678901');
INSERT INTO instituicao VALUES ('CLT009', 'www.instituicao9.com', 'Tipo 1', '90123456789012');
INSERT INTO instituicao VALUES ('CLT010', 'www.instituicao10.com', 'Tipo 3', '01234567890123');

-- Inserts movimentacao --
INSERT INTO movimentacao VALUES ('CLT001', 'CLT002', 'SOL001', '20230529', 'Solicitação 1', 'Categoria 1');
INSERT INTO movimentacao VALUES ('CLT002', 'CLT003', 'SOL002', '20230528', 'Solicitação 2', 'Categoria 2');
INSERT INTO movimentacao VALUES ('CLT003', 'CLT004', 'SOL003', '20230527', 'Solicitação 3', 'Categoria 1');
INSERT INTO movimentacao VALUES ('CLT004', 'CLT005', 'SOL004', '20230526', 'Solicitação 4', 'Categoria 3');
INSERT INTO movimentacao VALUES ('CLT005', 'CLT006', 'SOL005', '20230525', 'Solicitação 5', 'Categoria 2');
INSERT INTO movimentacao VALUES ('CLT006', 'CLT007', 'SOL006', '20230524', 'Solicitação 6', 'Categoria 1');
INSERT INTO movimentacao VALUES ('CLT007', 'CLT008', 'SOL007', '20230523', 'Solicitação 7', 'Categoria 3');
INSERT INTO movimentacao VALUES ('CLT008', 'CLT009', 'SOL008', '20230522', 'Solicitação 8', 'Categoria 2');
INSERT INTO movimentacao VALUES ('CLT009', 'CLT010', 'SOL009', '20230521', 'Solicitação 9', 'Categoria 1');
INSERT INTO movimentacao VALUES ('CLT010', 'CLT001', 'SOL010', '20230520', 'Solicitação 10', 'Categoria 3');

INSERT INTO alimento VALUES ('ALM001', 'Maçã', '230329', 10, 'CLT001');
INSERT INTO alimento VALUES ('ALM002', 'Arroz', '241224', 5, 'CLT002');
INSERT INTO alimento VALUES ('ALM003', 'Feijão', '150923', 7, 'CLT003');
INSERT INTO alimento VALUES ('ALM004', 'Frango', '010122', 2, 'CLT004');
INSERT INTO alimento VALUES ('ALM005', 'Pão de Forma', '310523', 3, 'CLT005');
INSERT INTO alimento VALUES ('ALM006', 'Leite', '010623', 4, 'CLT006');
INSERT INTO alimento VALUES ('ALM007', 'Cenoura', '280523', 6, 'CLT007');
INSERT INTO alimento VALUES ('ALM008', 'Banana', '010723', 8, 'CLT008');
INSERT INTO alimento VALUES ('ALM009', 'Tomate', '290523', 3, 'CLT009');
INSERT INTO alimento VALUES ('ALM010', 'Biscoito', '310723', 5, 'CLT010');



DROP TABLE usuario;
DROP TABLE cliente;
DROP TABLE instituicao;
DROP TABLE movimentacao;
drop table alimento;

SELECT * FROM cliente;
SELECT * FROM usuario;
select * from alimento;
SELECT * FROM instituicao;
SELECT * FROM movimentacao;


commit;