SELECT DISTINCT carga FROM cursos
ORDER BY carga;

SELECT carga FROM cursos
GROUP BY carga;

SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga
ORDER BY COUNT(nome) DESC;

SELECT totaulas, COUNT(*) FROM cursos
GROUP BY totaulas
ORDER BY totaulas;

SELECT totaulas, carga FROM cursos
WHERE totaulas = 30
GROUP BY carga
ORDER BY carga;

SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga
HAVING COUNT(nome) > 3;

SELECT carga, COUNT(*) FROM cursos
WHERE ano > 2015
GROUP BY carga
HAVING carga > (SELECT AVG(carga) FROM cursos)
ORDER BY carga;