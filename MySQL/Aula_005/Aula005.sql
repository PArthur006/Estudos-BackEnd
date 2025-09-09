use cadastro2;

INSERT INTO pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
('Ana', '1975-12-22', 'F', '52.3', '1.45', 'EUA'),
('Pedro', '2006-08-24', 'M', '87.5', '1.80', DEFAULT),
('Júlia', '1999-05-30', 'F', '75.9', '1.7', 'Portugal');

SELECT * FROM pessoas;