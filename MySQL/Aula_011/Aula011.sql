
SELECT * FROM cursos;
SELECT * FROM cursos ORDER BY nome;

SELECT * FROM cursos ORDER BY nome DESC;

SELECT ano, nome, carga FROM cursos ORDER BY ano, nome;

SELECT nome, descricao, carga FROM cursos WHERE ano = '2016' ORDER BY nome;

SELECT nome, descricao, carga FROM cursos WHERE ano <= '2015' ORDER BY ano, nome;

SELECT nome, descricao, carga FROM cursos WHERE ano BETWEEN 2014 AND 2016 ORDER BY ano, nome;

SELECT ano, nome, descricao FROM cursos WHERE ano IN (2014, 2016) ORDER BY ano, nome;

SELECT * FROM cursos WHERE carga > 35 AND totaulas < 30 ORDER BY idcurso, nome;

SELECT * FROM cursos WHERE carga > 35 OR totaulas < 30 ORDER BY nome;