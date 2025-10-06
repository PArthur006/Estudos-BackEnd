USE cadastro;

CREATE TABLE gafanhoto_assiste_curso (
    id INT NOT NULL AUTO_INCREMENT,
    data DATE,
    idgafanhoto INT,
    idcurso INT,
    PRIMARY KEY (id),
    FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id),
    FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
) DEFAULT CHARSET = utf8;

INSERT INTO gafanhoto_assiste_curso VALUES
(DEFAULT, '2014-10-10', '2', '15'),
(DEFAULT, '2014-08-22', '3', '8'),
(DEFAULT, '2014-12-03', '4', '12')
;

SELECT * FROM gafanhoto_assiste_curso;

SELECT g.nome, c.nome FROM gafanhotos g
JOIN gafanhoto_assiste_curso a
ON g.id = a.idgafanhoto
JOIN cursos c
ON c.idcurso = a.idcurso
ORDER BY g.nome;