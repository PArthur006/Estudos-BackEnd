# Aula 16: INNER JOIN com Várias Tabelas

### 1. A Tabela Associativa (ou Tabela de Junção)

Quando temos um relacionamento **Muitos-para-Muitos (N-N)**, como "um Gafanhoto assiste a muitos Cursos" e "um Curso é assistido por muitos gafanhotos", precisamos de uma tabela intermediária para conectar as duas.
- **Propósito:** Registrar cada "evento" de ligação entre as duas entidades.
- **Estrutura:** A tabela `gafanhoto_assiste_curso` é um exemplo clássico. Sua estrutura principal consiste em:
    - Uma Chave Primária (`id`) para a própria tabela.
    Uma Chave Estrangeira que aponta para a PK de `gafanhotos` (`idgafanhotos`).
    Uma Chave Estrangeira que aponta para a PK de `cursos` (`idcurso`).
    Pode conter outros atributos próprios do relacionamento (ex: `data` em que o curso foi assistido).

### 2. Sintaxe do `JOIN` Múltiplo

Para conectar mais de duas tabelas, simplesmente "encadeamos" as cláusulas `JOIN`. A lógica é que o resultado da primeira junção é então unido à terceira tabela, e assim por diante.

**Sintaxe:**

    ```sql
    SELECT ...
    FROM TabelaA
    JOIN TabelaB ON TabelaA.pk = TabelaB.fk_a
    JOIN TabelaC ON TabelaB.fk_c = TabelaC.pk;
    ```

### 3. Apelidos de Tabela (Aliases)

Para simplificar a escrita e a leitura de `JOIN`s muito complexos, usamos apelidos (aliases) curtos para os nomes das tabelas.
- **Propósito:**
    1. Tornar o código mais limpo e curto.
    2. Evitar ambiguidade quando tabelas diferentes têm colunas com o mesmo nome (ex: `gafanhotos.nome` e `cursos.nome`).
- **Sintaxe:**

    ```sql
    FROM nome_longo_da_tabela AS apelido
    -- ou a forma mais comum e curta:
    FROM nome_longo_da_tabela apelido
    ```

    - **Importante:** Uma vez que um apelido é definido, ele **deve** ser usado no restante da consulta.

### 4. Exemplo da Aula Comentado:

```sql
-- Seleciona o nome do gafanhoto e o nome do curso
SELECT g.nome, c.nome 

-- Ponto de partida: a tabela de gafanhotos (apelidada de 'g')
FROM gafanhotos g

-- Primeira junção: conecta o gafanhoto ('g') com a tabela de assistência ('a')
-- A condição de ligação é o ID do gafanhoto
JOIN gafanhoto_assiste_curso a ON g.id = a.idgafanhoto

-- Segunda junção: conecta o resultado anterior (que já tem os dados de 'a') com a tabela de cursos ('c')
-- A condição de ligação é o ID do curso
JOIN cursos c ON c.idcurso = a.idcurso

-- No final, ordena o resultado pelo nome do gafanhoto
ORDER BY g.nome;
```