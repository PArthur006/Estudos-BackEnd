# Aula 12: Consultas com Padrões e Funções de Agregação
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. Filtrando com Padrões de Texto (`LIKE`)

A cláusula `LIKE` é usada com `WHERE` para buscar um padrão específico em uma coluna de texto. É uma ferramenta poderosa para buscas parciais.

**Wildcards (Curingas):**

`LIKE` utiliza caracteres especiais chamados *wildcards* para definir o padrão de busca.

- **`%` (Porcentagem):** Substitui nenhum, um ou vários caracteres.
    - `LIKE 'A%'`: Encontra qualquer texto que **começa** com 'A'.
    - `LIKE '%A'`: Encontra qualquer texto que **termina** com 'A'.
    - `LIKE '%A%'`: Encontra qualquer texto que **contém** 'A' em qualquer posição.
- **`_` (Undescore):** Substitui **exatamente um** único caractere.
    - `LIKE 'PHP_'`: Encontra 'PHP_' (com espaço), 'PHP5', 'PHP7', mas não 'PHP'.
- **Negação:**
    - `NOT LIKE`: Retorna todos os registros que **não** correspondem ao padrão.

**Exemplo:**
```sql
-- Seleciona todos os cursos cujo nome começa com 'A'
SELECT * FROM cursos
WHERE nome LIKE 'A%';

-- Seleciona todos os gafanhotos cujo nome contém 'SILVA' em qualquer posição
SELECT * FROM gafanhotos
WHERE nome LIKE '%SILVA%';
```

### 2. Removendo Duplicatas com `DISTINCT`

O operador `DISTINCT` é usado junto com `SELECT` para retornar apenas valores distintos (únicos), eliminando as repetições de uma coluna no resultado final.

**Sintaxe:**

```sql
SELECT DISTINCT coluna FROM tabela;
```

**Exemplo:**

```sql
-- Retorna uma lista com todas as nacionalidades existentes na tabela, sem repetição
SELECT DISTINCT nacionalidade FROM gafanhotos
ORDER BY nacionalidade;
```

### 3. Funções de Agregação

Funções de agregação realizam um cálculo sobre um conjunto de linhas e retornam um único valor como resultado.

- `COUNT(*)`: Conta o número de registros.
    - `COUNT(*)`: Conta todas as linhas resultantes da consulta.
    - `COUNT(coluna)`: Conta as linhas onde a coluna não é nula.

    ```sql
    -- Conta quantos cursos estão cadastrados
    SELECT COUNT(*) FROM cursos;
    ```

- `MAX(coluna)`: Retorna o maior valor de uma coluna.

    ```sql
    -- Exibe qual é a carga horária máxima entre todos os cursos
    SELECT MAX(carga) FROM cursos;
    ```
- `MIN(coluna)`: Retorna o menor valor de uma coluna.

    ```sql
    -- Exibe o menor total de aulas entre os cursos de 2016
    SELECT MIN(totaulas) FROM cursos WHERE ano = '2016';
    ```
- `SUM(coluna)`: Soma todos os valores de uma coluna numérica.

    ```sql
    -- Soma o total de aulas de todos os cursos de 2016
    SELECT SUM(totaulas) FROM cursos WHERE ano = '2016';
    ``` 
- `AVG(coluna)`: Calcula a média dos valores de uma coluna numérica.

    ```sql
    -- Calcula a média de aulas dos cursos de 2016
    SELECT AVG(totaulas) FROM cursos WHERE ano = '2016';
    ```
