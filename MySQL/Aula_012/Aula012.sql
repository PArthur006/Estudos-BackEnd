SELECT * FROM cursos
WHERE nome LIKE 'A%';

SELECT * FROM cursos
WHERE nome LIKE '%A%';

SELECT * FROM cursos
WHERE nome NOT LIKE '%A%';

UPDATE cursos SET nome = "PáOO" WHERE idcurso = '9';

SELECT * FROM cursos
WHERE nome LIKE 'PHP_';

SELECT * FROM gafanhotos
WHERE nome LIKE '%SILVA';

SELECT DISTINCT nacionalidade FROM gafanhotos
ORDER BY nacionalidade; 

SELECT COUNT(*) FROM cursos;

SELECT COUNT(*) FROM cursos
WHERE totaulas >= 20;

SELECT MAX(carga) FROM cursos;

SELECT MAX(totaulas) FROM cursos
WHERE ano = '2016';

SELECT MIN(totaulas) FROM cursos
WHERE ano = '2016';

SELECT SUM(totaulas) FROM cursos
WHERE ano = '2016';

SELECT AVG(totaulas) FROM cursos
WHERE ano = '2016';