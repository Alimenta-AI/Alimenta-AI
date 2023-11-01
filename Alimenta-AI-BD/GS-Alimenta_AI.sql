CREATE TABLE cliente (
  clienteId CHAR(20) PRIMARY KEY,
  nome VARCHAR2(50) NOT NULL,
  email VARCHAR2(150) UNIQUE NOT NULL,
  senha VARCHAR2(20) NOT NULL,
  celular CHAR(11) UNIQUE NOT NULL,
  endereco VARCHAR2(200) NOT NULL,
  tipoCliente NUMBER(1) NOT NULL
);

CREATE TABLE usuario (
  cpf CHAR(11) UNIQUE NOT NULL,
  nascimento CHAR(8) NOT NULL,
  doador CHAR(3) NOT NULL,
  clienteId CHAR(20),
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE instituicao (
  website VARCHAR2(150),
  tipo VARCHAR2(15),
  cnpj CHAR(14) UNIQUE NOT NULL,
  clienteId CHAR(20),
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE estoque (
  estoqueId CHAR(20) PRIMARY KEY,
  tamanho NUMBER(4) NOT NULL, 
  clienteId CHAR(20) NOT NULL,
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE alimento (
  alimentoId CHAR(20) PRIMARY KEY,
  nome VARCHAR2(50) NOT NULL,
  validade CHAR(6), -- mmyyyy 
  quantidade NUMBER(10) NOT NULL,
  estoqueId CHAR(20) NOT NULL,  
  FOREIGN KEY (estoqueId) REFERENCES estoque(estoqueId)
);

CREATE TABLE movimentacao (
  clienteIdUsuario CHAR(20),
  clienteIdInstituicao CHAR(20),
  num_solicitacao VARCHAR2(10) PRIMARY KEY,
  data_movimentacao CHAR(12) NOT NULL,
  descricao VARCHAR2(150) NOT NULL,
  categoria VARCHAR2(20) NOT NULL,
  FOREIGN KEY (clienteIdUsuario) REFERENCES cliente(clienteId),
  FOREIGN KEY (clienteIdInstituicao) REFERENCES cliente(clienteId)
);

CREATE TABLE avaliacao (
  nota NUMBER(2) NOT NULL,
  dataAvaliacao CHAR(12),
  avaliacaoId CHAR(20) PRIMARY KEY,
  clienteId CHAR(20),
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

CREATE TABLE comentario(
  comentarioId CHAR(20) PRIMARY KEY,
  texto VARCHAR2(250) NOT NULL,
  dataComentario CHAR(12) NOT NULL,
  avaliacaoId CHAR(20),
  FOREIGN KEY (avaliacaoId) REFERENCES avaliacao(avaliacaoId)
);

CREATE TABLE reservaCliente (
  reservaId CHAR(20) PRIMARY KEY,
  checkIn CHAR(12) NOT NULL,
  dataReserva CHAR(12) NOT NULL,
  checkOut CHAR(12) NOT NULL,
  clienteId CHAR(20),
  FOREIGN KEY (clienteId) REFERENCES cliente(clienteId)
);

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

INSERT INTO usuario VALUES ('23445345545', '20014444', 'SIM', 'CLT001');
INSERT INTO usuario VALUES ('23456789012', '20010202', 'SIM', 'CLT002');
INSERT INTO usuario VALUES ('34567890123', '20020303', 'SIM', 'CLT003');
INSERT INTO usuario VALUES ('45678901234', '20030404', 'SIM', 'CLT004');
INSERT INTO usuario VALUES ('56789012345', '20040505', 'SIM', 'CLT005');
INSERT INTO usuario VALUES ('67890123456', '20050606', 'SIM', 'CLT006');
INSERT INTO usuario VALUES ('78901234567', '20060707', 'SIM', 'CLT007');
INSERT INTO usuario VALUES ('89012345678', '20070808', 'SIM', 'CLT008');
INSERT INTO usuario VALUES ('90123456789', '20080909', 'NAO', 'CLT009');
INSERT INTO usuario VALUES ('01234567890', '20091010', 'SIM', 'CLT010');

INSERT INTO instituicao VALUES ('www.instituicao1.com', 'ONG', '12345678901234', 'CLT001');
INSERT INTO instituicao VALUES ('www.instituicao2.com', 'ONG', '23456789012345', 'CLT002');
INSERT INTO instituicao VALUES ('www.instituicao3.com', 'Tipo 1', '34567890123456', 'CLT003');
INSERT INTO instituicao VALUES ('www.instituicao4.com', 'ONG', '45678901234567', 'CLT004');
INSERT INTO instituicao VALUES ('www.instituicao5.com', 'Tipo 2', '56789012345678', 'CLT005');
INSERT INTO instituicao VALUES ('www.instituicao6.com', 'Tipo 1', '67890123456789', 'CLT006');
INSERT INTO instituicao VALUES ('www.instituicao7.com', 'Tipo 3', '78901234567890', 'CLT007');
INSERT INTO instituicao VALUES ('www.instituicao8.com', 'Tipo 2', '89012345678901', 'CLT008');
INSERT INTO instituicao VALUES ('www.instituicao9.com', 'Tipo 1', '90123456789012', 'CLT009');
INSERT INTO instituicao VALUES ('www.instituicao10.com', 'Tipo 3', '01234567890123', 'CLT010');

INSERT INTO movimentacao VALUES ('CLT001', 'CLT002', 'SOL001', '20230529', 'Solicit01', 'Faz Doação');
INSERT INTO movimentacao VALUES ('CLT002', 'CLT003', 'SOL002', '20230528', 'Solicit02', 'Recebe Doação');
INSERT INTO movimentacao VALUES ('CLT003', 'CLT004', 'SOL003', '20230527', 'Solicit03', 'Faz Doação');
INSERT INTO movimentacao VALUES ('CLT004', 'CLT005', 'SOL004', '20230526', 'Solicit04', 'Recebe Doação');
INSERT INTO movimentacao VALUES ('CLT005', 'CLT006', 'SOL005', '20230525', 'Solicit05', 'Faz Doação');
INSERT INTO movimentacao VALUES ('CLT006', 'CLT007', 'SOL006', '20230524', 'Solicit06', 'Recebe Doação');
INSERT INTO movimentacao VALUES ('CLT007', 'CLT008', 'SOL007', '20230523', 'Solicit07', 'Faz Doação');
INSERT INTO movimentacao VALUES ('CLT008', 'CLT009', 'SOL008', '20230522', 'Solicit08', 'Faz Doação');
INSERT INTO movimentacao VALUES ('CLT009', 'CLT010', 'SOL009', '20230521', 'Solicit09', 'Recebe Doação');
INSERT INTO movimentacao VALUES ('CLT010', 'CLT001', 'SOL010', '20230520', 'Solicit10', 'Faz Doação');

INSERT INTO estoque VALUES ('EST001', 100, 'CLT001');
INSERT INTO estoque VALUES ('EST002', 200, 'CLT002');
INSERT INTO estoque VALUES ('EST003', 150, 'CLT003');
INSERT INTO estoque VALUES ('EST004', 120, 'CLT004');
INSERT INTO estoque VALUES ('EST005', 80,  'CLT005');
INSERT INTO estoque VALUES ('EST006', 250, 'CLT006');
INSERT INTO estoque VALUES ('EST007', 180, 'CLT007');
INSERT INTO estoque VALUES ('EST008', 300, 'CLT008');
INSERT INTO estoque VALUES ('EST009', 200, 'CLT009');
INSERT INTO estoque VALUES ('EST010', 150, 'CLT010');

INSERT INTO alimento VALUES ('ALM001', 'Ma��', '230329', 10, 'EST001');
INSERT INTO alimento VALUES ('ALM002', 'Arroz', '241224', 5, 'EST002');
INSERT INTO alimento VALUES ('ALM003', 'Feij�o', '150923', 7, 'EST003');
INSERT INTO alimento VALUES ('ALM004', 'Frango', '010122', 2, 'EST004');
INSERT INTO alimento VALUES ('ALM005', 'P�o', '311221', 15, 'EST005');
INSERT INTO alimento VALUES ('ALM006', 'Leite', '070322', 8, 'EST006');
INSERT INTO alimento VALUES ('ALM007', 'Batata', '230521', 12, 'EST007');
INSERT INTO alimento VALUES ('ALM008', 'Cenoura', '060124', 9, 'EST008');
INSERT INTO alimento VALUES ('ALM009', 'Tomate', '290723', 6, 'EST009');
INSERT INTO alimento VALUES ('ALM010', 'Cebola', '110326', 11, 'EST010');

INSERT INTO avaliacao VALUES (8, '20230501', 'AVA001', 'CLT001');
INSERT INTO avaliacao VALUES (9, '20230502', 'AVA002', 'CLT002');
INSERT INTO avaliacao VALUES (7, '20230503', 'AVA003', 'CLT003');
INSERT INTO avaliacao VALUES (6, '20230504', 'AVA004', 'CLT004');
INSERT INTO avaliacao VALUES (10, '20230505', 'AVA005', 'CLT005');
INSERT INTO avaliacao VALUES (9, '20230506', 'AVA006', 'CLT006');
INSERT INTO avaliacao VALUES (8, '20230507', 'AVA007', 'CLT007');
INSERT INTO avaliacao VALUES (7, '20230508', 'AVA008', 'CLT008');
INSERT INTO avaliacao VALUES (6, '20230509', 'AVA009', 'CLT009');
INSERT INTO avaliacao VALUES (9, '20230510', 'AVA010', 'CLT010');

INSERT INTO comentario VALUES ('COM001', '�timo servi�o!', '20230501', 'AVA001');
INSERT INTO comentario VALUES ('COM002', 'Excelente atendimento.', '20230502', 'AVA002');
INSERT INTO comentario VALUES ('COM003', 'Precisa melhorar a pontualidade.', '20230503', 'AVA003');
INSERT INTO comentario VALUES ('COM004', 'Gostei dos produtos oferecidos.', '20230504', 'AVA004');
INSERT INTO comentario VALUES ('COM005', 'Servi�o de alta qualidade.', '20230505', 'AVA005');
INSERT INTO comentario VALUES ('COM006', 'Atendimento r�pido e eficiente.', '20230506', 'AVA006');
INSERT INTO comentario VALUES ('COM007', 'Pre�os competitivos.', '20230507', 'AVA007');
INSERT INTO comentario VALUES ('COM008', 'Poderia ter mais op��es de produtos.', '20230508', 'AVA008');
INSERT INTO comentario VALUES ('COM009', 'Recomendo o servi�o.', '20230509', 'AVA009');
INSERT INTO comentario VALUES ('COM010', 'Nada a reclamar.', '20230510', 'AVA010');

INSERT INTO reservaCliente VALUES ('RES001', '20230601', '20230601', '20230603', 'CLT001');
INSERT INTO reservaCliente VALUES ('RES002', '20230605', '20230605', '20230608', 'CLT002');
INSERT INTO reservaCliente VALUES ('RES003', '20230610', '20230610', '20230612', 'CLT003');
INSERT INTO reservaCliente VALUES ('RES004', '20230615', '20230615', '20230618', 'CLT004');
INSERT INTO reservaCliente VALUES ('RES005', '20230620', '20230620', '20230623', 'CLT005');
INSERT INTO reservaCliente VALUES ('RES006', '20230625', '20230625', '20230628', 'CLT006');
INSERT INTO reservaCliente VALUES ('RES007', '20230701', '20230701', '20230704', 'CLT007');
INSERT INTO reservaCliente VALUES ('RES008', '20230706', '20230706', '20230709', 'CLT008');
INSERT INTO reservaCliente VALUES ('RES009', '20230710', '20230710', '20230713', 'CLT009');
INSERT INTO reservaCliente VALUES ('RES010', '20230715', '20230715', '20230718', 'CLT010');
INSERT INTO reservaCliente VALUES ('RES011', '20230801', '20230801', '20230801', 'CLT001');
INSERT INTO reservaCliente VALUES ('RES012', '20230802', '20230802', '20230802', 'CLT001');
INSERT INTO reservaCliente VALUES ('RES013', '20230826', '20230826', '20230826', 'CLT001');

--clientes que possuem tipoCliente igual 1--
SELECT nome, email, endereco FROM cliente WHERE tipoCliente = 1 ORDER BY nome;

--Essa consulta retornara os alimentos (nome e validade) e seus respectivos clientes (nome)
---para alimentos com quantidade maior que 5, ordenados pela validade do alimento.--
SELECT alimento.nome, alimento.validade, cliente.nome
FROM alimento
JOIN estoque ON alimento.estoqueId = estoque.estoqueId
JOIN cliente ON estoque.clienteId = cliente.clienteId
WHERE alimento.quantidade > 5
ORDER BY alimento.validade;

--Obter a contagem de alimentos por tipo de cliente--
SELECT c.tipoCliente, COUNT(*) AS quantidade_alimentos
FROM alimento a
JOIN estoque e ON a.estoqueId = e.estoqueId
JOIN cliente c ON e.clienteId = c.clienteId
GROUP BY c.tipoCliente;

-- Obter a contagem de avaliações feitas por cada cliente.
SELECT clienteId, COUNT(*) AS total_avaliacoes
FROM avaliacao
GROUP BY clienteId;

-- Obter uma lista de clientes que fizeram movimentações em uma determinada categoria.
SELECT c.nome, m.descricao, m.data_movimentacao
FROM cliente c
JOIN movimentacao m ON c.clienteId = m.clienteIdUsuario
WHERE m.categoria = 'Recebe Doação'
ORDER BY m.data_movimentacao DESC;

-- Obter a contagem de reservas feitas por cada cliente, apenas para clientes que fizeram mais de 3 reservas.
SELECT clienteId, COUNT(*) AS total_reservas
FROM reservaCliente
GROUP BY clienteId
HAVING COUNT(*) > 3;

--Obter a media de quantidade de alimentos por tipo de cliente, considerando apenas os clientes que possuem mais de 3 alimentos:
SELECT c.tipoCliente, AVG(a.quantidade) AS media_alimentos
FROM alimento a
JOIN estoque e ON a.estoqueId = e.estoqueId
JOIN cliente c ON e.clienteId = c.clienteId
GROUP BY c.tipoCliente
HAVING COUNT(*) > 3;

commit;