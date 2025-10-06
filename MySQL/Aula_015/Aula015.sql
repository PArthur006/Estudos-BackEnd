USE cadastro;

DESCRIBE gafanhotos;

ALTER TABLE gafanhotos
ADD COLUMN cursopreferido INT;

ALTER TABLE gafanhotos 
ADD FOREIGN KEY (cursopreferido)
REFERENCES cursos(idcurso);

SELECT * FROM gafanhotos;

SELECT * FROM cursos;

UPDATE gafanhotos
SET cursopreferido = '6'
WHERE id = '1';

DELETE FROM cursos
WHERE idcurso = '6';

SELECT nome, cursopreferido FROM gafanhotos;

SELECT nome, ano FROM cursos;

SELECT gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano
FROM gafanhotos INNER JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido;

SELECT gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano
FROM gafanhotos LEFT OUTER JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido;