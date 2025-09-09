use cadastro2;

desc gafanhotos;

ALTER Table pessoas
RENAME TO gafanhotos;

ALTER Table pessoas
ADD COLUMN profissao VARCHAR(20) AFTER nome;

ALTER Table pessoas
DROP COLUMN profissao;

ALTER Table pessoas
MODIFY COLUMN profissao VARCHAR(25) DEFAULT '';

ALTER Table pessoas
CHANGE COLUMN profissao prof VARCHAR(20);

SELECT * FROM pessoas;

--- Nova Tabela

CREATE Table IF NOT EXISTS cursos (
    nome VARCHAR(30) NOT NULL UNIQUE,
    descricao TEXT,
    carga INT UNSIGNED,
    totaulas INT UNSIGNED,
    ano YEAR DEFAULT '2016'
) DEFAULT CHARSET=utf8;

ALTER TABLE cursos
ADD idcurso int FIRST;

ALTER TABLE cursos
ADD PRIMARY KEY(idcurso);

DESC cursos;

SELECT * FROM cursos;

--- Tabela de Teste

CREATE TABLE IF NOT EXISTS teste(
    id INT,
    nome VARCHAR(20),
    idade INT
)

INSERT INTO teste VALUES
('1', 'Pedro', '22'),
('2', 'Maria', '12'),
('3', 'Maricota', '77');

SELECT * FROM teste;

DROP TABLE IF EXISTS teste