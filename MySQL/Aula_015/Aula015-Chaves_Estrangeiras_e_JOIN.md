# Aula 15: Chaves Estrangeiras e JOIN

### 1.Chave Estrangeira (Foreign Key - FK)

A Chave Estrangeira é a implementação prática de um relacionamento. É uma coluna (ou conjunto de colunas) em uma tabela que cria um link para a Chave Primária de outra tabela.

- **Propósito:** Garantir a **Integridade Referencial** dos dados.
- **Sintaxe para adicionar a uma tabela existente:**
    ```sql
    ALTER TABLE tabela_filha
    ADD FOREIGN KEY (coluna_fk)
    REFERENCES tabela_pai(coluna_pk);
    ```
- **Exemplo da Aula:**
    ```sql
    -- Adiciona a coluna que vai receber a FK
    ALTER TABLE gafanhotos ADD COLUMN cursopreferido INT;

    -- Cria a restrição de FK, ligando a coluna nova à PK da tabela cursos
    ALTER TABLE gafanhotos 
    ADD FOREIGN KEY (cursopreferido)
    REFERENCES cursos(idcurso);
    ```
- **Regras de Integridade (Exemplos):**
    - Você não pode atribuir um `cursopreferido` a um gafanhoto se o `idcurso` não existir na tabela `cursos`.
    - Você não pode apagar um curso da tabela `curso` se algum gafanhoto ainda estiver refeciando aquele curso. (Foi o que aconteceu no exemplo: `DELETE FROM cursos WHERE idcurso = '6';`).

### 2. Storage Engines e ACID

- **Storage Engine:** É o "motor" que o MySQL usa para armazenar, manusear e ler os dados. O motor padrão e mais utilizado é o InnoDB.
- **InnoDB:** É o motor preferido porque ele dá suporte a transações e **restrições de Chave Estrangeira**, garantindo a integridade dos dados.
- **ACID:** É um acrônimo que descreve as propriedades de uma transação confiável, garantidas por motores como o InnoDB.
    - **A**tomicidade: Ou a transação é concluída com sucesso, ou é totalmente revertida.
    - **C**onsistência: Os dados sempre permanecem em um estado válido.
    - **I**solamento: Transações concorrentes não interferem umas nas outras.
    - **D**urabilidade: Uma vez que uma transação é confirmada, os dados não são perdidos.

### 3. Unindo Tabelas com `JOIN`

A cláusula `JOIN` é usada no `SELECT` para combinar linhas de duas ou mais tabelas com base em uma coluna relacionada entre elas (geralmente a PK de uma e a FK de outra).

- **`INNER JOIN` (Junção Interna):** Retorna apenas os registros que possuem um valor correspondente em **ambas as tabelas**. É a interseção dos dados.
- **Sintaxe:**
    ```sql
    SELECT tabela1.coluna, tabela2.coluna
    FROM tabela1 INNER JOIN tabela2
    ON tabela1.fk = tabela2.pk;
    ```
- **`OUTER JOIN` (Junção Externa):** Retorna todos os registros de uma tabela, e os registros correspondentes da outra. Se não houver correspondência, os campos da outra tabela ficam com valor `NULL`.
    - **`LEFT OUTER JOIN` (ou `LEFT JOIN`):** A tabela da **esqueda** (a que vem depois do `FROM`) tem preferência. Todos os seus registros serão listados.
    - **`RIGHT OUTER JOIN` (ou `RIGHT JOIN`):** A tabela da **direira** (a que vem depois do `JOIN`) tem preferência. Todos os seus registros serão listados. (É menos comum, pois geralmente pode ser reescrito como um **LEFT JOIN** invertendo a ordem das tabelas).
