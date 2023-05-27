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

--Inserts cliente--
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

--Inserts alimento--
INSERT INTO alimento VALUES ('ALM001', 'Maçã', TO_DATE('29/03/2003', 'DD/MM/YYYY'), 10, 'CLT001');
INSERT INTO alimento VALUES ('ALM002', 'Arroz', TO_DATE('31/12/2024', 'DD/MM/YYYY'), 5, 'CLT002');
INSERT INTO alimento VALUES ('ALM003', 'Feijão', TO_DATE('15/09/2023', 'DD/MM/YYYY'), 7, 'CLT003');
INSERT INTO alimento VALUES ('ALM004', 'Frango', TO_DATE('01/01/2022', 'DD/MM/YYYY'), 2, 'CLT004');
INSERT INTO alimento VALUES ('ALM005', 'Pão de Forma', TO_DATE('31/05/2023', 'DD/MM/YYYY'), 3, 'CLT005');
INSERT INTO alimento VALUES ('ALM006', 'Leite', TO_DATE('01/06/2023', 'DD/MM/YYYY'), 4, 'CLT006');
INSERT INTO alimento VALUES ('ALM007', 'Cenoura', TO_DATE('28/05/2023', 'DD/MM/YYYY'), 6, 'CLT007');
INSERT INTO alimento VALUES ('ALM008', 'Banana', TO_DATE('01/07/2023', 'DD/MM/YYYY'), 8, 'CLT008');
INSERT INTO alimento VALUES ('ALM009', 'Tomate', TO_DATE('29/05/2023', 'DD/MM/YYYY'), 3, 'CLT009');
INSERT INTO alimento VALUES ('ALM010', 'Biscoito', TO_DATE('31/07/2023', 'DD/MM/YYYY'), 5, 'CLT010');

--clientes que possuem tipoCliente igual 1--
SELECT nome, email, endereco FROM cliente WHERE tipoCliente = 1 ORDER BY nome;

--alimentos (nome, validade) e seus respectivos clientes (nome) para alimentos com quantidade maior que 5.--
SELECT alimento.nome, alimento.validade, cliente.nome
FROM alimento
JOIN cliente ON alimento.clienteId = cliente.clienteId
WHERE alimento.quantidade > 5
ORDER BY alimento.validade;

--Obter a contagem de alimentos por tipo de cliente--
SELECT cliente.tipoCliente, COUNT(*) quantidade_alimentos
FROM alimento
JOIN cliente ON alimento.clienteId = cliente.clienteId
GROUP BY cliente.tipoCliente;

--Obter a média de quantidade de alimentos por tipo de cliente, considerando apenas os clientes que possuem mais de 3 alimentos.--
SELECT cliente.tipoCliente, AVG(alimento.quantidade) media_alimentos
FROM alimento
JOIN cliente ON alimento.clienteId = cliente.clienteId
GROUP BY cliente.tipoCliente
HAVING COUNT(*) > 3;

commit;