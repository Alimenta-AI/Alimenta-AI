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
  validade DATE,
  quantidade NUMBER(10, 2) NOT NULL,
  clienteId CHAR(20) NOT NULL,
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

--Insert cliente--
INSERT INTO cliente VALUES ('João Silva', 'joao.silva@email.com', 'senha123', '9876543210', 'Rua A, 123', 'CLT001', 0);
INSERT INTO cliente VALUES ('Maria Santos', 'maria.santos@email.com', 'senha456', '9876543211', 'Rua B, 456', 'CLT002', 1);
INSERT INTO cliente VALUES ('Pedro Almeida', 'pedro.almeida@email.com', 'senha789', '9876543212', 'Rua C, 789', 'CLT003', 1);
INSERT INTO cliente VALUES ('Ana Oliveira', 'ana.oliveira@email.com', 'senhaabc', '9876543213', 'Rua D, 321', 'CLT004', 1);
INSERT INTO cliente VALUES ('Carlos Pereira', 'carlos.pereira@email.com', 'senhaxyz', '9876543214', 'Rua E, 654', 'CLT005', 1);
INSERT INTO cliente VALUES ('Laura Costa', 'laura.costa@email.com', 'senha123', '9876543215', 'Rua F, 987', 'CLT006', 0);
INSERT INTO cliente VALUES ('Fernando Santos', 'fernando.santos@email.com', 'senha456', '9876543216', 'Rua G, 654', 'CLT007', 1);
INSERT INTO cliente VALUES ('Camila Ribeiro', 'camila.ribeiro@email.com', 'senha789', '9876543217', 'Rua H, 321', 'CLT008', 1);
INSERT INTO cliente VALUES ('Rafaela Lima', 'rafaela.lima@email.com', 'senhaabc', '9876543218', 'Rua I, 654', 'CLT009', 0);
INSERT INTO cliente VALUES ('Marcos Oliveira', 'marcos.oliveira@email.com', 'senhaxyz', '9876543219', 'Rua J, 321', 'CLT010', 1);

--Insert usuario--
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

--Insert instituição--
INSERT INTO instituicao VALUES ('CLT001', '12345678901234');
INSERT INTO instituicao VALUES ('CLT002', '23456789012345');
INSERT INTO instituicao VALUES ('CLT003', '34567890123456');
INSERT INTO instituicao VALUES ('CLT004', '45678901234567');
INSERT INTO instituicao VALUES ('CLT005', '56789012345678');
INSERT INTO instituicao VALUES ('CLT006', '67890123456789');
INSERT INTO instituicao VALUES ('CLT007', '78901234567890');
INSERT INTO instituicao VALUES ('CLT008', '89012345678901');
INSERT INTO instituicao VALUES ('CLT009', '90123456789012');
INSERT INTO instituicao VALUES ('CLT010', '01234567890123');

--Insert alimento--
INSERT INTO alimento VALUES ('ALM001', 'Maçã','29/MAR/2003', 10, 'CLT001');
INSERT INTO alimento VALUES ('ALM002', 'Arroz, 31/DEC/2024', 5, 'CLT002');
INSERT INTO alimento VALUES ('ALM003', 'Feijão', '15/SEP/2023', 7, 'CLT003');
INSERT INTO alimento VALUES ('ALM004', 'Frango', '30/JUN/2023', 2, 'CLT004');
INSERT INTO alimento VALUES ('ALM005', 'Pão de Forma' , '31/MAY/2023', 3, 'CLT005');
INSERT INTO alimento VALUES ('ALM006', 'Leite','30/JUN/2023', 4, 'CLT006');
INSERT INTO alimento VALUES ('ALM007', 'Cenoura','28/MAY/2023', 6, 'CLT007');
INSERT INTO alimento VALUES ('ALM008', 'Banana','15/JUN/2023', 8, 'CLT008');
INSERT INTO alimento VALUES ('ALM009', 'Tomate','29/MAY/2023',3, 'CLT009');
INSERT INTO alimento VALUES ('ALM010', 'Biscoito','31/JUL/2023', 5, 'CLT010');