CREATE DATABASE cadastro2
default CHARACTER SET utf8
default COLLATE utf8_general_ci;

use cadastro2;
CREATE Table pessoas (
    id int NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE,
    sexo ENUM('M','F'),
    peso DECIMAL(5,2),
    altura DECIMAL(3,2),
    nacionalidade VARCHAR(20) DEFAULT 'Brazil',
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;